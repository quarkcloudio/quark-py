from flask import request
import json
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
from .resolves_fields import ResolvesFields
from .resolves_actions import ResolvesActions
from .resolves_searches import ResolvesSearches
from .performs_queries import PerformsQueries
from ..service.attachment import AttachmentService
from ..utils.lister import list_to_tree
from ..db import db


@dataclass
class Resource:

    # 页面标题
    title: Any = ""

    # 页面副标题
    sub_title: Any = ""

    # 是否显示返回图标
    back_icon: Any = True

    # 是否启用导出功能
    export: bool = False

    # 导出按钮的文本内容
    export_text: str = "导出"

    # 导出接口的路径
    export_path: str = "/api/admin/<resource>/export"

    # 每页显示的数据条数，默认为 10
    page_size: Optional[int] = 10

    # 可选的每页条数选项
    page_size_options: List[int] = field(default_factory=lambda: [10, 20, 50, 100])

    # 全局数据排序规则
    query_order: str = "created_at desc"

    # 列表页面的排序规则。
    index_query_order: str = ""

    # 导出数据时的排序规则
    export_query_order: str = ""

    # 数据模型对象
    model: Any = field(default=None)

    # 表单组件实例
    form: Form = field(default_factory=Form)

    # 表格组件实例
    table: Table = field(default_factory=Table)

    # 表格搜索组件
    table_search: Search = field(default_factory=Search)

    # 表格列配置组件
    table_column: Column = field(default_factory=Column)

    # 表格工具栏组件
    table_tool_bar: ToolBar = field(default_factory=ToolBar)

    # 表格树形筛选组件
    table_tree_bar: TreeBar = field(default_factory=TreeBar)

    # 表格标题后缀文字
    table_title_suffix: str = "列表"

    # 操作列标题
    table_action_column_title: str = "操作"

    # 操作列宽度，单位为像素
    table_action_column_width: int = 150

    # 表格数据轮询间隔时间（秒）
    table_polling: Any = field(default=None)

    # 是否将表格数据转换为树形结构
    table_list_to_tree: bool = False

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

    def get_form(self):
        """获取表单页 Form 实例"""
        return self.form

    def get_table(self):
        """获取列表页 Table 实例"""
        return self.table

    def get_table_search(self):
        """获取表格搜索组件 Search 实例"""
        return self.table_search

    def get_table_column(self):
        """获取表格列配置 Column 实例"""
        return self.table_column

    def get_table_tool_bar(self):
        """获取表格工具栏 ToolBar 实例"""
        return self.table_tool_bar

    def get_table_tree_bar(self):
        """获取表格树形栏 TreeBar 实例"""
        return self.table_tree_bar

    def get_table_title_suffix(self):
        """获取列表页表格标题后缀"""
        return self.table_title_suffix

    def get_table_action_column_title(self):
        """获取表格操作列标题文字"""
        return self.table_action_column_title

    def get_table_action_column_width(self):
        """获取表格操作列的宽度"""
        return self.table_action_column_width

    def get_table_polling(self):
        """获取表格轮询数据间隔时间"""
        return self.table_polling

    def get_page_size(self):
        """获取分页配置，默认每页数量"""
        return self.page_size

    def get_page_size_options(self):
        """获取每页可选的数据条数配置"""
        return self.page_size_options

    def get_table_list_to_tree(self):
        """获取是否将表格数据转换为树形结构"""
        return self.table_list_to_tree

    def get_query_order(self):
        """获取全局排序规则"""
        return self.query_order

    def get_index_query_order(self):
        """获取列表页排序规则"""
        return self.index_query_order

    def get_export_query_order(self):
        """获取导出数据的排序规则"""
        return self.export_query_order

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
        header = (
            PageHeader().set_title(self.get_title()).set_sub_title(self.get_sub_title())
        )
        if not self.get_back_icon():
            header.set_back_icon(False)
        return PageContainer().set_header(header).set_body(body).to_json()

    def query(self) -> Any:
        """
        全局查询
        """
        return db.session.query(self.get_model())

    def index_query(self) -> Any:
        """
        列表查询
        """
        return self.query()

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
        index_table_actions = (
            ResolvesActions().set_actions(self.actions()).index_table_actions()
        )
        return (
            self.get_table_tool_bar()
            .set_title(self.index_table_title())
            .set_actions(index_table_actions)
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

    def index_table_menu_items(self) -> List[Dict[str, str]]:
        return self.menu_items()

    def index_table_menu(self) -> Dict[str, Any]:
        # 获取菜单项
        items = self.index_table_menu_items()
        if items is None:
            return {}

        # 返回表格菜单
        return {"type": "tab", "items": items}

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
        table_columns = (
            ResolvesFields()
            .set_fields(self.fields())
            .set_table_column(self.get_table_column)
            .set_table_action_column_title(self.get_table_action_column_title())
            .set_table_action_column_width(self.get_table_action_column_width())
            .index_table_columns()
        )
        index_table_alert_actions = (
            ResolvesActions().set_actions(self.actions()).index_table_alert_actions()
        )
        index_searches = (
            ResolvesSearches()
            .set_search(self.get_table_search())
            .set_searches(self.searches())
            .index_searches()
        )

        # 是否开启树形表格
        table_list_to_tree = self.get_table_list_to_tree()
        if table_list_to_tree is not None:
            data = self.index_table_list_to_tree(data)

        # 构建表格配置
        table = (
            table.set_polling(table_polling)
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

            return table.set_pagination(
                current, page_size_val, int(total), 1, page_size_options
            ).set_datasource(items)

    def before_index_showing(self, list_data: List[Dict[str, Any]]) -> List[Any]:
        """
        页面显示前回调
        """
        result = []
        for item in list_data:
            result.append(item)
        return result

    def performs_index_list(self, list_data: List[Any]) -> List[Any]:
        """
        处理列表字段
        """
        result = []
        index_fields = ResolvesFields().set_fields(self.fields()).index_fields()

        for item in list_data:
            fields = {}

            for field in index_fields:
                component = field.component
                name = field.name

                if component == "actionField":
                    items_callback = field.callback
                    if items_callback:
                        action_items = items_callback(item)
                    else:
                        action_items = field.items

                    rendered_actions = []
                    for action in action_items:
                        rendered_actions.append(ResolvesActions().build_action(action))

                    fields[name] = rendered_actions
                else:
                    callback = field.callback
                    if callback:
                        fields[name] = callback(item)
                    else:
                        value = getattr(item, name, None)
                        if value is None:
                            continue

                        # JSON 字符串解析
                        if isinstance(value, str):
                            if value.startswith("[") or value.startswith("{"):
                                try:
                                    value = json.loads(value)
                                except:
                                    pass

                        # 图片字段处理
                        if component in ["imageField", "imagePickerField"]:
                            value = AttachmentService().get_image_url(value)

                        fields[name] = value

            result.append(fields)

        return result

    def index_render(self) -> Any:
        """列表页渲染"""

        # 获取模型类
        query = self.index_query()

        # 获取搜索项
        searches = self.searches()

        filter_str = request.args.get("filter")
        column_filters = {}
        try:
            column_filters = json.loads(filter_str)
        except:
            pass

        # 获取排序规则
        sorter_str = request.args.get("sorter")
        orderings = {}
        try:
            orderings = json.loads(sorter_str)
        except:
            pass

        # 构建查询
        query = (
            PerformsQueries()
            .set_query(query)
            .build_index_query(searches, column_filters)
        )

        # 获取分页配置
        page_size = self.get_page_size()
        page_size_options = self.get_page_size_options()

        if not page_size or not isinstance(page_size, int):
            results = PerformsQueries().apply_index_orderings(query, orderings).all()
            parsed_results = self.performs_index_list(results)
            return parsed_results

        # 分页参数
        data = request.args.get("search")
        search_params = {}
        if data:
            try:
                search_params = json.loads(data)
            except:
                pass

        page = int(search_params.get("current", 1))
        page_size = int(search_params.get("pageSize", page_size))

        # 获取总数
        total = query.count()

        # 获取当前页数据
        results = (
            PerformsQueries()
            .apply_index_orderings(query, orderings)
            .limit(page_size)
            .offset((page - 1) * page_size)
            .all()
        )

        # 解析列表数据
        parsed_items = self.performs_index_list(results)

        # 列表显示前回调
        parsed_items = self.before_index_showing(parsed_items)

        data = {
            "page": page,
            "pageSize": page_size,
            "pageSizeOptions": page_size_options,
            "total": total,
            "items": parsed_items,
        }

        # 组件渲染
        body = self.index_component_render(data)

        # 页面组件渲染
        component = self.page_component_render(body)

        return component

    def editable_render(self) -> Any:
        """行内编辑渲染"""
        pass

    def action_render(self) -> Any:
        """执行行为"""
        pass
