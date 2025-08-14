from typing import Any, List, Optional

from fastapi import Request
from pydantic import BaseModel, Field

from ..component.card.card import Card
from ..component.grid.col import Col
from ..component.grid.row import Row
from ..component.pagecontainer.pagecontainer import PageContainer
from ..component.pagecontainer.pageheader import PageHeader


class Dashboard(BaseModel):
    """仪表盘"""

    # 页面标题
    title: str = Field(default="")

    # 页面子标题
    sub_title: Optional[str] = Field(default="")

    # 页面是否携带返回Icon
    back_icon: bool = Field(default=False)

    async def init(self, request: Request):
        """初始化"""
        return self

    async def cards(self, request: Request) -> List[Any]:
        """获取卡片组件列表"""
        return []

    async def page_component_render(self, request: Request, body: Any) -> Any:
        """页面组件渲染"""
        return await self.page_container_component_render(request, body)

    async def page_container_component_render(self, request: Request, body: Any) -> Any:
        """页面容器组件渲染"""

        # 设置头部
        header = PageHeader().set_title(self.title).set_sub_title(self.sub_title)
        if not self.back_icon:
            header.set_back_icon(False)

        # 返回页面容器组件
        return PageContainer().set_header(header).set_body(body)

    async def render(self, request: Request) -> Any:
        """组件渲染"""
        # 获取卡片组件列表
        cards = await self.cards(request)
        if not cards:
            return "请实现Cards内容"

        cols: List[Col] = []
        body: List[Row] = []
        col_num = 0

        for key, v in enumerate(cards):
            # 断言 statistic 组件类型
            if hasattr(v, "calculate"):
                value = await v.calculate()
                item = Card().set_body(value)
            else:
                item = Card()

            # 获取卡片的列数
            col_span = getattr(v, "col", 0)
            col_info = Col().set_span(col_span).set_body(item)
            cols.append(col_info)
            col_num += col_span

            # 如果列数达到 24，创建一行
            if col_num % 24 == 0:
                row = Row().set_gutter(8).set_body(cols)
                if key != 0:
                    row.set_style({"marginTop": "20px"})
                body.append(row)
                cols = []

        # 如果还有剩余的列，创建一行
        if cols:
            row = Row().set_gutter(8).set_body(cols)
            if col_num > 24:
                row.set_style({"marginTop": "20px"})
            body.append(row)

        return await self.page_component_render(request, body)
