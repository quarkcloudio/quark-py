# upload.py
from typing import List, Optional, Union, Dict, Any
from pydantic import BaseModel, Field
from fastapi import FastAPI, File, UploadFile, Form, HTTPException, Request
import base64
import uuid
import mimetypes
import os
from PIL import Image
import io


# Pydantic模型定义
class OSSConfig(BaseModel):
    access_key: str = ""
    secret_key: str = ""
    endpoint: str = ""
    bucket: str = ""


class MinioConfig(BaseModel):
    endpoint: str = ""
    access_key: str = ""
    secret_key: str = ""
    bucket: str = ""


class FileInfo(BaseModel):
    name: str = ""
    path: str = ""
    url: str = ""
    size: int = 0


class StorageConfig(BaseModel):
    limit_size: int = Field(default=0, description="限制文件大小(字节)")
    limit_type: List[str] = Field(default_factory=list, description="限制文件类型")
    limit_image_width: int = Field(default=0, description="限制图片宽度")
    limit_image_height: int = Field(default=0, description="限制图片高度")
    driver: str = Field(default="local", description="存储驱动")
    check_file_exist: bool = Field(default=True, description="检查文件是否已存在")
    oss_config: Optional[OSSConfig] = Field(default=None, description="OSS配置")
    minio_config: Optional[MinioConfig] = Field(default=None, description="Minio配置")


class FileModel(BaseModel):
    name: str = ""
    content: bytes = b""
    header: Dict[str, str] = Field(default_factory=dict)

    class Config:
        arbitrary_types_allowed = True


class UploadResponse(BaseModel):
    code: int = 200
    msg: str = "上传成功"
    data: Optional[FileInfo] = None


class Base64UploadRequest(BaseModel):
    file: str = Field(..., description="Base64编码的文件数据")


# 文件系统类
class FileSystem:
    def __init__(self, config: StorageConfig):
        self.config = config
        self.file: Optional[FileModel] = None
        self.with_image_extra_flag = False
        self.rand_name_flag = False
        self.save_path = "uploads"

    def reader(self, file: FileModel) -> "FileSystem":
        self.file = file
        return self

    def with_image_extra(self) -> "FileSystem":
        self.with_image_extra_flag = True
        return self

    def rand_name(self) -> "FileSystem":
        self.rand_name_flag = True
        return self

    def path(self, save_path: str) -> "FileSystem":
        self.save_path = save_path
        return self

    def save(self) -> tuple[Optional[FileInfo], Optional[Exception]]:
        try:
            if not self.file:
                return None, Exception("文件未设置")

            # 检查文件大小
            if (
                self.config.limit_size > 0
                and len(self.file.content) > self.config.limit_size
            ):
                return None, Exception(
                    f"文件大小超过限制 {self.config.limit_size} 字节"
                )

            # 检查文件类型
            if self.config.limit_type:
                file_type = mimetypes.guess_type(self.file.name)[0] or ""
                if file_type not in self.config.limit_type:
                    # 也检查文件扩展名
                    ext = os.path.splitext(self.file.name)[1].lower()
                    allowed_exts = [
                        t.split("/")[-1] if "/" in t else t
                        for t in self.config.limit_type
                    ]
                    if (
                        ext not in allowed_exts
                        and file_type not in self.config.limit_type
                    ):
                        return None, Exception(f"不支持的文件类型: {file_type}")

            # 处理图片尺寸检查
            if self.config.limit_image_width > 0 or self.config.limit_image_height > 0:
                try:
                    img = Image.open(io.BytesIO(self.file.content))
                    width, height = img.size

                    if (
                        self.config.limit_image_width > 0
                        and width != self.config.limit_image_width
                    ):
                        return None, Exception(
                            f"图片宽度必须为 {self.config.limit_image_width} 像素"
                        )

                    if (
                        self.config.limit_image_height > 0
                        and height != self.config.limit_image_height
                    ):
                        return None, Exception(
                            f"图片高度必须为 {self.config.limit_image_height} 像素"
                        )
                except Exception:
                    # 如果不是图片文件，跳过尺寸检查
                    pass

            # 生成随机文件名
            if self.rand_name_flag and self.file:
                name, ext = os.path.splitext(self.file.name)
                self.file.name = f"{uuid.uuid4().hex}{ext}"

            # 确保保存路径存在
            os.makedirs(self.save_path, exist_ok=True)

            # 保存文件
            file_path = os.path.join(self.save_path, self.file.name)

            # 检查文件是否已存在
            if self.config.check_file_exist and os.path.exists(file_path):
                name, ext = os.path.splitext(self.file.name)
                self.file.name = f"{name}_{uuid.uuid4().hex[:8]}{ext}"
                file_path = os.path.join(self.save_path, self.file.name)

            with open(file_path, "wb") as f:
                f.write(self.file.content)

            file_info = FileInfo(
                name=self.file.name,
                path=file_path,
                url=f"/{file_path}",
                size=len(self.file.content),
            )

            return file_info, None

        except Exception as e:
            return None, e


