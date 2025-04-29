from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field
from abc import ABC, abstractmethod

# 假设这些模块已经存在或需要实现
from quark import Template, Context, CJSONError
from dal.db import Client as DBClient
from template.admin.component.card import Component as CardComponent
from template.admin.component.descriptions import Component as DescriptionsComponent
from template.admin.component.grid import Row, Col
from template.admin.component.pagecontainer import Component as PageContainerComponent, PageHeader
from template.admin.component.statistic import Component as StatisticComponent

class Dashboarder(ABC):
    @abstractmethod
    def get_title(self) -> str:
        """获取页面标题"""
        pass

    @abstractmethod
    def get_sub_title(self) -> str:
        """获取页面子标题"""
        pass

    @abstractmethod
    def get_back_icon(self) -> bool:
        """获取页面是否携带返回Icon"""
        pass

    @abstractmethod
    def cards(self, ctx: Context) -> List[Any]:
        """获取卡片组件列表"""
        pass

    @abstractmethod
    def page_container_component_render(self, ctx: Context, body: Any) -> Any:
        """页面容器组件渲染"""
        pass

class DashboardTemplate(BaseModel, Template, Dashboarder):
    index_path: str = Field(..., description="路由路径")
    title: str = Field(..., description="页面标题")
    sub_title: str = Field(..., description="页面子标题")
    back_icon: bool = Field(..., description="页面是否携带返回Icon")
    db: Any = Field(None, description="数据库客户端")

    def bootstrap(self) -> 'DashboardTemplate':
        """启动模板，设置路由路径"""
        self.index_path = "/api/admin/dashboard/:resource/index"
        return self

    def load_init_route(self) -> 'DashboardTemplate':
        """加载初始化路由"""
        self.GET(self.index_path, self.render)  # 后台仪表盘路由
        return self

    def load_init_data(self, ctx: Context) -> 'DashboardTemplate':
        """加载初始化数据"""
        # 初始化数据对象
        self.db = DBClient

        # 设置标题
        self.title = "仪表盘"

        # 设置页面是否携带返回Icon
        self.back_icon = False

        return self

    def init(self, ctx: Context) -> 'DashboardTemplate':
        """初始化方法"""
        return self

    def get_title(self) -> str:
        """获取页面标题"""
        return self.title

    def get_sub_title(self) -> str:
        """获取页面子标题"""
        return self.sub_title

    def get_back_icon(self) -> bool:
        """获取页面是否携带返回Icon"""
        return self.back_icon

    def cards(self, ctx: Context) -> List[Any]:
        """获取卡片组件列表"""
        return []

    def page_component_render(self, ctx: Context, body: Any) -> Any:
        """页面组件渲染"""
        template = ctx.template

        # 页面容器组件渲染
        return template.page_container_component_render(ctx, body)

    def page_container_component_render(self, ctx: Context, body: Any) -> Any:
        """页面容器组件渲染"""
        template = ctx.template

        # 获取页面标题
        title = template.get_title()

        # 获取页面子标题
        sub_title = template.get_sub_title()

        # 获取页面是否携带返回Icon
        back_icon = template.get_back_icon()

        # 设置头部
        header = PageHeader().init().set_title(title).set_sub_title(sub_title)

        if not back_icon:
            header.set_back_icon(False)

        # 返回页面容器组件
        return PageContainerComponent().init().set_header(header).set_body(body)

    def render(self, ctx: Context) -> None:
        """组件渲染"""
        template = ctx.template

        # 获取卡片组件列表
        cards = template.cards(ctx)
        if not cards:
            raise CJSONError("请实现Cards内容")

        cols: List[Col] = []
        body: List[Row] = []
        col_num = 0

        for key, v in enumerate(cards):
            # 断言statistic组件类型
            if hasattr(v, 'calculate') and isinstance(v.calculate(), StatisticComponent):
                item = CardComponent().init().set_body(v.calculate())
            elif hasattr(v, 'calculate') and isinstance(v.calculate(), DescriptionsComponent):
                item = CardComponent().init().set_body(v.calculate())
            else:
                item = CardComponent().init()

            # 获取卡片的列数
            col = getattr(v, 'col', 0)
            col_info = Col().init().set_span(col).set_body(item)
            cols.append(col_info)
            col_num += col

            # 如果列数达到24，创建一行
            if col_num % 24 == 0:
                row = Row().init().set_gutter(8).set_body(cols)
                if key != 0:
                    row.set_style({"marginTop": "20px"})
                body.append(row)
                cols = []

        # 如果还有剩余的列，创建一行
        if cols:
            row = Row().init().set_gutter(8).set_body(cols)
            if col_num > 24:
                row.set_style({"marginTop": "20px"})
            body.append(row)

        # 页面组件渲染
        component = template.page_component_render(ctx, body)

        # 返回JSON响应
        ctx.JSON(200, component)