from __future__ import annotations
from dataclasses import dataclass
from typing import Any, List, Dict, Optional, Callable
from abc import ABC, abstractmethod


@dataclass
class FormComponent:
    """表单组件"""
    def init(self):
        return self


@dataclass
class TableComponent:
    """表格组件"""
    def init(self):
        return self


@dataclass
class TableSearch:
    """表格搜索组件"""
    def init(self):
        return self


@dataclass
class TableColumn:
    """表格列组件"""
    def init(self):
        return self


@dataclass
class TableToolBar:
    """表格工具栏组件"""
    def init(self):
        return self


@dataclass
class TableTreeBar:
    """表格树形结构组件"""
    def init(self):
        return self


@dataclass
class PageHeader:
    """页面头部组件"""
    title: str = ""
    sub_title: str = ""
    back_icon: bool = True

    def set_title(self, title: str) -> PageHeader:
        self.title = title
        return self

    def set_sub_title(self, sub_title: str) -> PageHeader:
        self.sub_title = sub_title
        return self

    def set_back_icon(self, enable: bool) -> PageHeader:
        self.back_icon = enable
        return self


@dataclass
class PageContainerComponent:
    """页面容器组件"""
    header: PageHeader = None
    body: Any = None

    def init(self):
        return self

    def set_header(self, header: PageHeader) -> PageContainerComponent:
        self.header = header
        return self

    def set_body(self, body: Any) -> PageContainerComponent:
        self.body = body
        return self


@dataclass
class Template(ABC):
    """
    增删改查模板类
    """

    # 路径配置
    index_path: str = "/api/admin/:resource/index"
    editable_path: str = "/api/admin/:resource/editable"
    action_path: str = "/api/admin/:resource/action/:uriKey"
    action_values_path: str = "/api/admin/:resource/action/:uriKey/values"
    create_path: str = "/api/admin/:resource/create"
    store_path: str = "/api/admin/:resource/store"
    edit_path: str = "/api/admin/:resource/edit"
    edit_values_path: str = "/api/admin/:resource/edit/values"
    save_path: str = "/api/admin/:resource/save"
    import_path: str = "/api/admin/:resource/import"
    export_path: str = "/api/admin/:resource/export"
    detail_path: str = "/api/admin/:resource/detail"
    detail_values_path: str = "/api/admin/:resource/detail/values"
    import_template_path: str = "/api/admin/:resource/import/template"
    form_path: str = "/api/admin/:resource/form"
    content_path: str = ""

    # 页面标题与子标题
    title: str = "默认标题"
    sub_title: str = "默认副标题"
    back_icon: bool = True

    # 组件实例
    form: FormComponent = FormComponent()
    table: TableComponent = TableComponent()
    table_search: TableSearch = TableSearch()
    table_column: TableColumn = TableColumn()
    table_tool_bar: TableToolBar = TableToolBar()
    table_tree_bar: TableTreeBar = TableTreeBar()

    # 表格配置
    table_title_suffix: str = "列表"
    table_action_column_title: str = "操作"
    table_action_column_width: int = 150
    table_polling: int = 0  # 轮询间隔（秒）
    table_list_to_tree: Optional[Dict[str, Any]] = None  # 树状结构设置
    export: bool = False
    export_text: str = "导出"
    page_size: Any = 20
    page_size_options: List[int] = (10, 20, 50, 100)
    query_order: str = ""
    index_query_order: str = ""
    export_query_order: str = ""

    model: Optional[Any] = None  # 模型实例

    def bootstrap(self) -> Template:
        """初始化路径"""
        return self

    def load_init_route(self) -> Template:
        """加载初始路由"""
        # 示例占位符
        self.GET(self.index_path, self.index_render)
        self.GET(self.editable_path, self.editable_render)
        self.ANY(self.action_path, self.action_render)
        return self

    def GET(self, path: str, handler: Callable):
        print(f"GET route registered: {path}")

    def ANY(self, path: str, handler: Callable):
        print(f"ANY route registered: {path}")

    def index_render(self, ctx: Any) -> Any:
        """列表页渲染"""
        pass

    def editable_render(self, ctx: Any) -> Any:
        """行内编辑渲染"""
        pass

    def action_render(self, ctx: Any) -> Any:
        """执行行为"""
        pass

    @abstractmethod
    def fields(self, ctx: Any) -> List[Dict]:
        """字段定义"""
        return []

    @abstractmethod
    def searches(self, ctx: Any) -> List[Dict]:
        """搜索项定义"""
        return []

    @abstractmethod
    def actions(self, ctx: Any) -> List[Dict]:
        """行为定义"""
        return []

    @abstractmethod
    def menu_items(self, ctx: Any) -> List[Dict[str, str]]:
        """菜单项定义"""
        return []

    def get_model(self) -> Any:
        """获取模型实例"""
        return self.model

    def get_title(self) -> str:
        """获取页面标题"""
        return self.title

    def get_sub_title(self) -> str:
        """获取页面副标题"""
        return self.sub_title

    def get_back_icon(self) -> bool:
        """是否显示返回图标"""
        return self.back_icon

    def get_export(self) -> bool:
        """是否允许导出"""
        return self.export

    def get_export_text(self) -> str:
        """获取导出按钮文本"""
        return self.export_text

    def before_exporting(self, ctx: Any, data: List[Dict]) -> List[Any]:
        """导出前处理"""
        return [item for item in data]

    def after_exporting(self, ctx: Any, result: Any) -> Any:
        """导出后处理"""
        return result

    def before_importing(self, ctx: Any, data: List[List[Any]]) -> List[List[Any]]:
        """导入前处理"""
        return data

    def before_editable(self, ctx: Any, id: Any, field: str, value: Any) -> Optional[str]:
        """行内编辑前处理"""
        return None

    def after_editable(self, ctx: Any, id: Any, field: str, value: Any) -> Optional[str]:
        """行内编辑后处理"""
        return None

    def page_component_render(self, ctx: Any, body: Any) -> Any:
        """页面组件渲染"""
        return self.page_container_component_render(ctx, body)

    def page_container_component_render(self, ctx: Any, body: Any) -> PageContainerComponent:
        """页面容器组件渲染"""
        header = PageHeader().set_title(self.get_title()).set_sub_title(self.get_sub_title())
        if not self.get_back_icon():
            header.set_back_icon(False)
        return PageContainerComponent().set_header(header).set_body(body)