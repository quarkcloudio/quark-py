import json
from datetime import datetime

import openpyxl

from ..models.attachment import Attachment
from ..services.config import ConfigService


class AttachmentService:
    def __init__(self):
        self.config_service = ConfigService()

    async def get_list_by_search(
        self, admin_id, attachment_type, category_id, name, createtime, page
    ):
        query = Attachment.filter(status=1, source="ADMIN", uid=admin_id)

        if category_id:
            query = query.filter(category_id=category_id)
        if name:
            query = query.filter(name__contains=name)
        if len(createtime) == 2:
            query = query.filter(created_at__range=(createtime[0], createtime[1]))

        total = await query.count()
        attachments = await query.order_by("-id").offset((page - 1) * 8).limit(8)

        for attachment in attachments:
            attachment.url = (
                await self.get_url(attachment.url)
                + f"?timestamp={int(datetime.now().timestamp())}"
            )

        return attachments, total

    async def insert_get_id(self, attachment):
        await attachment.save()
        return attachment.id

    async def delete_by_id(self, attachment_id):
        return await Attachment.filter(id=attachment_id).delete()

    async def get_info_by_id(self, attachment_id):
        attachment = await Attachment.filter(status=1, id=attachment_id).first()
        return attachment

    async def update_by_id(self, attachment_id, data: Attachment):
        return await Attachment.filter(status=1, id=attachment_id).update(**data)

    async def get_info_by_hash(self, hash_value):
        return await Attachment.filter(status=1, hash=hash_value).first()

    async def get_url(self, *params):
        id = None
        attachment_type = None

        if len(params) == 1:
            id = params[0]
        elif len(params) == 2:
            attachment_type = params[0]
            id = params[1]

        http = ""
        path = ""
        web_site_domain = await self.config_service.get_value("WEB_SITE_DOMAIN")
        if web_site_domain is not None and web_site_domain != "":
            http = (
                "https://"
                if await self.config_service.get_value("SSL_OPEN") == "1"
                else "http://"
            )

        if isinstance(id, str):
            if "://" in id and "{" not in id:
                return id
            if "./" in id and "{" not in id:
                return http + web_site_domain + id.replace("./web/app/", "/", 1)
            if "/" in id and "{" not in id:
                return http + web_site_domain + id
            if "{" in id:
                try:
                    json_data = json.loads(id)
                    if isinstance(json_data, dict):
                        path = json_data.get("url", "")
                    elif isinstance(json_data, list):
                        path = json_data[0].get("url", "")
                except json.JSONDecodeError:
                    pass

            if "://" in path:
                return path
            if "./" in path:
                path = path.replace("./web/app/", "/", 1)
            if path:
                return http + web_site_domain + path

        attachment = await Attachment.filter(id=id, status=1).first()
        if attachment and attachment.id != 0:
            path = attachment.url
            if "://" in path:
                return path
            if "./" in path:
                path = path.replace("./web/app/", "/", 1)
            if path:
                return http + web_site_domain + path

        if attachment_type == "IMAGE":
            return http + web_site_domain + "/admin/default.png"
        return ""

    async def get_file_url(self, id):
        return await self.get_url("FILE", id)

    async def get_image_url(self, id):
        return await self.get_url("IMAGE", id)

    async def get_urls(self, id):
        paths = []
        http = (
            "https://"
            if await self.config_service.get_value("SSL_OPEN") == "1"
            else "http://"
        )
        web_site_domain = await self.config_service.get_value("WEB_SITE_DOMAIN")

        if isinstance(id, str):
            if "{" in id:
                try:
                    json_data = json.loads(id)
                    if isinstance(json_data, list):
                        for v in json_data:
                            path = v.get("url", "")
                            if "://" in path:
                                paths.append(path)
                            else:
                                if "./" in path:
                                    path = path.replace("./web/app/", "/", 1)
                                if path:
                                    path = http + web_site_domain + path
                                paths.append(path)
                except json.JSONDecodeError:
                    pass

        return paths

    async def get_path(self, id):
        path = ""
        if isinstance(id, str):
            if "://" in id and "{" not in id:
                return id
            if "./" in id and "{" not in id:
                return id
            if "/" in id and "{" not in id:
                return id
            if "{" in id:
                try:
                    json_data = json.loads(id)
                    if isinstance(json_data, dict):
                        id = json_data.get("id", "")
                    elif isinstance(json_data, list):
                        id = json_data[0].get("id", "")
                except json.JSONDecodeError:
                    pass

        attachment = await Attachment.filter(id=id, status=1).first()
        return attachment.path if attachment else ""

    async def get_file_path(self, id):
        return await self.get_path(id)

    async def get_image_path(self, id):
        return await self.get_path(id)

    async def get_paths(self, id):
        paths = []
        if isinstance(id, str):
            if "{" in id:
                try:
                    json_data = json.loads(id)
                    if isinstance(json_data, list):
                        for v in json_data:
                            paths.append(await self.get_path(v["id"]))
                except json.JSONDecodeError:
                    pass
        return paths

    async def get_excel_data(self, file_id):
        file = await Attachment.filter(id=file_id, status=1).first()
        if not file:
            return []

        workbook = openpyxl.load_workbook(file.path)
        sheet = workbook.active
        data = []
        for row in sheet.iter_rows(values_only=True):
            data.append(row)
        return data

    async def count_by_type(self, file_type):
        return await Attachment.filter(type=file_type).count()
