from flask import request
from dataclasses import dataclass, field
from typing import Any, List, Dict, Optional
from ..component.form.form import Form
from ..component.table.table import Table
from ..component.table.search import Search
from ..component.table.column import Column
from ..component.table.tool_bar import ToolBar
from ..component.table.tree_bar import TreeBar
from ..component.pagecontainer.pagecontainer import PageContainer
from ..component.pagecontainer.pageheader import PageHeader
from ..utils.lister import list_to_tree
from .resolves_fields import ResolvesFields

@dataclass
class Resource:
    title: str = "页面标题"  # 页面标题
    sub_title: str = "页面子标题"  # 页面子标题
    back_icon: bool = True  # 页面是否携带返回Icon
    table_polling: int = 0  # 表格是否轮询数据
    export: bool = False  # 是否具有导出功能
    export_text: str = "导出"  # 导出按钮文字内容
    export_path: str = "/api/admin/<resource>/export"  # 导出接口路径
    page_size: Optional[int] = 10  # 分页配置，默认每页10条
    page_size_options: List[int] = field(default_factory=lambda: [10, 20, 50, 100])  # 每页显示条数
    query_order: str = "created_at desc"  # 全局排序规则
    model: Optional[Any] = None  # 挂载模型
    form: Form = field(default_factory=Form)
    table: Table = field(default_factory=Table)
    table_search: Search = field(default_factory=Search)
    table_column: Column = field(default_factory=Column)
    table_tool_bar: ToolBar = field(default_factory=ToolBar)
    table_tree_bar: TreeBar = field(default_factory=TreeBar)
    table_title_suffix: str = "列表"
    table_action_column_title: str = "操作"
    table_action_column_width: int = 150
    table_polling: int = 0  # 轮询间隔（秒）
    table_list_to_tree: bool = False  # 列表数据是否转换为树形结构
    index_query_order: str = ""  # 列表页排序规则
    export_query_order: str = ""  # 导出数据排序规则

    # 获取Model结构体
    def get_model(self):
        return self.model

    # 获取标题
    def get_title(self):
        return self.title

    # 获取子标题
    def get_sub_title(self):
        return self.sub_title

    # 页面是否携带返回Icon
    def get_back_icon(self):
        return self.back_icon

    # 获取表单页Form实例
    def get_form(self):
        return self.form

    # 获取列表页Table实例
    def get_table(self):
        return self.table

    # 获取Search实例
    def get_table_search(self):
        return self.table_search

    # 获取Column实例
    def get_table_column(self):
        return self.table_column

    # 获取工具栏实例
    def get_table_tool_bar(self):
        return self.table_tool_bar

    # 获取树形实例
    def get_table_tree_bar(self):
        return self.table_tree_bar

    # 列表页表格标题后缀
    def get_table_title_suffix(self):
        return self.table_title_suffix

    # 列表页表格行为列显示文字
    def get_table_action_column_title(self):
        return self.table_action_column_title

    # 列表页表格行为列的宽度
    def get_table_action_column_width(self):
        return self.table_action_column_width

    # 获取轮询数据
    def get_table_polling(self):
        return self.table_polling

    # 获取分页配置
    def get_page_size(self):
        return self.page_size

    # 指定每页可以显示多少条
    def get_page_size_options(self):
        return self.page_size_options

    # 列表页列表数据转换为树形结构
    def get_table_list_to_tree(self):
        return self.table_list_to_tree

    # 获取全局排序规则
    def get_query_order(self):
        return self.query_order

    # 获取列表页排序规则
    def get_index_query_order(self):
        return self.index_query_order

    # 获取导出数据排序规则
    def get_export_query_order(self):
        return self.export_query_order

    # 获取是否具有导出功能
    def get_export(self):
        return self.export

    # 获取导出按钮文字内容
    def get_export_text(self):
        return self.export_text

    def fields(self) -> List[Dict]:
        """字段定义"""
        return []

    def searches(self) -> List[Dict]:
        """搜索项定义"""
        return []

    def actions(self) -> List[Dict]:
        """行为定义"""
        return []

    def menu_items(self) -> List[Dict[str, str]]:
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

    def before_exporting(self, data: List[Dict]) -> List[Any]:
        """导出前处理"""
        return [item for item in data]

    def after_exporting(self, result: Any) -> Any:
        """导出后处理"""
        return result

    def before_importing(self, data: List[List[Any]]) -> List[List[Any]]:
        """导入前处理"""
        return data

    def before_editable(self, id: Any, field: str, value: Any) -> Optional[str]:
        """行内编辑前处理"""
        return None

    def after_editable(self, id: Any, field: str, value: Any) -> Optional[str]:
        """行内编辑后处理"""
        return None

    def page_component_render(self, body: Any) -> Any:
        """页面组件渲染"""
        return self.page_container_component_render(body)

    def page_container_component_render(self, body: Any) -> PageContainer:
        """页面容器组件渲染"""
        header = PageHeader().set_title(self.get_title()).set_sub_title(self.get_sub_title())
        if not self.get_back_icon():
            header.set_back_icon(False)
        return PageContainer().set_header(header).set_body(body)
    
    def index_table_list_to_tree(self, list_data: List[Any]) -> List[Any]:
        """
        列表页数据转换成树结构
        """
        data = request.args.to_dict()
        if isinstance(data.get("search"), dict) and data["search"]:
            return list_data

        pk_name = "id"
        pid_name = "pid"
        children_name = "children"
        root_id = 0

        table_list_to_tree = self.get_table_list_to_tree()

        if isinstance(table_list_to_tree, bool):
            if not table_list_to_tree:
                return list_data
        elif isinstance(table_list_to_tree, dict):
            pk_name = table_list_to_tree.get("pkName", "id")
            pid_name = table_list_to_tree.get("pidName", "pid")
            children_name = table_list_to_tree.get("childrenName", "children")
            root_id = table_list_to_tree.get("rootId", 0)

        # 假设 lister.ListToTree 是一个可用函数
        tree, _ = list_to_tree(list_data, pk_name, pid_name, children_name, root_id)
        return tree

    def index_table_extra_render(self) -> Any:
        """
        列表页表格主体
        """
        return None

    def index_table_tool_bar(self) -> Any:
        """
        列表页工具栏组件
        """
        return (
            self.get_table_tool_bar()
            .set_title(self.index_table_title())
            .set_actions(self.index_table_actions())
            .set_menu(self.index_table_menu())
        )

    def index_table_tree_bar(self) -> Any:
        """
        列表页树形结构组件
        """
        return self.get_table_tree_bar()

    def index_table_title(self) -> str:
        """
        获取列表标题
        """
        return f"{self.get_title()}{self.get_table_title_suffix()}"

    def index_table_menu_items(self, ctx) -> List[Dict[str, str]]:
        # 假设 ctx.template 是一个 Resourcer 类型的实例，返回对应的 MenuItems
        template = ctx.template  # 这里假设ctx对象有template属性
        return template.menu_items(ctx)
    
    def index_table_menu(self, ctx) -> Dict[str, Any]:
        # 获取菜单项
        items = self.index_table_menu_items(ctx)
        if items is None:
            return {}
        
        # 返回表格菜单
        return {
            "type": "tab",
            "items": items
        }

    def index_component_render(self, data: Any) -> Any:
        """
        列表页组件渲染主逻辑
        """
        table = self.get_table()
        table_title = self.index_table_title()
        table_polling = self.get_table_polling()
        table_extra_render = self.index_table_extra_render()
        table_tool_bar = self.index_table_tool_bar()
        table_tree_bar = self.index_table_tree_bar()
        get_fields = self.fields()
        table_columns = ResolvesFields().set_fields(get_fields).index_table_columns()
        index_table_alert_actions = self.index_table_alert_actions()
        index_searches = self.index_searches()

        # 是否开启树形表格
        table_list_to_tree = self.get_table_list_to_tree()
        if table_list_to_tree is not None:
            data = self.index_table_list_to_tree(data)

        # 构建表格配置
        table = (
            table.set_polling(int(table_polling))
            .set_title(table_title)
            .set_table_extra_render(table_extra_render)
            .set_tool_bar(table_tool_bar)
            .set_tree_bar(table_tree_bar)
            .set_columns(table_columns)
            .set_batch_actions(index_table_alert_actions)
            .set_searches(index_searches)
        )

        page_size = self.get_page_size()
        if page_size is None:
            return table.set_datasource(data)

        # 如果不是整数分页配置，直接返回数据
        if not isinstance(page_size, int):
            return table.set_datasource(data)
        else:
            current = data.get("page")
            page_size_val = data.get("pageSize")
            page_size_options = data.get("pageSizeOptions")
            total = data.get("total")
            items = data.get("items")

            return (
                table.set_pagination(current, page_size_val, int(total), 1, page_size_options)
                .set_datasource(items)
            )

    def before_index_showing(
        self, list_data: List[Dict[str, Any]]
    ) -> List[Any]:
        """
        页面显示前回调
        """
        result = []
        for item in list_data:
            result.append(item)
        return result

    def index_render(self) -> Any:
        """列表页渲染"""
        pass
    
    def editable_render(self) -> Any:
        """行内编辑渲染"""
        pass

    def action_render(self) -> Any:
        """执行行为"""
        pass