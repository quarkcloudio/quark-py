from typing import Any, Dict, List, Optional

from pydantic import Field, model_validator

from ..component import Component


class Expandable(Component):
    children_column_name: Optional[str] = None
    column_title: Optional[Any] = None
    column_width: Optional[Any] = None
    default_expand_all_rows: bool = None
    default_expanded_row_keys: List[Any] = None
    expanded_row_class_name: Optional[str] = None
    expanded_row_keys: List[Any] = None
    expand_icon: Optional[Any] = None
    expand_row_by_click: bool = None
    fixed: Optional[Any] = None
    indent_size: int = None
    row_expandable: bool = None
    show_expand_column: bool = None


class Table(Component):
    component: str = "table"
    row_key: str = "id"
    api: str = None
    api_type: str = "GET"
    table_layout: str = None
    header_title: str = None
    columns: Any = None
    row_selection: Any = Field(default_factory=list)
    options: Dict[str, bool] = Field(
        default_factory=lambda: {"fullScreen": True, "reload": True, "setting": True}
    )
    search: Any = None
    batch_actions: Any = None
    date_formatter: str = "string"
    column_empty_text: str = "-"
    tool_bar: Any = None
    tree_bar: Any = None
    table_extra_render: Any = None
    expandable: Optional[Expandable] = None
    scroll: Any = None
    striped: bool = False
    datasource: Any = None
    pagination: Any = None
    polling: int = None

    @model_validator(mode="after")
    def init(self):
        self.set_key("table", False)
        return self

    # 设置方法（链式调用）
    def set_style(self, style: dict):
        self.style = style
        return self

    def set_row_key(self, key: str):
        self.row_key = key
        return self

    def set_api(self, api: str):
        self.api = api
        return self

    def set_api_type(self, api_type: str):
        self.api_type = api_type
        return self

    def set_table_layout(self, layout: str):
        self.table_layout = layout
        return self

    def set_title(self, title: str):
        self.header_title = title
        return self

    def set_header_title(self, title: str):
        self.header_title = title
        return self

    def set_searches(self, search: Any):
        self.search = search
        return self

    def set_columns(self, columns: Any):
        self.columns = columns
        return self

    def set_row_selection(self, selection: Any):
        self.row_selection = selection
        return self

    def set_options(self, options: Dict[str, bool]):
        self.options = options
        return self

    def set_date_formatter(self, formatter: str):
        self.date_formatter = formatter
        return self

    def set_column_empty_text(self, text: str):
        self.column_empty_text = text
        return self

    def set_tool_bar(self, toolbar: Any):
        self.tool_bar = toolbar
        return self

    def set_tree_bar(self, treebar: Any):
        self.tree_bar = treebar
        return self

    def set_batch_actions(self, actions: Any):
        self.batch_actions = actions
        return self

    def set_table_extra_render(self, render: Any):
        self.table_extra_render = render
        return self

    def set_expandable(self, expandable: Expandable):
        self.expandable = expandable
        return self

    def set_scroll(self, scroll: Any):
        self.scroll = scroll
        return self

    def set_striped(self, striped: bool):
        self.striped = striped
        return self

    def set_datasource(self, source: Any):
        self.datasource = source
        return self

    def set_pagination(
        self,
        current: int,
        page_size: int,
        total: int,
        default_current: int,
        page_size_options: list,
    ):
        self.pagination = {
            "current": current,
            "pageSize": page_size,
            "total": total,
            "defaultCurrent": default_current,
            "pageSizeOptions": page_size_options,
        }
        return self

    def set_polling(self, polling: int):
        self.polling = polling
        return self
