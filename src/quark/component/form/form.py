import json
from typing import Any, Dict, List, Optional

from pydantic import model_validator

from ..component import Component


class Form(Component):
    """
    表单组件类
    """

    title: Optional[str] = None
    width: Optional[str] = None
    colon: bool = True
    values: Dict[str, Any] = {}
    initial_values: Dict[str, Any] = {}
    label_align: str = "right"
    name: Optional[str] = None
    preserve: bool = True
    required_mark: bool = True
    scroll_to_first_error: bool = False
    size: str = "default"
    date_formatter: str = "string"
    layout: str = "horizontal"
    grid: bool = False
    row_props: Dict[str, Any] = {}
    label_col: Dict[str, Any] = {"span": 4}
    wrapper_col: Dict[str, Any] = {"span": 20}
    button_wrapper_col: Dict[str, Any] = {"offset": 4, "span": 20}
    api: Optional[str] = None
    api_type: str = "POST"
    target_blank: bool = False
    init_api: Optional[str] = None
    body: Any = None
    actions: List[Any] = None
    component_key: Optional[str] = None
    style: Dict[str, Any] = None

    @model_validator(mode="after")
    def init(self) -> "Form":
        """
        初始化
        """
        self.component = "form"
        self.colon = True
        self.label_align = "right"
        self.preserve = True
        self.required_mark = True
        self.size = "default"
        self.date_formatter = "string"
        self.layout = "horizontal"
        self.label_col = {
            "span": 4,
        }
        self.wrapper_col = {
            "span": 20,
        }
        self.button_wrapper_col = {
            "offset": 4,
            "span": 20,
        }
        self.api_type = "POST"

        self.set_key()

        return self

    def set_style(self, style: Dict[str, Any]) -> "Form":
        """
        Set style.
        """
        self.style = style
        return self

    def set_title(self, title: str) -> "Form":
        """
        配置表单标题
        """
        self.title = title
        return self

    def set_width(self, width: str) -> "Form":
        """
        配置表单宽度
        """
        self.width = width
        return self

    def set_colon(self, colon: bool) -> "Form":
        """
        配置 Form.Item 的 colon 的默认值。表示是否显示 label 后面的冒号 (只有在属性 layout 为 horizontal 时有效)
        """
        self.colon = colon
        return self

    def parse_initial_value(self, item: Any, initial_values: Dict[str, Any]) -> Any:
        """
        解析initialValue
        """
        value = None

        # 数组直接返回
        if isinstance(item, list):
            return None

        # 这里假设item是一个对象，具有name、default_value和value属性
        name = getattr(item, "name", "")
        if not name:
            return None

        if hasattr(item, "default_value") and item.default_value is not None:
            value = item.default_value

        if hasattr(item, "value") and item.value is not None:
            value = item.value

        if name in initial_values and initial_values[name] is not None:
            value = initial_values[name]

        return value

    def find_fields(self, fields: Any, when: bool) -> Any:
        """
        查找字段
        """
        items = []

        if isinstance(fields, list):
            for v in fields:
                items.extend(self.field_parser(v, when))
        else:
            items.extend(self.field_parser(fields, when))

        return items

    def field_parser(self, v: Any, when: bool) -> List[Any]:
        """
        解析字段
        """
        items = []

        # 数组直接返回
        if isinstance(v, list):
            return items

        # 检查是否有body属性
        if hasattr(v, "body") and v.body is not None:
            get_items = self.find_fields(v.body, True)
            if isinstance(get_items, list) and len(get_items) > 0:
                items.extend(get_items)
            return items

        # 检查是否有tab_panes属性
        if hasattr(v, "tab_panes") and v.tab_panes is not None:
            get_items = self.find_fields(v.tab_panes, True)
            if isinstance(get_items, list) and len(get_items) > 0:
                items.extend(get_items)
            return items

        # 默认情况
        component = getattr(v, "component", "")
        if "Field" in component:
            items.append(v)
            if when:
                when_fields = self.get_when_fields(v)
                if len(when_fields) > 0:
                    items.extend(when_fields)

        return items

    def get_when_fields(self, item: Any) -> List[Any]:
        """
        获取When组件中的字段
        """
        items = []

        if not hasattr(item, "when") or item.when is None:
            return items

        get_when = item.get_when() if hasattr(item, "get_when") else None

        if get_when is None:
            return items

        when_items = getattr(get_when, "items", None)
        if when_items is None:
            return items

        for v in when_items:
            if v.body is not None:
                if isinstance(v.body, list):
                    if len(v.body) > 0:
                        items.extend(v.body)
                else:
                    items.append(v.body)

        return items

    def set_initial_values(self, initial_values: Dict[str, Any]) -> "Form":
        """
        表单默认值，只有初始化以及重置时生效
        """
        data = initial_values.copy()

        fields = self.find_fields(self.body, True)
        if isinstance(fields, list):
            for v in fields:
                value = self.parse_initial_value(v, initial_values)
                if value is not None:
                    name = getattr(v, "name", "")
                    data[name] = value

        for k, v in data.items():
            if isinstance(v, str) and "[" in v:
                try:
                    m = json.loads(v)
                    if isinstance(m, list):
                        data[k] = m
                    elif isinstance(m, dict) and "{" in v:
                        data[k] = m
                except json.JSONDecodeError:
                    if "{" in v:
                        try:
                            m = json.loads(v)
                            if isinstance(m, dict):
                                data[k] = m
                        except json.JSONDecodeError:
                            pass
            elif isinstance(v, str) and "{" in v:
                try:
                    m = json.loads(v)
                    if isinstance(m, dict):
                        data[k] = m
                except json.JSONDecodeError:
                    pass

        self.initial_values = data
        return self

    def set_label_align(self, label_align: str) -> "Form":
        """
        label 标签的文本对齐方式,left | right
        """
        self.label_align = label_align
        return self

    def set_name(self, name: str) -> "Form":
        """
        表单名称，会作为表单字段 id 前缀使用
        """
        self.name = name
        return self

    def set_preserve(self, preserve: bool) -> "Form":
        """
        当字段被删除时保留字段值
        """
        self.preserve = preserve
        return self

    def set_required_mark(self, required_mark: bool) -> "Form":
        """
        必选样式，可以切换为必选或者可选展示样式。此为 Form 配置，Form.Item 无法单独配置
        """
        self.required_mark = required_mark
        return self

    def set_scroll_to_first_error(self, scroll_to_first_error: bool) -> "Form":
        """
        提交失败自动滚动到第一个错误字段
        """
        self.scroll_to_first_error = scroll_to_first_error
        return self

    def set_size(self, size: str) -> "Form":
        """
        设置字段组件的尺寸（仅限 antd 组件）,small | middle | large
        """
        self.size = size
        return self

    def set_date_formatter(self, date_formatter: str) -> "Form":
        """
        自动格式数据，例如 moment 的表单,支持 string 和 number 两种模式
        """
        self.date_formatter = date_formatter
        return self

    def set_layout(self, layout: str) -> "Form":
        """
        表单布局，horizontal | vertical
        """
        if layout == "vertical":
            self.label_col = None
            self.wrapper_col = None
            self.button_wrapper_col = None

        self.layout = layout
        return self

    def set_grid(self, grid: bool) -> "Form":
        """
        开启栅格化模式，宽度默认百分比，请使用 colProps 控制宽度，示例：https://procomponents.ant.design/components/form#栅格化布局
        """
        self.grid = grid
        return self

    def set_row_props(self, row_props: Dict[str, Any]) -> "Form":
        """
        开启 grid 模式时传递给 Row, 仅在ProFormGroup, ProFormList, ProFormFieldSet 中有效，默认：{ gutter: 8 }
        """
        self.row_props = row_props
        return self

    def set_label_col(self, label_col: Dict[str, Any]) -> "Form":
        """
        label 标签布局，同 <Col> 组件，设置 span offset 值，如 {span: 3, offset: 12} 或 sm: {span: 3, offset: 12}
        """
        self.label_col = label_col
        return self

    def set_wrapper_col(self, wrapper_col: Dict[str, Any]) -> "Form":
        """
        需要为输入控件设置布局样式时，使用该属性，用法同 labelCol
        """
        if self.layout == "vertical":
            raise Exception("If layout set vertical mode,can't set wrapperCol!")

        self.wrapper_col = wrapper_col
        return self

    def set_button_wrapper_col(self, button_wrapper_col: Dict[str, Any]) -> "Form":
        """
        表单按钮布局样式,默认：['offset' => 2, 'span' => 22 ]
        """
        if self.layout == "vertical":
            raise Exception("If layout set vertical mode,can't set buttonWrapperCol!")

        self.button_wrapper_col = button_wrapper_col
        return self

    def set_api(self, api: str) -> "Form":
        """
        表单提交的接口链接
        """
        self.api = api
        return self

    def set_api_type(self, api_type: str) -> "Form":
        """
        表单提交接口的类型
        """
        self.api_type = api_type
        return self

    def set_target_blank(self, target_blank: bool) -> "Form":
        """
        提交表单的数据是否打开新页面，只有在GET类型的时候有效
        """
        self.target_blank = target_blank
        return self

    def set_init_api(self, init_api: str) -> "Form":
        """
        获取表单数据
        """
        self.init_api = init_api
        return self

    def set_body(self, items: Any) -> "Form":
        """
        表单项
        """
        self.body = items
        return self

    def parse_submit_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        解析保存提交数据库前的值
        """
        # 注意：这里假设self.body是一个列表
        if isinstance(self.body, list):
            for v in self.body:
                ignore = getattr(v, "ignore", False)

                # 删除忽略的值
                if ignore:
                    name = getattr(v, "name", "")
                    if name and name in data:
                        del data[name]

        for k, v in data.items():
            if isinstance(v, dict):
                data[k] = json.dumps(v)

        return data

    def set_actions(self, actions: List[Any]) -> "Form":
        """
        设置表单行为
        """
        self.actions = actions
        return self
