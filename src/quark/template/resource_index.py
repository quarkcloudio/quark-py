from typing import Any, List, Dict, Optional, Union
from dataclasses import dataclass


@dataclass
class Context:
    """
    模拟 quark.Context 上下文对象
    """
    query_params: Dict[str, Any] = None
    template: Any = None

    def all_querys(self) -> Dict[str, Any]:
        return self.query_params or {}

    def get_template(self):
        return self.template


class Resourcer:
    """
    模拟 types.Resourcer 接口，提供通用方法定义
    """

    def get_table_list_to_tree(self) -> Optional[Union[bool, Dict]]:
        pass

    def get_table_tool_bar(self, ctx: Context):
        pass

    def get_table_tree_bar(self, ctx: Context):
        pass

    def get_title(self) -> str:
        pass

    def get_table_title_suffix(self) -> str:
        pass

    def get_table_polling(self) -> int:
        pass

    def index_table_extra_render(self, ctx: Context):
        pass

    def index_table_actions(self, ctx: Context):
        pass

    def index_table_menu(self, ctx: Context):
        pass

    def index_table_columns(self, ctx: Context):
        pass

    def index_table_alert_actions(self, ctx: Context):
        pass

    def index_searches(self, ctx: Context):
        pass

    def get_page_size(self) -> Any:
        pass

    def get_table(self):
        pass


class Template:
    """
    对应 Go 中的 Template 结构体，包含列表页渲染相关的方法
    """

    def __init__(self):
        pass

    def index_table_list_to_tree(self, ctx: Context, list_data: List[Any]) -> List[Any]:
        """
        列表页数据转换成树结构
        """
        data = ctx.all_querys()
        if isinstance(data.get("search"), dict) and data["search"]:
            return list_data

        pk_name = "id"
        pid_name = "pid"
        children_name = "children"
        root_id = 0

        resourcer: Resourcer = ctx.get_template()
        table_list_to_tree = resourcer.get_table_list_to_tree()

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

    def index_table_extra_render(self, ctx: Context) -> Any:
        """
        列表页表格主体
        """
        return None

    def index_table_tool_bar(self, ctx: Context) -> Any:
        """
        列表页工具栏组件
        """
        resourcer: Resourcer = ctx.get_template()
        return (
            resourcer.get_table_tool_bar(ctx)
            .set_title(self.index_table_title(ctx))
            .set_actions(self.index_table_actions(ctx))
            .set_menu(self.index_table_menu(ctx))
        )

    def index_table_tree_bar(self, ctx: Context) -> Any:
        """
        列表页树形结构组件
        """
        resourcer: Resourcer = ctx.get_template()
        return resourcer.get_table_tree_bar(ctx)

    def index_table_title(self, ctx: Context) -> str:
        """
        获取列表标题
        """
        resourcer: Resourcer = ctx.get_template()
        return f"{resourcer.get_title()}{resourcer.get_table_title_suffix()}"

    def index_component_render(self, ctx: Context, data: Any) -> Any:
        """
        列表页组件渲染主逻辑
        """
        resourcer: Resourcer = ctx.get_template()

        table = resourcer.get_table()
        table_title = self.index_table_title(ctx)
        table_polling = resourcer.get_table_polling()
        table_extra_render = resourcer.index_table_extra_render(ctx)
        table_tool_bar = self.index_table_tool_bar(ctx)
        table_tree_bar = self.index_table_tree_bar(ctx)
        table_columns = self.index_table_columns(ctx)
        index_table_alert_actions = self.index_table_alert_actions(ctx)
        index_searches = self.index_searches(ctx)

        # 是否开启树形表格
        table_list_to_tree = resourcer.get_table_list_to_tree()
        if table_list_to_tree is not None:
            data = self.index_table_list_to_tree(ctx, data)

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

        page_size = resourcer.get_page_size()
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
        self, ctx: Context, list_data: List[Dict[str, Any]]
    ) -> List[Any]:
        """
        页面显示前回调
        """
        result = []
        for item in list_data:
            result.append(item)
        return result


# 假设的辅助函数，模拟 lister.ListToTree
def list_to_tree(
    items: List[Any], pk_name: str, pid_name: str, children_name: str, root_id: int
) -> (List[Any], Optional[str]):
    """
    将列表数据转为树形结构
    """
    # 这里你可以实现实际的树形构建逻辑
    return [], None