def new_storage(config: StorageConfig) -> FileSystem:
    return FileSystem(config)


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
    oss_config: Optional[OSSConfig] = Field(default=None)

    # Minio配置
    minio_config: Optional[MinioConfig] = Field(default=None)

    class Config:
        arbitrary_types_allowed = True

    def get_storage_config(self) -> StorageConfig:
        return StorageConfig(
            limit_size=self.limit_size,
            limit_type=self.limit_type,
            limit_image_width=self.limit_image_width,
            limit_image_height=self.limit_image_height,
            driver=self.driver,
            oss_config=self.oss_config,
            minio_config=self.minio_config,
        )

    async def before_handle(
        self, request: Request, file_system: FileSystem
    ) -> tuple[FileSystem, Optional[FileInfo], Optional[Exception]]:
        """
        上传前回调
        """
        return file_system, None, None

    async def after_handle(
        self, request: Request, result: Optional[FileInfo]
    ) -> UploadResponse:
        """
        上传后回调
        """
        return UploadResponse(code=200, msg="上传成功", data=result)

    async def handle(
        self, request: Request, resource: str, file: UploadFile = File(...)
    ) -> UploadResponse:
        """
        执行文件上传
        """
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

            # 创建文件系统对象
            storage_config = self.get_storage_config()
            storage_config.limit_image_width = limit_image_width
            storage_config.limit_image_height = limit_image_height

            file_system = new_storage(storage_config).reader(
                FileModel(
                    content=file_content,
                    name=file.filename or "unnamed_file",
                    header=dict(file.headers),
                )
            )

            # 上传前回调
            get_file_system, file_info, err = await self.before_handle(
                request, file_system
            )
            if err:
                raise HTTPException(status_code=400, detail=str(err))

            if file_info:
                return await self.after_handle(request, file_info)

            # 保存文件
            result, err = (
                get_file_system.with_image_extra()
                .rand_name()
                .path(self.save_path)
                .save()
            )

            if err:
                raise HTTPException(status_code=400, detail=str(err))

            return await self.after_handle(request, result)

        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    async def handle_from_base64(
        self, request: Request, resource: str, body: Base64UploadRequest
    ) -> UploadResponse:
        """
        通过Base64执行上传
        """
        # 获取查询参数
        limit_w = request.query_params.get("limitW", "")
        limit_h = request.query_params.get("limitH", "")

        # 解析Base64数据
        if "," not in body.file:
            raise HTTPException(status_code=400, detail="格式错误")

        header, encoded = body.file.split(",", 1)

        try:
            file_data = base64.b64decode(encoded)
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Base64解码失败: {str(e)}")

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

            # 创建文件系统对象
            storage_config = self.get_storage_config()
            storage_config.limit_image_width = limit_image_width
            storage_config.limit_image_height = limit_image_height

            file_system = new_storage(storage_config).reader(
                FileModel(content=file_data, name=filename)
            )

            # 上传前回调
            get_file_system, file_info, err = await self.before_handle(
                request, file_system
            )
            if err:
                raise HTTPException(status_code=400, detail=str(err))

            if file_info:
                return await self.after_handle(request, file_info)

            # 保存文件
            result, err = (
                get_file_system.with_image_extra()
                .rand_name()
                .path(self.save_path)
                .save()
            )

            if err:
                raise HTTPException(status_code=400, detail=str(err))

            return await self.after_handle(request, result)

        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))


# FastAPI应用
app = FastAPI(title="文件上传API", description="基于Pydantic的文件上传服务")

# 创建上传模板实例
upload_template = UploadTemplate()


# 路由定义
@app.post("/api/admin/upload/{resource}/handle", response_model=UploadResponse)
async def upload_file(request: Request, resource: str, file: UploadFile = File(...)):
    """
    文件上传接口
    """
    return await upload_template.handle(request, resource, file)


@app.post("/api/admin/upload/{resource}/base64Handle", response_model=UploadResponse)
async def upload_base64_file(
    request: Request, resource: str, body: Base64UploadRequest
):
    """
    Base64文件上传接口
    """
    return await upload_template.handle_from_base64(request, resource, body)
