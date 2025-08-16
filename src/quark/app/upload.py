import json
from datetime import datetime
from typing import Any

from fastapi import Request

from quark import Message, Storage, Upload
from quark.models import Attachment
from quark.schemas import FileInfo, ImageCropRequest, ImageDeleteRequest
from quark.services import AttachmentCategoryService, AttachmentService, AuthService


class Image(Upload):

    async def init(self, request: Request):
        """
        初始化
        """
        # 限制文件大小
        self.limit_size = 1024 * 1024 * 1024 * 2

        # 限制文件类型
        self.limit_type = [
            "image/png",
            "image/gif",
            "image/jpeg",
            "image/svg+xml",
        ]

        # 设置文件上传路径
        self.save_path = (
            f"./web/app/storage/images/{datetime.now().strftime('%Y%m%d')}/"
        )

        return self

    async def get_list(self, request: Request):
        """
        获取文件列表
        """
        try:
            # 从request中获取参数
            category_id = request.query_params.get("categoryId")
            name = request.query_params.get("name")
            createtime = request.query_params.get("createtime")
            page = request.query_params.get("page", "1")

            # 类型转换
            try:
                category_id = int(category_id) if category_id else None
                page = int(page) if page else 1
            except ValueError:
                page = 1

            current_admin = await AuthService(request).get_current_admin()

            # 使用服务层获取数据
            images, total = await AttachmentService().get_list_by_search(
                current_admin.id, "IMAGE", category_id, name, createtime, page
            )

            # 获取分类列表
            categorys = await AttachmentCategoryService().get_list(current_admin.id)
        except Exception as e:
            return Message.error(str(e))

        return Message.success(
            "获取成功",
            {
                "pagination": {
                    "current": page,
                    "defaultCurrent": 1,
                    "pageSize": 8,
                    "total": total,
                },
                "list": images,
                "categorys": categorys,
            },
        )

    async def delete(self, request: Request):
        """
        图片删除
        """
        try:
            # 从request中解析JSON数据
            request_data = await request.json()

            image_delete_req = ImageDeleteRequest(**request_data)

            await AttachmentService().delete_by_id(image_delete_req.id)

        except Exception as e:
            return Message.error(str(e))

        return Message.success("操作成功")

    async def crop(self, request: Request):
        """
        图片裁剪
        """
        # 从request中解析JSON数据
        request_data = await request.json()

        image_crop_req = ImageCropRequest(**request_data)

        # 获取查询参数
        limit_w = request.query_params.get("limitW")
        limit_h = request.query_params.get("limitH")

        # 获取图片信息
        image_info = await AttachmentService().get_info_by_id(image_crop_req.id)
        if not image_info:
            return Message.error("图片不存在")

        # 解析base64数据
        files = image_crop_req.file.split(",")
        if len(files) != 2:
            return Message.error("格式错误")

        # 获取尺寸限制
        limit_image_width = getattr(self, "limit_image_width", 0)
        limit_image_height = getattr(self, "limit_image_height", 0)

        if limit_w:
            try:
                limit_image_width = int(limit_w)
            except ValueError:
                pass

        if limit_h:
            try:
                limit_image_height = int(limit_h)
            except ValueError:
                pass

        # 创建存储实例
        storage = Storage(
            limit_size=self.limit_size,
            limit_type=self.limit_type,
            limit_image_width=limit_image_width,
            limit_image_height=limit_image_height,
            driver=self.driver,
            save_path=self.save_path,
            file_base64_str=files[1],
        )

        # 处理文件
        file_paths = image_info.path.split("/")
        file_name = file_paths[-1]

        result = await storage.name(file_name).save()

        # 重写URL
        if self.driver == "local":
            result.url = await AttachmentService().get_image_url(result.url)

        # 更新数据库
        extra = ""
        if result.extra:
            extra = json.dumps(result.extra)

        current_admin = await AuthService(request).get_current_admin()

        attachment = Attachment(
            source="ADMIN",
            uid=current_admin.id,
            name=result.name,
            type="IMAGE",
            size=result.size,
            ext=result.ext,
            path=result.path,
            url=result.url,
            hash=result.hash,
            extra=extra,
            status=1,
        )

        await AttachmentService().update_by_id(
            image_info.id,attachment
        )

        # 重新获取更新后的数据
        updated_attachment = await AttachmentService().get_info_by_id(image_info.id)

        return Message.success(
            "操作成功",
            {
                "name": updated_attachment.name,
                "size": updated_attachment.size,
                "ext": updated_attachment.ext,
                "path": updated_attachment.path,
                "url": updated_attachment.url,
                "hash": updated_attachment.hash,
                "extra": (
                    json.loads(updated_attachment.extra)
                    if updated_attachment.extra
                    else None
                ),
            },
        )

    async def before_handle(self, request: Request, storage: Storage) -> Any:
        """
        上传前回调
        """
        try:
            file_hash = await storage.get_hash()
            image_info = await AttachmentService().get_info_by_hash(file_hash)

            if image_info and image_info.id != 0:
                extra = {}
                if image_info.extra:
                    try:
                        extra = json.loads(image_info.extra)
                    except:
                        pass

                file_info = {
                    "name": image_info.name,
                    "size": image_info.size,
                    "ext": image_info.ext,
                    "path": image_info.path,
                    "url": image_info.url,
                    "hash": image_info.hash,
                    "extra": extra,
                }

                return Message.success("获取成功", file_info)

            return None
        except Exception as e:
            return Message.error(str(e))

    async def after_handle(self, request: Request, result: FileInfo) -> Any:
        """
        上传完成后回调
        """
        try:
            # 重写url
            if self.driver == "local":
                result.url = await AttachmentService().get_image_url(result.url)

            extra = ""
            if result.extra:
                extra = json.dumps(result.extra)

            current_admin = await AuthService(request).get_current_admin()

            attachment = Attachment(
                source="ADMIN",
                uid=current_admin.id,
                name=result.name,
                type="IMAGE",
                size=result.size,
                ext=result.ext,
                path=result.path,
                url=result.url,
                hash=result.hash,
                extra=extra,
                status=1,
            )

            # 插入数据库
            attachment_id = await AttachmentService().insert_get_id(attachment)
            return Message.success(
                "上传成功",
                {
                    "id": attachment_id,
                    "contentType": result.mime_type,
                    "ext": result.ext,
                    "hash": result.hash,
                    "name": result.name,
                    "path": result.path,
                    "size": result.size,
                    "url": result.url,
                    "extra": result.extra,
                },
            )

        except Exception as e:
            return Message.error(str(e))


