import base64
from typing import List, Optional, Tuple, Dict, Any
from fastapi import Request
from pydantic import BaseModel, Field
from quark.schemas import FileInfo, OSSConfig, MinioConfig, StorageConfig, FileModel
from ..component.message.message import Message


class Upload(BaseModel):
    """
    文件上传模板类

    处理文件上传的核心逻辑，支持普通文件上传和Base64格式上传
    """

    # 上传限制
    limit_size: int = Field(default=0)

    # 允许的文件类型
    limit_type: List[str] = Field(default_factory=list)

    # 限制图片宽度
    limit_image_width: int = Field(default=0)

    # 限制图片高度
    limit_image_height: int = Field(default=0)

    # 存储驱动
    driver: str = Field(default="local")

    # 保存路径
    save_path: str = Field(default="uploads")

    # OSS配置
    oss_config: OSSConfig = Field(default=None)

    # Minio配置
    minio_config: MinioConfig = Field(default=None)

    def get_limit_size(self) -> int:
        """
        获取限制文件大小

        Returns:
            int: 文件大小限制(字节)
        """
        return self.limit_size

    def get_limit_type(self) -> List[str]:
        """
        获取限制文件类型列表

        Returns:
            List[str]: 允许的文件类型列表
        """
        return self.limit_type

    def get_limit_image_width(self) -> int:
        """
        获取限制图片宽度

        Returns:
            int: 图片宽度限制
        """
        return self.limit_image_width

    def get_limit_image_height(self) -> int:
        """
        获取限制图片高度

        Returns:
            int: 图片高度限制
        """
        return self.limit_image_height

    def get_driver(self) -> str:
        """
        获取存储驱动

        Returns:
            str: 存储驱动类型
        """
        return self.driver

    def get_save_path(self) -> str:
        """
        获取文件保存路径

        Returns:
            str: 文件保存路径
        """
        return self.save_path

    def get_oss_config(self) -> Optional[OSSConfig]:
        """
        获取OSS配置

        Returns:
            Optional[OSSConfig]: OSS配置对象
        """
        return self.oss_config

    def get_minio_config(self) -> Optional[MinioConfig]:
        """
        获取Minio配置

        Returns:
            Optional[MinioConfig]: Minio配置对象
        """
        return self.minio_config

    async def handle(self, request: Request) -> Dict[str, Any]:
        """
        执行文件上传

        Args:
            request: HTTP请求对象
            resource: 资源标识
            file: 上传的文件

        Returns:
            Dict[str, Any]: 上传结果
        """
        # 解析 multipart/form-data
        form = await request.form()

        # 获取字段名为 file 的文件
        file = form.get("file")

        try:
            limit_w = request.query_params.get("limitW", "")
            limit_h = request.query_params.get("limitH", "")

            # 读取文件内容
            file_content = await file.read()

            limit_size = self.get_limit_size()
            limit_type = self.get_limit_type()

            limit_image_width = self.get_limit_image_width()
            if limit_w != "":
                try:
                    limit_image_width = int(limit_w)
                except ValueError:
                    pass  # 保持原值

            limit_image_height = self.get_limit_image_height()
            if limit_h != "":
                try:
                    # 注意：原Go代码这里有bug，应该是limit_image_height
                    limit_image_height = int(limit_h)
                except ValueError:
                    pass  # 保持原值

            driver = self.get_driver()
            oss_config = self.get_oss_config()
            minio_config = self.get_minio_config()
            save_path = self.get_save_path()

            file_system = new_storage(
                StorageConfig(
                    limit_size=limit_size,
                    limit_type=limit_type,
                    limit_image_width=limit_image_width,
                    limit_image_height=limit_image_height,
                    driver=driver,
                    check_file_exist=True,
                    oss_config=oss_config,
                    minio_config=minio_config,
                )
            ).reader(
                FileModel(
                    content=file_content,
                    name=file.filename or "",
                    header=dict(file.headers),
                )
            )

            # 上传前回调
            get_file_system, file_info = self.before_handle(request, file_system)

            if file_info:
                return self.after_handle(request, file_info)

            result = (
                await get_file_system.with_image_extra()
                .rand_name()
                .path(save_path)
                .save()
            )

            return self.after_handle(request, result)
        except Exception as e:
            return Message.error(str(e))

    async def handle_from_base64(self, request: Request) -> Dict[str, Any]:
        """
        通过Base64执行上传

        Args:
            request: HTTP请求对象
            resource: 资源标识
            file_data: Base64编码的文件数据

        Returns:
            Dict[str, Any]: 上传结果
        """

        try:
            limit_w = request.query_params.get("limitW", "")
            limit_h = request.query_params.get("limitH", "")

            try:
                data = await request.json()
            except ValueError as e:
                return Message.error(str(e))

            if "file" not in data:
                return Message.error("参数错误")

            files = data["file"].split(",")
            if len(files) != 2:
                return Message.error("格式错误")

            try:
                file_content = base64.b64decode(files[1])
            except Exception as e:
                return Message.error(f"Base64解码失败: {str(e)}")

            limit_size = self.get_limit_size()
            limit_type = self.get_limit_type()

            limit_image_width = self.get_limit_image_width()
            if limit_w != "":
                try:
                    limit_image_width = int(limit_w)
                except ValueError:
                    pass

            limit_image_height = self.get_limit_image_height()
            if limit_h != "":
                try:
                    # 注意：原Go代码这里有bug
                    limit_image_height = int(limit_h)
                except ValueError:
                    pass

            save_path = self.get_save_path()
            driver = self.get_driver()
            oss_config = self.get_oss_config()
            minio_config = self.get_minio_config()

            file_system = new_storage(
                StorageConfig(
                    limit_size=limit_size,
                    limit_type=limit_type,
                    limit_image_width=limit_image_width,
                    limit_image_height=limit_image_height,
                    driver=driver,
                    check_file_exist=True,
                    oss_config=oss_config,
                    minio_config=minio_config,
                )
            ).reader(FileModel(content=file_content))

            # 上传前回调
            get_file_system, file_info = self.before_handle(request, file_system)

            if file_info:
                return self.after_handle(request, file_info)

            result = (
                await get_file_system.with_image_extra()
                .rand_name()
                .path(save_path)
                .save()
            )

            return self.after_handle(request, result)

        except Exception as e:
            return Message.error(str(e))

    def before_handle(
        self, request: Request, file_system: FileSystem
    ) -> Tuple[FileSystem, Optional[FileInfo]]:
        """
        上传前回调

        Args:
            ctx: 上下文对象
            file_system: 文件系统对象

        Returns:
            Tuple[FileSystem, Optional[FileInfo]]: 文件系统对象和文件信息（如果有）
        """
        # 默认实现，可以被子类重写
        return file_system, None

    def after_handle(self, request: Request, result: FileInfo) -> Dict[str, Any]:
        """
        上传后回调

        Args:
            ctx: 上下文对象
            result: 文件信息对象

        Returns:
            Dict[str, Any]: 上传成功的响应结果
        """
        return Message.success("上传成功", result)
