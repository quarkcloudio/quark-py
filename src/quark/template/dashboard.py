from typing import Any, List
from dataclasses import dataclass, field
from ..component.card.card import Component as CardComponent
from ..component.grid.row import Row
from ..component.grid.col import Col
from ..component.pagecontainer.pagecontainer import Component as PageContainerComponent
from ..component.pagecontainer.pageheader import PageHeader

@dataclass
class Dashboard:
    title: str = "仪表盘"
    sub_title: str = None
    back_icon: bool = False

    def get_title(self) -> str:
        """获取页面标题"""
        return self.title

    def get_sub_title(self) -> str:
        """获取页面子标题"""
        return self.sub_title

    def get_back_icon(self) -> bool:
        """获取页面是否携带返回Icon"""
        return self.back_icon

    def cards(self) -> List[Any]:
        """获取卡片组件列表"""
        return []

    def page_component_render(self, body: Any) -> Any:
        """页面组件渲染"""

        # 页面容器组件渲染
        return self.page_container_component_render(body)

    def page_container_component_render(self, body: Any) -> Any:
        """页面容器组件渲染"""

        # 获取页面标题
        title = self.get_title()

        # 获取页面子标题
        sub_title = self.get_sub_title()

        # 获取页面是否携带返回Icon
        back_icon = self.get_back_icon()

        # 设置头部
        header = PageHeader().set_title(title).set_sub_title(sub_title)

        if not back_icon:
            header.set_back_icon(False)

        # 返回页面容器组件
        return PageContainerComponent().set_header(header).set_body(body).to_json()

    def render(self) -> None:
        """组件渲染"""

        # 获取卡片组件列表
        cards = self.cards()
        if not cards:
            return "请实现Cards内容"

        cols: List[Col] = []
        body: List[Row] = []
        col_num = 0

        for key, v in enumerate(cards):
            # 断言statistic组件类型
            if hasattr(v, 'calculate'):
                item = CardComponent().set_body(v.calculate())
            else:
                item = CardComponent()

            # 获取卡片的列数
            col = getattr(v, 'col', 0)
            col_info = Col().set_span(col).set_body(item)
            cols.append(col_info)
            col_num += col

            # 如果列数达到24，创建一行
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

        # 页面组件渲染
        component = self.page_component_render(body)

        # 返回JSON响应
        return component