class File(Upload):
    """
    文件上传处理类
    """

    async def init(self, request: Request):
        """
        初始化文件上传配置

        Args:
            ctx: Quark上下文对象

        Returns:
            File: 配置后的File对象
        """
        # 限制文件大小为2GB
        self.limit_size = 1024 * 1024 * 1024 * 2

        # 限制文件类型
        self.limit_type = [
            "image/png",
            "image/gif",
            "image/jpeg",
            "video/mp4",
            "video/mpeg",
            "application/x-xls",
            "application/x-ppt",
            "application/msword",
            "application/zip",
            "application/pdf",
            "application/vnd.ms-excel",
            "application/vnd.ms-powerpoint",
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            "application/vnd.openxmlformats-officedocument.presentationml.presentation",
        ]

        # 设置文件上传路径
        self.save_path = f"./web/app/storage/files/{datetime.now().strftime('%Y%m%d')}/"

        return self

    async def before_handle(self, request: Request, storage: Storage) -> Any:
        """
        上传前回调处理

        Args:
            request: 请求对象
            storage: 存储对象

        Returns:
            Any: 处理结果
        """
        try:
            file_hash = await storage.get_hash()
        except Exception as e:
            return Message.error(str(e))

        try:
            file_info = await AttachmentService().get_info_by_hash(file_hash)
        except Exception as e:
            return Message.error(str(e))

        if file_info and file_info.id != 0:
            extra = {}
            if file_info.extra:
                try:
                    extra = json.loads(file_info.extra)
                except (json.JSONDecodeError, TypeError):
                    pass

            file_info_obj = FileInfo(
                name=file_info.name,
                size=file_info.size,
                ext=file_info.ext,
                path=file_info.path,
                url=file_info.url,
                hash=file_info.hash,
                extra=extra,
            )
            return Message.success("获取成功", file_info_obj)

        return None

    async def after_handle(self, request: Request, result: FileInfo) -> Any:
        """
        上传完成后回调处理

        Args:
            request: 请求对象
            result: 文件信息对象

        Returns:
            Any: 处理结果
        """

        # 重写url
        if self.driver == "local":
            result.url = await AttachmentService().get_file_url(result.url)

        try:
            admin_info = await AuthService(request).get_current_admin()
        except Exception as e:
            return Message.error(str(e))

        extra = ""
        if result.extra is not None:
            try:
                extra_data = json.dumps(result.extra)
                extra = extra_data
            except (TypeError, ValueError):
                pass

        # 插入数据库
        try:
            attachment = Attachment(
                source="ADMIN",
                uid=admin_info.id,
                name=result.name,
                type="FILE",
                size=result.size,
                ext=result.ext,
                path=result.path,
                url=result.url,
                hash=result.hash,
                extra=extra,
                status=1,
            )
            id = await AttachmentService().insert_get_id(attachment)
        except Exception as e:
            return Message.error(str(e))

        return Message.success(
            "上传成功",
            {
                "id": id,
                "contentType": result.mime_type,
                "ext": result.ext,
                "hash": result.hash,
                "name": result.name,
                "path": result.path,
                "size": result.size,
                "url": result.url,
                "extra": result.extra,
            },
        )
