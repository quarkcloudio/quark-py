from dataclasses import dataclass, field
from typing import Any, List, Optional

@dataclass
class Expandable:
    ChildrenColumnName: Optional[str] = None
    ColumnTitle: Optional[Any] = None
    ColumnWidth: Optional[Any] = None
    DefaultExpandAllRows: bool = False
    DefaultExpandedRowKeys: List[Any] = field(default_factory=list)
    ExpandedRowClassName: Optional[str] = None
    ExpandedRowKeys: List[Any] = field(default_factory=list)
    ExpandIcon: Optional[Any] = None
    ExpandRowByClick: bool = False
    Fixed: Optional[Any] = None
    IndentSize: int = 0
    RowExpandable: bool = False
    ShowExpandColumn: bool = False


@dataclass
class Component(Element):
    RowKey: str = "id"
    Api: str = ""
    ApiType: str = "GET"
    TableLayout: str = ""
    HeaderTitle: str = ""
    Columns: Any = None
    RowSelection: Any = field(default_factory=list)
    Options: Dict[str, bool] = field(default_factory=lambda: {
        "fullScreen": True, "reload": True, "setting": True
    })
    Search: Any = None
    BatchActions: Any = None
    DateFormatter: str = "string"
    ColumnEmptyText: str = "-"
    ToolBar: Any = None
    TreeBar: Any = None
    TableExtraRender: Any = None
    Expandable: Optional[Expandable] = None
    Scroll: Any = None
    Striped: bool = False
    Datasource: Any = None
    Pagination: Any = None
    Polling: int = 0

    def __post_init__(self):
        self.Component = "table"
        self.set_key("table", False)

    def set_style(self, style: dict):
        self.Style = style
        return self

    def set_row_key(self, key: str):
        self.RowKey = key
        return self

    def set_api(self, api: str):
        self.Api = api
        return self

    def set_api_type(self, api_type: str):
        self.ApiType = api_type
        return self

    def set_table_layout(self, layout: str):
        self.TableLayout = layout
        return self

    def set_title(self, title: str):
        self.HeaderTitle = title
        return self

    def set_columns(self, columns: Any):
        self.Columns = columns
        return self

    def set_row_selection(self, selection: Any):
        self.RowSelection = selection
        return self

    def set_options(self, options: Dict[str, bool]):
        self.Options = options
        return self

    def set_date_formatter(self, formatter: str):
        self.DateFormatter = formatter
        return self

    def set_column_empty_text(self, text: str):
        self.ColumnEmptyText = text
        return self

    def set_toolbar(self, toolbar: Any):
        self.ToolBar = toolbar
        return self

    def set_treebar(self, treebar: Any):
        self.TreeBar = treebar
        return self

    def set_batch_actions(self, actions: Any):
        self.BatchActions = actions
        return self

    def set_table_extra_render(self, render: Any):
        self.TableExtraRender = render
        return self

    def set_expandable(self, expandable: Expandable):
        self.Expandable = expandable
        return self

    def set_scroll(self, scroll: Any):
        self.Scroll = scroll
        return self

    def set_striped(self, striped: bool):
        self.Striped = striped
        return self

    def set_datasource(self, source: Any):
        self.Datasource = source
        return self

    def set_pagination(self, current: int, page_size: int, total: int, default_current: int, page_size_options: list):
        self.Pagination = {
            "current": current,
            "pageSize": page_size,
            "total": total,
            "defaultCurrent": default_current,
            "pageSizeOptions": page_size_options
        }
        return self

    def set_polling(self, polling: int):
        self.Polling = polling
        return self
