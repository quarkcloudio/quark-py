# upload.py
from typing import List, Any
from pydantic import BaseModel, Field
from fastapi import UploadFile, Request
import base64
import uuid
import mimetypes
import os
from PIL import Image
import io
from ..component.message.message import Message


# 上传模板类
class Upload(BaseModel):

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
    oss_config: Any = Field(default=None)

    # Minio配置
    minio_config: Any = Field(default=None)

    class Config:
        arbitrary_types_allowed = True

    async def before_handle(self, request: Request, file: UploadFile):
        """
        上传前回调
        """

    async def after_handle(self, request: Request, result: Any):
        """
        上传后回调
        """
        return Message.success("上传成功", result)

    async def handle(self, request: Request):
        """
        执行文件上传
        """

        # 解析 multipart/form-data
        form = await request.form()

        # 获取字段名为 file 的文件
        file = form.get("file")

        # 获取查询参数
        limit_w = request.query_params.get("limitW", "")
        limit_h = request.query_params.get("limitH", "")

        # 获取限制条件
        limit_size = self.limit_size
        limit_type = self.limit_type

        limit_image_width = self.limit_image_width
        if limit_w.isdigit():
            limit_image_width = int(limit_w)

        limit_image_height = self.limit_image_height
        if limit_h.isdigit():
            limit_image_height = int(limit_h)

        try:
            # 读取文件内容
            file_content = await file.read()

            # 上传前回调
            file_info = await self.before_handle(request, file)
            if file_info:
                return await self.after_handle(request, file_info)

            # 保存文件
            with open(f"./uploads/{filename}", "wb") as f:
                f.write(file_content)

            return await self.after_handle(request, file_info)

        except Exception as e:
            return Message.error(str(e))

    async def base64_handle(self, request: Request):
        """
        通过Base64执行上传
        """
        json_data = await request.json()
        base64_str = json_data.get("file")

        # 获取查询参数
        limit_w = request.query_params.get("limitW", "")
        limit_h = request.query_params.get("limitH", "")

        # 解析Base64数据
        if "," not in base64_str:
            return Message.error("格式错误")

        header, encoded = base64_str.split(",", 1)

        try:
            file_content = base64.b64decode(encoded)
        except Exception as e:
            return Message.error(str(e))

        # 获取限制条件
        limit_size = self.limit_size
        limit_type = self.limit_type

        limit_image_width = self.limit_image_width
        if limit_w.isdigit():
            limit_image_width = int(limit_w)

        limit_image_height = self.limit_image_height
        if limit_h.isdigit():
            limit_image_height = int(limit_h)

        try:
            # 确定文件扩展名（从Base64头部）
            ext = ""
            if "jpeg" in header:
                ext = ".jpg"
            elif "png" in header:
                ext = ".png"
            elif "gif" in header:
                ext = ".gif"
            else:
                ext = ".bin"

            filename = f"base64_upload{ext}"

            # 上传前回调
            file_info = await self.before_handle(request, file_system)
            if file_info:
                return await self.after_handle(request, file_info)

            # 保存文件
            with open(f"./uploads/{filename}", "wb") as f:
                f.write(file_content)

            return await self.after_handle(request, file_info)

        except Exception as e:
            return Message.error(str(e))
