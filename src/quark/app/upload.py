import base64
import hashlib
import json
import os
from datetime import datetime
from typing import Any, Dict, Optional, Tuple

from fastapi import HTTPException, Request

from quark import Message, Storage, Upload
from quark.schemas import FileInfo, ImageCropRequest, ImageDeleteRequest
from quark.services import AttachmentCategoryService, AttachmentService, AuthService


class Image(Upload):

    def init(self) -> "Image":
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
            images, total = await AttachmentService.get_list_by_search(
                current_admin.id, "IMAGE", category_id, name, createtime, page
            )

            # 获取分类列表
            categorys = await AttachmentCategoryService.get_list(current_admin.id)
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

            await AttachmentService.delete_by_id(image_delete_req.id)
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
        image_info = await AttachmentService.get_info_by_id(image_crop_req.id)
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
            limit_types=self.limit_type,
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
            result["url"] = AttachmentService.get_image_url(result["url"])

        # 更新数据库
        extra = ""
        if result.get("extra"):
            extra = json.dumps(result["extra"])

        current_admin = await AuthService(request).get_current_admin()

        await AttachmentService.update_by_id(
            image_info.id,
            source="ADMIN",
            uid=current_admin.id,
            name=result["name"],
            type="IMAGE",
            size=result["size"],
            ext=result["ext"],
            path=result["path"],
            url=result["url"],
            hash=result["hash"],
            extra=extra,
            status=1,
        )

        # 重新获取更新后的数据
        updated_attachment = await AttachmentService.get_info_by_id(image_info.id)

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

    async def before_handle(
        self, file_system: Any
    ) -> Tuple[Any, Optional[Dict], Optional[Exception]]:
        """
        上传前回调
        """
        try:
            file_hash = file_system.get_file_hash()
            image_info = await AttachmentService.get_info_by_hash(file_hash)

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

                return file_system, file_info, None

            return file_system, None, None
        except Exception as e:
            return file_system, None, e

    async def after_handle(self, request: Request, result: FileInfo) -> Dict:
        """
        上传完成后回调
        """
        try:
            # 重写url
            if self.driver == "local":
                result["url"] = AttachmentService.get_image_url(result["url"])

            extra = ""
            if result.get("extra"):
                extra = json.dumps(result["extra"])

            current_admin = await AuthService(request).get_current_admin()

            # 插入数据库
            attachment_id = await AttachmentService.insert_get_id(
                source="ADMIN",
                uid=current_admin.id,
                name=result["name"],
                type="IMAGE",
                size=result["size"],
                ext=result["ext"],
                path=result["path"],
                url=result["url"],
                hash=result["hash"],
                extra=extra,
                status=1,
            )
            return Message.success(
                "上传成功",
                {
                    "id": attachment_id,
                    "contentType": result.get("content_type", ""),
                    "ext": result["ext"],
                    "hash": result["hash"],
                    "name": result["name"],
                    "path": result["path"],
                    "size": result["size"],
                    "url": result["url"],
                    "extra": result.get("extra", {}),
                },
            )

        except Exception as e:
            return Message.error(str(e))

    async def handle(self, request: Request):
        """
        文件上传处理
        """
        try:
            # 检查文件类型
            if file.content_type not in self.limit_type:
                raise HTTPException(status_code=400, detail="不支持的文件类型")

            # 读取文件内容
            file_content = await file.read()

            # 创建文件系统模拟对象
            class FileSystemMock:
                def __init__(self, content):
                    self.content = content

                def get_file_hash(self):
                    return hashlib.md5(self.content).hexdigest()

            file_system = FileSystemMock(file_content)

            # 上传前回调
            _, file_info, _ = await self.before_handle(file_system)

            if file_info:
                return {"code": 200, "msg": "上传成功", "data": file_info}

            # 保存文件
            filename = f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{file.filename}"

            # 确保目录存在
            os.makedirs(self.save_path, exist_ok=True)

            file_path = os.path.join(self.save_path, filename)
            async with aiofiles.open(file_path, "wb") as out_file:
                await out_file.write(file_content)

            # 获取文件URL
            file_url = f"/storage/images/{datetime.now().strftime('%Y%m%d')}/{filename}"

            # 构造结果
            result = {
                "name": filename,
                "size": len(file_content),
                "ext": os.path.splitext(filename)[1],
                "path": file_path,
                "url": file_url,
                "hash": file_system.get_file_hash(),
                "content_type": file.content_type,
            }

            # 上传后回调
            return await self.after_handle(result, result)

        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    async def handle_from_base64(self, request: Request):
        """
        Base64文件上传处理
        """
        try:
            # 从request中解析表单数据
            form_data = await request.form()
            file = form_data.get("file")

            if not file:
                raise HTTPException(status_code=400, detail="文件数据为空")

            # 解析base64数据
            files = file.split(",")
            if len(files) != 2:
                raise HTTPException(status_code=400, detail="格式错误")

            image_data = base64.b64decode(files[1])

            # 创建文件系统模拟对象
            class FileSystemMock:
                def __init__(self, content):
                    self.content = content

                def get_file_hash(self):
                    return hashlib.md5(self.content).hexdigest()

            file_system = FileSystemMock(image_data)

            # 上传前回调
            _, file_info, _ = await self.before_handle(file_system)

            if file_info:
                return {"code": 200, "msg": "上传成功", "data": file_info}

            # 保存文件
            filename = f"{datetime.now().strftime('%Y%m%d%H%M%S')}.png"  # 默认png格式

            # 确保目录存在
            os.makedirs(self.save_path, exist_ok=True)

            file_path = os.path.join(self.save_path, filename)
            async with aiofiles.open(file_path, "wb") as out_file:
                await out_file.write(image_data)

            # 获取文件URL
            file_url = f"/storage/images/{datetime.now().strftime('%Y%m%d')}/{filename}"

            # 构造结果
            result = {
                "name": filename,
                "size": len(image_data),
                "ext": ".png",
                "path": file_path,
                "url": file_url,
                "hash": file_system.get_file_hash(),
                "content_type": "image/png",
            }

            # 上传后回调
            return await self.after_handle(result, result)

        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
