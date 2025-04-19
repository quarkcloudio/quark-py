from dataclasses import dataclass
from quark.template.login import Login

@dataclass
class Index(Login):
    api: str = "/api/admin/login/index/handle"
    redirect: str = "/layout/index?api=/api/admin/dashboard/index/index"
    title: str = "QuarkPy"
    sub_title: str = "信息丰富的世界里，唯一稀缺的就是人类的注意力"