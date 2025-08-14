from typing import Any, Dict, List

from pydantic import BaseModel, Field

from quark import Message, Request
from quark.schemas import FileInfo, MinioConfig, OSSConfig
from quark.storage import Storage


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

    async def init(self, request: Request):
        """初始化"""
        return self

    async def handle(self, request: Request) -> Dict[str, Any]:
        """
        执行文件上传
        """
        # 解析 multipart/form-data
        form = await request.form()

        # 获取字段名为 file 的文件
        file = form.get("file")

        try:
            limit_w = request.query_params.get("limitW", "")
            limit_h = request.query_params.get("limitH", "")

            limit_image_width = self.limit_image_width
            if limit_w != "":
                try:
                    limit_image_width = int(limit_w)
                except ValueError:
                    pass  # 保持原值

            limit_image_height = self.limit_image_height
            if limit_h != "":
                try:
                    limit_image_height = int(limit_h)
                except ValueError:
                    pass  # 保持原值

            storage = Storage(
                file=file,
                driver=self.driver,
                oss_config=self.oss_config,
                minio_config=self.minio_config,
                limit_image_height=limit_image_height,
                limit_image_width=limit_image_width,
                limit_size=self.limit_size,
                limit_type=self.limit_type,
                with_image_extra=True,
                rand_name=True,
            )

            # 上传前回调
            before_handle_result = await self.before_handle(request, storage)

            if before_handle_result is not None:
                return before_handle_result

            result = await storage.path(self.save_path).save()

            return await self.after_handle(request, result)
        except Exception as e:
            return Message.error(str(e))

    async def handle_from_base64(self, request: Request) -> Dict[str, Any]:
        """
        通过Base64执行上传
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

            limit_image_width = self.limit_image_width
            if limit_w != "":
                try:
                    limit_image_width = int(limit_w)
                except ValueError:
                    pass

            limit_image_height = self.limit_image_height
            if limit_h != "":
                try:
                    limit_image_height = int(limit_h)
                except ValueError:
                    pass

            storage = Storage(
                file_base64_str=data["file"],
                driver=self.driver,
                oss_config=self.oss_config,
                minio_config=self.minio_config,
                limit_image_height=limit_image_height,
                limit_image_width=limit_image_width,
                limit_size=self.limit_size,
                limit_type=self.limit_type,
                with_image_extra=True,
                rand_name=True,
            )

            # 上传前回调
            before_handle_result = await self.before_handle(request, storage)

            if before_handle_result is not None:
                return before_handle_result

            result = await storage.path(self.save_path).save()

            return await self.after_handle(request, result)

        except Exception as e:
            return Message.error(str(e))

    async def before_handle(self, request: Request, storage: Storage) -> Any:
        """
        上传前回调
        """
        return None

    async def after_handle(self, request: Request, result: FileInfo) -> Any:
        """
        上传后回调
        """
        return Message.success("上传成功", result)
