from typing import Any, Dict, Optional

from pydantic import BaseModel, field_validator


class LoginData(BaseModel):
    username: str
    password: str
    captcha: Dict[str, str]

    @field_validator("captcha")
    def captcha_must_have_id_and_value(cls, v):
        if "id" not in v or not v["id"]:
            raise ValueError("验证码ID不能为空")
        if "value" not in v or not v["value"]:
            raise ValueError("验证码不能为空")
        return v


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
    ext: str
    path: str
    size: int
    mime_type: str
    url: str
    hash: str
    extra: Optional[Dict[str, Any]] = None


class ImageListRequest(BaseModel):
    categoryId: Optional[int] = None
    name: Optional[str] = None
    createtime: Optional[str] = None
    page: int = 1


class ImageDeleteRequest(BaseModel):
    id: int


class ImageCropRequest(BaseModel):
    id: int
    file: str
