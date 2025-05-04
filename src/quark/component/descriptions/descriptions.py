from pydantic import Field, model_validator
from typing import Any, Dict, Optional, Union
from ..component import Component

class Descriptions(Component):
    component: str = "descriptions"
    title: str = Field("", description="标题")
    tooltip: str = Field("", description="内容的补充描述，hover 后显示")
    extra: Optional[Any] = Field(None, description="描述列表的操作区域，显示在右上方")
    bordered: bool = Field(False, description="是否展示边框")
    column: Union[int, Dict[str, int]] = Field(1, description="一行的 ProDescriptionsItems 数量")
    size: str = Field("default", description="设置尺寸")
    layout: str = Field("horizontal", description="布局，horizontal|vertical")
    colon: bool = Field(True, description="配置 ProDescriptions.Item 的 colon 的默认值")
    columns: Optional[Any] = Field(None, description="列")
    data_source: Optional[Any] = Field(None, description="数据")
    init_api: Optional[Any] = Field(None, description="数据初始化接口")
    items: Optional[Any] = Field(None, description="数据项")
    actions: Optional[Any] = Field(None, description="行为")
    style: Optional[Dict[str, Any]] = Field(None, description="样式")

    @model_validator(mode="after")
    def init(self):
        self.set_key()
        return self

    def set_style(self, style: Dict[str, Any]):
        # 设置样式
        self.style = style
        return self

    def set_title(self, title: str):
        # 设置标题
        self.title = title
        return self

    def set_tooltip(self, tooltip: str):
        # 设置内容的补充描述，hover 后显示
        self.tooltip = tooltip
        return self

    def set_extra(self, extra: Any):
        # 设置描述列表的操作区域
        self.extra = extra
        return self

    def set_bordered(self, bordered: bool):
        # 设置是否展示边框
        self.bordered = bordered
        return self

    def set_layout(self, layout: str):
        # 设置布局
        self.layout = layout
        return self

    def set_column(self, column: Union[int, Dict[str, int]]):
        # 设置一行的 ProDescriptionsItems 数量
        self.column = column
        return self

    def set_columns(self, columns: Any):
        # 设置列
        self.columns = columns
        return self

    def set_data_source(self, data_source: Any):
        # 设置数据
        self.data_source = data_source
        return self

    def set_size(self, size: str):
        # 设置尺寸
        self.size = size
        return self

    def set_colon(self, colon: bool):
        # 设置 ProDescriptions.Item 的 colon 的默认值
        self.colon = colon
        return self

    def set_init_api(self, api: Any):
        # 设置数据初始化接口
        self.init_api = api
        return self

    def set_items(self, items: Any):
        # 设置数据项
        self.items = items
        return self

    def set_actions(self, actions: Any):
        # 设置行为
        self.actions = actions
        return self