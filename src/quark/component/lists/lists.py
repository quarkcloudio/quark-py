from pydantic import BaseModel
from typing import Any, Optional
from ..component import Component

class Lists(Component):
    row_key: str = ""
    api: str = ""
    api_type: str = ""
    header_title: str = ""
    metas: Optional[Any] = None
    row_selection: Optional[Any] = None
    striped: bool = False
    datasource: Optional[Any] = None
    pagination: Optional[Any] = None
    tool_bar: Optional[Any] = None
    style: Optional[dict[str, Any]] = None

    # Set style.
    def set_style(self, style: dict[str, Any]) -> 'Lists':
        self.style = style
        return self

    # layout 的左上角 的 title
    def set_row_key(self, row_key: str) -> 'Lists':
        self.row_key = row_key
        return self

    # 获取表格数据接口
    def set_api(self, api: str) -> 'Lists':
        self.api = api
        return self

    # 获取表格数据接口类型
    def set_api_type(self, api_type: str) -> 'Lists':
        self.api_type = api_type
        return self

    # 表头标题
    def set_title(self, title: str) -> 'Lists':
        self.header_title = title
        return self

    # 表头标题
    def set_header_title(self, header_title: str) -> 'Lists':
        self.header_title = header_title
        return self

    # 批量设置表格列
    def set_metas(self, metas: Any) -> 'Lists':
        limits = [
            "type",
            "title",
            "subTitle",
            "description",
            "avatar",
            "actions",
            "content",
            "extra"
        ]

        if isinstance(metas, dict):
            for k in metas.keys():
                if k not in limits:
                    raise ValueError("meta index key must be in 'type','title','subTitle','description','avatar','actions','content','extra'!")
        self.metas = metas
        return self

    # 批量操作选择项
    def set_row_selection(self, row_selection: list[Any]) -> 'Lists':
        self.row_selection = row_selection
        return self

    # 透传 ProUtils 中的 ListToolBar 配置项
    def set_tool_bar(self, tool_bar: Any) -> 'Lists':
        self.tool_bar = tool_bar
        return self

    # 设置表格滚动
    def set_striped(self, striped: bool) -> 'Lists':
        self.striped = striped
        return self

    # 表格数据
    def set_datasource(self, datasource: Any) -> 'Lists':
        self.datasource = datasource
        return self

    # 表格分页
    def set_pagination(self, current: int, page_size: int, total: int, default_current: int) -> 'Lists':
        self.pagination = {
            "current": current,
            "page_size": page_size,
            "total": total,
            "default_current": default_current
        }
        return self