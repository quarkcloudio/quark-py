from typing import Any, Dict, List

from quark import Request

from ..utils import list_to_tree
from .resolves_actions import ResolvesActions
from .resolves_fields import ResolvesFields
from .resolves_searches import ResolvesSearches


class ResourceIndex:
    """资源：增删改查"""

    async def index_table_list_to_tree(
        self, request: Request, list_data: List[Any]
    ) -> List[Any]:
        """
        列表页数据转换成树结构
        """
        data = request.query_params
        if isinstance(data.get("search"), dict) and data["search"]:
            return list_data

        pk_name = "id"
        pid_name = "pid"
        children_name = "children"
        root_id = 0

        table_list_to_tree = self.table_list_to_tree
        if isinstance(table_list_to_tree, bool):
            if not table_list_to_tree:
                return list_data
        elif isinstance(table_list_to_tree, dict):
            pk_name = table_list_to_tree.get("pkName", "id")
            pid_name = table_list_to_tree.get("pidName", "pid")
            children_name = table_list_to_tree.get("childrenName", "children")
            root_id = table_list_to_tree.get("rootId", 0)

        tree = list_to_tree(list_data, pk_name, pid_name, children_name, root_id)
        return tree

    async def index_table_extra_render(self, request: Request) -> Any:
        """
        列表页表格主体
        """
        return None

    async def index_table_tool_bar(self, request: Request) -> Any:
        """
        列表页工具栏组件
        """
        actions = await self.actions(request)
        index_table_actions = await ResolvesActions(
            request=request, actions=actions
        ).index_table_actions()
        index_table_title = await self.index_table_title(request)
        index_table_menu = await self.index_table_menu(request)
        return (
            self.table_tool_bar.set_title(index_table_title)
            .set_actions(index_table_actions)
            .set_menu(index_table_menu)
        )

    async def index_table_tree_bar(self, request: Request) -> Any:
        """
        列表页树形结构组件
        """
        return self.table_tree_bar

    async def index_table_title(self, request: Request) -> str:
        """
        获取列表标题
        """
        return self.title + self.table_title_suffix

    async def index_table_menu_items(self, request: Request) -> List[Dict[str, str]]:
        return await self.menu_items(request)

    async def index_table_menu(self, request: Request) -> Dict[str, Any]:
        # 获取菜单项
        items = await self.index_table_menu_items(request)
        if items is None:
            return {}

        # 返回表格菜单
        return {"type": "tab", "items": items}

    async def index_component_render(self, request: Request, data: Any) -> Any:
        """
        列表页组件渲染主逻辑
        """
        table_title = await self.index_table_title(request)
        table_extra_render = await self.index_table_extra_render(request)
        table_tool_bar = await self.index_table_tool_bar(request)
        table_tree_bar = await self.index_table_tree_bar(request)
        fields = await self.fields(request)
        actions = await self.actions(request)
        searches = await self.searches(request)
        index_table_row_actions = await ResolvesActions(
            request=request, actions=actions
        ).index_table_row_actions()
        table_columns = ResolvesFields(
            request=request,
            fields=fields,
            table_column=self.table_column,
            table_row_actions=index_table_row_actions,
            table_action_column_title=self.table_action_column_title,
            table_action_column_width=self.table_action_column_width,
        ).index_table_columns()
        index_table_alert_actions = await ResolvesActions(
            request=request, actions=actions
        ).index_table_alert_actions()
        index_searches = ResolvesSearches(
            request=request, search=self.table_search, searches=searches
        ).index_searches()

        # 是否开启树形表格
        if self.table_list_to_tree is not None:
            data = await self.index_table_list_to_tree(request, data)

        # 构建表格配置
        table = (
            self.table.set_polling(self.table_polling)
            .set_title(table_title)
            .set_table_extra_render(table_extra_render)
            .set_tool_bar(table_tool_bar)
            .set_tree_bar(table_tree_bar)
            .set_columns(table_columns)
            .set_batch_actions(index_table_alert_actions)
            .set_searches(index_searches)
        )

        page_size = self.page_size
        if page_size is None:
            return table.set_datasource(data)

        # 如果不是整数分页配置，直接返回数据
        if not isinstance(page_size, int) or isinstance(page_size, bool):
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

    async def before_index_showing(
        self, request: Request, list: List[Dict[str, Any]]
    ) -> List[Any]:
        """
        页面显示前回调
        """
        return list
