import uuid
import os
from quark.schemas import FileInfo, StorageConfig, FileModel


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
        """
        self.with_image_extra = True
        return self

    def rand_name(self) -> "Storage":
        """
        使用随机文件名
        """
        self.rand_name = True
        return self

    def path(self, path: str) -> "Storage":
        """
        设置保存路径
        """
        self.path = path
        return self

    async def save(self) -> FileInfo:
        """
        保存文件
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
