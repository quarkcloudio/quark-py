import base64
import hashlib
import os
import uuid
from io import BytesIO
from typing import List

import filetype
from fastapi import UploadFile
from PIL import Image

from quark.schemas import FileInfo, MinioConfig, OSSConfig


class Storage:
    """
    文件系统类
    """

    # 文件对象
    file: UploadFile = None

    # Base64文件字符串
    file_base64_str: str = None

    # 文件字节流
    file_bytes: bytes = None

    # 上传限制
    limit_size: int = None

    # 允许的文件类型
    limit_type: List[str] = None

    # 限制图片宽度
    limit_image_width: int = None

    # 限制图片高度
    limit_image_height: int = None

    # 存储驱动
    driver: str = "local"

    # 是否上传图片时返回图片的额外信息
    with_image_extra = False

    # 是否随机文件名
    rand_name: bool = False

    # 保存路径
    save_path: str = ""

    # 保存文件名称
    save_name: str = ""

    # OSS配置
    oss_config: OSSConfig = None

    # Minio配置
    minio_config: MinioConfig = None

    def __init__(
        self,
        file: UploadFile = None,
        file_base64_str: str = None,
        file_bytes: bytes = None,
        limit_size: int = None,
        limit_type: list = None,
        limit_image_width: int = None,
        limit_image_height: int = None,
        rand_name: bool = None,
        save_path: str = None,
        save_name: str = None,
        oss_config: OSSConfig = None,
        minio_config: MinioConfig = None,
        driver: str = None,
        with_image_extra: bool = None,
    ):
        self.file = file
        self.file_base64_str = file_base64_str
        self.file_bytes = file_bytes
        self.driver = driver
        self.with_image_extra = with_image_extra
        self.oss_config = oss_config
        self.minio_config = minio_config
        self.limit_size = limit_size
        self.limit_type = limit_type
        self.limit_image_width = limit_image_width
        self.limit_image_height = limit_image_height
        self.rand_name = rand_name
        self.save_path = save_path
        self.save_name = save_name

    async def get_mime_type(self) -> str:
        if self.file is not None:
            return self.file.content_type
        elif self.file_base64_str is not None:
            kind = filetype.guess(base64.b64decode(self.file_base64_str))
            if kind is not None:
                return kind.mime
            else:
                return "application/octet-stream"
        elif self.file_bytes is not None:
            kind = filetype.guess(self.file_bytes)
            if kind is not None:
                return kind.mime
            else:
                return "application/octet-stream"
        else:
            return "application/octet-stream"

    async def get_ext(self) -> str:
        if self.file is not None:
            return os.path.splitext(self.file.filename)[1]
        elif self.file_base64_str is not None:
            kind = filetype.guess(base64.b64decode(self.file_base64_str))
            if kind is not None:
                return kind.extension
            else:
                return ""
        elif self.file_bytes is not None:
            kind = filetype.guess(self.file_bytes)
            if kind is not None:
                return kind.extension
            else:
                return ""
        else:
            return ""

    async def get_size(self) -> int:
        if self.file is not None:
            return self.file.size
        elif self.file_base64_str is not None:
            return len(base64.b64decode(self.file_base64_str))
        elif self.file_bytes is not None:
            return len(self.file_bytes)
        else:
            return 0

    async def get_bytes(self) -> bytes:
        # 如果已经有缓存，直接返回
        if self.file_bytes is not None:
            return self.file_bytes

        if self.file is not None:
            self.file_bytes = await self.file.read()
            return self.file_bytes
        elif self.file_base64_str is not None:
            self.file_bytes = base64.b64decode(self.file_base64_str)
            return self.file_bytes
        elif self.file_bytes is not None:
            return self.file_bytes
        else:
            return b""

    async def get_hash(self) -> str:
        """
        获取文件哈希值
        """
        file_bytes = await self.get_bytes()
        filename = self.save_name or self.file.filename
        return hashlib.md5(file_bytes + filename.encode()).hexdigest()

    async def check_limit(self):
        """
        检查文件是否符合上传限制
        """
        file_size = await self.get_size()
        file_mime_type = await self.get_mime_type()
        if self.limit_size and file_size > self.limit_size:
            raise ValueError("文件大小超出限制")
        if self.limit_type and not any(t in file_mime_type for t in self.limit_type):
            raise ValueError("文件类型不允许")
        if self.limit_image_width and self.limit_image_height:
            # 检查图片尺寸
            with Image.open(BytesIO(await self.get_bytes())) as img:
                width, height = img.size
                if width > self.limit_image_width or height > self.limit_image_height:
                    raise ValueError("图片尺寸超出限制")

    def path(self, path: str) -> "Storage":
        """
        设置保存路径
        """
        self.save_path = path
        return self

    def name(self, name: str) -> "Storage":
        """
        设置保存文件名
        """
        self.save_name = name
        return self

    async def save(self) -> FileInfo:
        """
        保存文件
        """
        try:
            # 根据驱动类型选择保存方式
            if self.driver == "local":
                return await self._save_local()
            elif self.driver == "oss" and self.oss_config:
                return await self._save_oss()
            elif self.driver == "minio" and self.minio_config:
                return await self._save_minio()
            else:
                # 默认本地保存
                return await self._save_local()
        except Exception as e:
            raise e

    async def _save_local(self) -> FileInfo:
        """
        本地保存文件
        """
        # 检查文件是否符合上传限制
        await self.check_limit()

        ext = await self.get_ext()
        # 处理文件名
        if self.rand_name:
            filename = f"{uuid.uuid4()}{ext}"
        else:
            filename = self.save_name or self.file.filename or f"{uuid.uuid4()}{ext}"

        # 构建完整路径
        if self.save_path:
            save_path = os.path.join(self.save_path, filename)
        else:
            save_path = filename

        # 确保目录存在
        directory = os.path.dirname(save_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)

        file_bytes = await self.get_bytes()
        file_size = await self.get_size()
        file_mime_type = await self.get_mime_type()

        # 保存文件
        with open(save_path, "wb") as f:
            f.write(file_bytes)

        # 创建文件信息
        file_info = FileInfo(
            name=filename,
            ext=ext,
            path=save_path,
            size=file_size,
            mime_type=file_mime_type,
            url=f"{save_path}",
            hash=await self.get_hash(),
        )
        return file_info

    async def _save_oss(self) -> FileInfo:
        """
        OSS保存文件（模拟实现）
        """
        # 这里应该实现真实的OSS上传逻辑
        # 为简化示例，仍然保存到本地
        return await self._save_local()

    async def _save_minio(self) -> FileInfo:
        """
        Minio保存文件（模拟实现）
        """
        # 这里应该实现真实的Minio上传逻辑
        # 为简化示例，仍然保存到本地
        return await self._save_local()
