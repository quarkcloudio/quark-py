from typing import List, Optional, Tuple, Dict
from pydantic import BaseModel
import uuid
import os


class OSSConfig(BaseModel):
    """
    阿里云 OSS 配置模型
    """

    access_key_id: str
    access_key_secret: str
    endpoint: str
    bucket: str
    domain: Optional[str] = None
    is_https: bool = True
    path_prefix: Optional[str] = None
    acl: str = "default"


class MinioConfig(BaseModel):
    """
    MinIO 配置模型
    """

    endpoint: str
    access_key: str
    secret_key: str
    bucket: str
    secure: bool = True
    region: Optional[str] = None
    domain: Optional[str] = None
    path_prefix: Optional[str] = None


class FileInfo(BaseModel):
    """
    文件信息模型
    """

    name: str
    path: str
    size: int
    mime_type: str
    url: str


class FileModel:
    """
    文件模型类
    """

    def __init__(self, content: bytes, name: str = "", header: Optional[Dict] = None):
        self.content = content
        self.name = name
        self.header = header or {}


class StorageConfig(BaseModel):
    """
    存储配置模型
    """

    limit_size: int = 0
    limit_type: List[str] = []
    limit_image_width: int = 0
    limit_image_height: int = 0
    driver: str = "local"
    check_file_exist: bool = True
    oss_config: Optional[OSSConfig] = None
    minio_config: Optional[MinioConfig] = None


class Storage:
    """
    文件系统类
    """

    def __init__(self, config: StorageConfig, file: FileModel):
        self.config = config
        self.file = file
        self.with_image_extra = False
        self.rand_name = False
        self.path = ""

    def with_image_extra(self) -> "Storage":
        """
        添加图片额外处理

        Returns:
            FileSystem: 当前实例
        """
        self.with_image_extra = True
        return self

    def rand_name(self) -> "Storage":
        """
        使用随机文件名

        Returns:
            FileSystem: 当前实例
        """
        self.rand_name = True
        return self

    def path(self, path: str) -> "Storage":
        """
        设置保存路径

        Args:
            path: 保存路径

        Returns:
            FileSystem: 当前实例
        """
        self.path = path
        return self

    async def save(self) -> Tuple[FileInfo, Optional[Exception]]:
        """
        保存文件

        Returns:
            Tuple[FileInfo, Optional[Exception]]: 文件信息和可能的异常
        """
        try:
            # 根据驱动类型选择保存方式
            if self.config.driver == "local":
                return await self._save_local()
            elif self.config.driver == "oss" and self.config.oss_config:
                return await self._save_oss()
            elif self.config.driver == "minio" and self.config.minio_config:
                return await self._save_minio()
            else:
                # 默认本地保存
                return await self._save_local()
        except Exception as e:
            return None, e

    async def _save_local(self) -> Tuple[FileInfo, Optional[Exception]]:
        """
        本地保存文件

        Returns:
            Tuple[FileInfo, Optional[Exception]]: 文件信息和可能的异常
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

        return file_info, None

    async def _save_oss(self) -> Tuple[FileInfo, Optional[Exception]]:
        """
        OSS保存文件（模拟实现）

        Returns:
            Tuple[FileInfo, Optional[Exception]]: 文件信息和可能的异常
        """
        # 这里应该实现真实的OSS上传逻辑
        # 为简化示例，仍然保存到本地
        return await self._save_local()

    async def _save_minio(self) -> Tuple[FileInfo, Optional[Exception]]:
        """
        Minio保存文件（模拟实现）

        Returns:
            Tuple[FileInfo, Optional[Exception]]: 文件信息和可能的异常
        """
        # 这里应该实现真实的Minio上传逻辑
        # 为简化示例，仍然保存到本地
        return await self._save_local()
