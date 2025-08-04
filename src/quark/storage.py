import uuid
import os
from PIL import Image
from io import BytesIO
import base64
from typing import List
from fastapi import UploadFile
from quark.schemas import FileInfo, OSSConfig, MinioConfig


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

    async def get_mime_type(self) -> str:
        return self.file.content_type

    async def get_size(self) -> int:
        content = await self.file.read()
        size_in_bytes = len(content)
        return size_in_bytes

    async def get_bytes(self) -> bytes:
        content = await self.file.read()
        return content

    async def check_limit(self):
        """
        检查文件是否符合上传限制
        """
        if self.limit_size and len(self.file_bytes) > self.limit_size:
            raise ValueError("文件大小超出限制")
        if self.limit_type and not any(
            t in self.file_info.mime_type for t in self.limit_type
        ):
            raise ValueError("文件类型不允许")
        if self.limit_image_width and self.limit_image_height:
            # 检查图片尺寸
            with Image.open(BytesIO(self.file_bytes)) as img:
                width, height = img.size
                if width > self.limit_image_width or height > self.limit_image_height:
                    raise ValueError("图片尺寸超出限制")

    def path(self, path: str) -> "Storage":
        """
        设置保存路径
        """
        self.save_path = path
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
        # 处理文件名
        if self.rand_name:
            ext = os.path.splitext(self.file.name)[1] if self.file.name else ""
            filename = f"{uuid.uuid4()}{ext}"
        else:
            filename = self.file.name or str(uuid.uuid4())

        # 构建完整路径
        if self.path:
            save_path = os.path.join(self.path, filename)
        else:
            save_path = filename

        # 确保目录存在
        directory = os.path.dirname(save_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)

        # 保存文件
        with open(save_path, "wb") as f:
            f.write(self.file.content)

        # 创建文件信息
        file_info = FileInfo(
            name=filename,
            path=save_path,
            size=len(self.file.content),
            mime_type=(
                self.file.header.get("Content-Type", "application/octet-stream")
                if self.file.header
                else "application/octet-stream"
            ),
            url=f"/{save_path}",
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
