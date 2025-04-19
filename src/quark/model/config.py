from sqlalchemy import Column, Integer, String, DateTime, func
from ..dal import db

class Config(db.Model):
    __tablename__ = 'configs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    type = Column(String(20), nullable=False)
    name = Column(String(255), nullable=False)
    sort = Column(Integer, default=0)
    group_name = Column(String(255), nullable=False)
    value = Column(String(2000))
    remark = Column(String(100), nullable=False, default="")
    status = Column(Integer, nullable=False, default=1)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    @staticmethod
    def seeder():
        session = db.Session()
        try:
            seeders = [
                Config(title="网站名称", type="text", name="WEB_SITE_NAME", sort=0, group_name="基本", value="QuarkCloud", remark="", status=1),
                Config(title="关键字", type="text", name="WEB_SITE_KEYWORDS", sort=0, group_name="基本", value="QuarkCloud", remark="", status=1),
                Config(title="描述", type="textarea", name="WEB_SITE_DESCRIPTION", sort=0, group_name="基本", value="QuarkCloud", remark="", status=1),
                Config(title="Logo", type="picture", name="WEB_SITE_LOGO", sort=0, group_name="基本", value="", remark="", status=1),
                Config(title="统计代码", type="textarea", name="WEB_SITE_SCRIPT", sort=0, group_name="基本", value="", remark="", status=1),
                Config(title="网站域名", type="text", name="WEB_SITE_DOMAIN", sort=0, group_name="基本", value="", remark="", status=1),
                Config(title="网站版权", type="text", name="WEB_SITE_COPYRIGHT", sort=0, group_name="基本", value="© Company 2018", remark="", status=1),
                Config(title="开启SSL", type="switch", name="SSL_OPEN", sort=0, group_name="基本", value="0", remark="", status=1),
                Config(title="开启网站", type="switch", name="WEB_SITE_OPEN", sort=0, group_name="基本", value="1", remark="", status=1),
                Config(title="KeyID", type="text", name="OSS_ACCESS_KEY_ID", sort=0, group_name="阿里云存储", value="", remark="你的AccessKeyID", status=1),
                Config(title="KeySecret", type="text", name="OSS_ACCESS_KEY_SECRET", sort=0, group_name="阿里云存储", value="", remark="你的AccessKeySecret", status=1),
                Config(title="EndPoint", type="text", name="OSS_ENDPOINT", sort=0, group_name="阿里云存储", value="", remark="地域节点", status=1),
                Config(title="Bucket域名", type="text", name="OSS_BUCKET", sort=0, group_name="阿里云存储", value="", remark="", status=1),
                Config(title="自定义域名", type="text", name="OSS_MYDOMAIN", sort=0, group_name="阿里云存储", value="", remark="例如：oss.web.com", status=1),
                Config(title="开启云存储", type="switch", name="OSS_OPEN", sort=0, group_name="阿里云存储", value="0", remark="", status=1),
            ]

            for cfg in seeders:
                exists = session.query(Config).filter_by(name=cfg.name).first()
                if not exists:
                    session.add(cfg)
            session.commit()
        except Exception as e:
            session.rollback()
            raise
        finally:
            session.close()
