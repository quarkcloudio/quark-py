from tortoise import fields, models


class Config(models.Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    type = fields.CharField(max_length=20)
    name = fields.CharField(max_length=255)
    sort = fields.IntField(default=0)
    group_name = fields.CharField(max_length=255)
    value = fields.CharField(max_length=2000, null=True)
    remark = fields.CharField(max_length=100, default="", null=False)
    status = fields.IntField(default=1)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True, null=True)

    class Meta:
        table = "configs"

    @staticmethod
    async def seeder():
        seeders = [
            {
                "title": "网站名称",
                "type": "text",
                "name": "WEB_SITE_NAME",
                "group_name": "基本",
                "value": "QuarkCloud",
            },
            {
                "title": "关键字",
                "type": "text",
                "name": "WEB_SITE_KEYWORDS",
                "group_name": "基本",
                "value": "QuarkCloud",
            },
            {
                "title": "描述",
                "type": "textarea",
                "name": "WEB_SITE_DESCRIPTION",
                "group_name": "基本",
                "value": "QuarkCloud",
            },
            {
                "title": "Logo",
                "type": "picture",
                "name": "WEB_SITE_LOGO",
                "group_name": "基本",
                "value": "",
            },
            {
                "title": "统计代码",
                "type": "textarea",
                "name": "WEB_SITE_SCRIPT",
                "group_name": "基本",
                "value": "",
            },
            {
                "title": "网站域名",
                "type": "text",
                "name": "WEB_SITE_DOMAIN",
                "group_name": "基本",
                "value": "",
            },
            {
                "title": "网站版权",
                "type": "text",
                "name": "WEB_SITE_COPYRIGHT",
                "group_name": "基本",
                "value": "© Company 2018",
            },
            {
                "title": "开启SSL",
                "type": "switch",
                "name": "SSL_OPEN",
                "group_name": "基本",
                "value": "0",
            },
            {
                "title": "开启网站",
                "type": "switch",
                "name": "WEB_SITE_OPEN",
                "group_name": "基本",
                "value": "1",
            },
            {
                "title": "KeyID",
                "type": "text",
                "name": "OSS_ACCESS_KEY_ID",
                "group_name": "阿里云存储",
                "value": "",
                "remark": "你的AccessKeyID",
            },
            {
                "title": "KeySecret",
                "type": "text",
                "name": "OSS_ACCESS_KEY_SECRET",
                "group_name": "阿里云存储",
                "value": "",
                "remark": "你的AccessKeySecret",
            },
            {
                "title": "EndPoint",
                "type": "text",
                "name": "OSS_ENDPOINT",
                "group_name": "阿里云存储",
                "value": "",
                "remark": "地域节点",
            },
            {
                "title": "Bucket域名",
                "type": "text",
                "name": "OSS_BUCKET",
                "group_name": "阿里云存储",
                "value": "",
            },
            {
                "title": "自定义域名",
                "type": "text",
                "name": "OSS_MYDOMAIN",
                "group_name": "阿里云存储",
                "value": "",
                "remark": "例如：oss.web.com",
            },
            {
                "title": "开启云存储",
                "type": "switch",
                "name": "OSS_OPEN",
                "group_name": "阿里云存储",
                "value": "0",
            },
        ]

        for data in seeders:
            exists = await Config.filter(name=data["name"]).exists()
            if not exists:
                await Config.create(**data)
