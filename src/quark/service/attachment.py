from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import json
import os
from datetime import datetime
import openpyxl

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quark.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)

# 定义Attachment模型
class Attachment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    path = db.Column(db.String(255), nullable=False)
    url = db.Column(db.String(255), nullable=False)
    hash = db.Column(db.String(255), nullable=False)
    category_id = db.Column(db.Integer, nullable=True)
    type = db.Column(db.String(50), nullable=True)
    source = db.Column(db.String(50), nullable=False)
    uid = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Integer, nullable=False, default=1)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Attachment {self.name}>'

# 初始化数据库
with app.app_context():
    db.create_all()

# 假设的ConfigService类
class ConfigService:
    def get_value(self, key):
        # 这里添加实际的配置获取逻辑
        config = {
            "WEB_SITE_DOMAIN": "example.com",
            "SSL_OPEN": "1"
        }
        return config.get(key, "")

# AttachmentService类
class AttachmentService:
    def __init__(self):
        self.config_service = ConfigService()

    def get_list_by_search(self, admin_id, attachment_type, category_id, name, createtime, page):
        query = Attachment.query.filter_by(status=1, source="ADMIN", uid=admin_id)

        if category_id:
            query = query.filter_by(category_id=category_id)
        if name:
            query = query.filter(Attachment.name.like(f"%{name}%"))
        if len(createtime) == 2:
            query = query.filter(Attachment.created_at.between(createtime[0], createtime[1]))

        total = query.count()
        attachments = query.order_by(Attachment.id.desc()).limit(8).offset((page - 1) * 8).all()

        for attachment in attachments:
            attachment.url = self.get_url(attachment.url) + f"?timestamp={int(datetime.utcnow().timestamp())}"

        return attachments, total, None

    def insert_get_id(self, attachment):
        db.session.add(attachment)
        db.session.commit()
        return attachment.id, None

    def delete_by_id(self, attachment_id):
        return Attachment.query.filter_by(id=attachment_id).delete()

    def get_info_by_id(self, attachment_id):
        attachment = Attachment.query.filter_by(status=1, id=attachment_id).first()
        return attachment, None

    def update_by_id(self, attachment_id, data):
        return Attachment.query.filter_by(status=1, id=attachment_id).update(data)

    def get_info_by_hash(self, hash_value):
        attachment = Attachment.query.filter_by(status=1, hash=hash_value).first()
        return attachment, None

    def get_url(self, *params):
        id = None
        attachment_type = None

        if len(params) == 1:
            id = params[0]
        elif len(params) == 2:
            attachment_type = params[0]
            id = params[1]

        http = "https://" if self.config_service.get_value("SSL_OPEN") == "1" else "http://"
        web_site_domain = self.config_service.get_value("WEB_SITE_DOMAIN")

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

        attachment = Attachment.query.filter_by(id=id, status=1).first()
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

    def get_file_url(self, id):
        return self.get_url("FILE", id)

    def get_image_url(self, id):
        return self.get_url("IMAGE", id)

    def get_urls(self, id):
        paths = []
        http = "https://" if self.config_service.get_value("SSL_OPEN") == "1" else "http://"
        web_site_domain = self.config_service.get_value("WEB_SITE_DOMAIN")

        if isinstance(id, str):
            if "{" in id:
                try:
                    json_data = json.loads(id)
                    if isinstance(json_data, list):
                        for v in json_data:
                            path = v.get("url", "")
                            if "://" in path:
                                paths.append(v["url"])
                            else:
                                if "./" in path:
                                    path = path.replace("./web/app/", "/", 1)
                                if path:
                                    path = http + web_site_domain + path
                                paths.append(path)
                except json.JSONDecodeError:
                    pass

        return paths

    def get_path(self, id):
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

        attachment = Attachment.query.filter_by(id=id, status=1).first()
        return attachment.path if attachment else ""

    def get_file_path(self, id):
        return self.get_path(id)

    def get_image_path(self, id):
        return self.get_path(id)

    def get_paths(self, id):
        paths = []
        if isinstance(id, str):
            if "{" in id:
                try:
                    json_data = json.loads(id)
                    if isinstance(json_data, list):
                        for v in json_data:
                            paths.append(self.get_path(v["id"]))
                except json.JSONDecodeError:
                    pass

        return paths

    def get_excel_data(self, file_id):
        file = Attachment.query.filter_by(id=file_id, status=1).first()
        if not file:
            return [], ValueError("param error")

        try:
            workbook = openpyxl.load_workbook(file.path)
            sheet = workbook.active
            data = []
            for row in sheet.iter_rows(values_only=True):
                data.append(row)
            return data, None
        except Exception as e:
            return [], e