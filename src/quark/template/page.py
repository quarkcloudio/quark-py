from pydantic import BaseModel


class Page(BaseModel):

    # 页面标题
    title: str = ""
