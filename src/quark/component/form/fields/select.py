import json
from typing import Dict, List, Optional, Any, Callable, Union
from .base import Base


class FieldNames(Base):
    """
    定义选项中标签、值和子项字段名的类。

    Attributes:
        label (str): 标签字段名。
        value (str): 值字段名。
        children (str): 子项字段名。
    """

    label: str
    value: str
    children: str


class Option(Base):
    """
    表示选择框选项的类。

    Attributes:
        label (str): 选项显示的标签。
        value (Any): 选项对应的值。
        disabled (bool): 选项是否禁用，默认为 False。
    """

    label: str
    value: Any
    disabled: bool = False


class Select(Base):

    component: str = "selectField"
    """
    组件名称
    """

    allow_clear: bool = True
    """
    可以点击清除图标删除内容，默认值为 True
    """

    auto_clear_search_value: bool = False
    """
    是否在选中项后清空搜索框，只在 mode 为 multiple 或 tags 时有效，默认值为 False
    """

    auto_focus: bool = False
    """
    默认获取焦点，默认值为 False
    """

    bordered: bool = True
    """
    是否有边框，默认值为 True
    """

    clear_icon: Optional[Any] = None
    """
    自定义的多选框清空图标，默认值为 None
    """

    default_active_first_option: bool = True
    """
    是否默认高亮第一个选项，默认值为 True
    """

    default_open: bool = False
    """
    是否默认展开下拉菜单，默认值为 False
    """

    default_value: Optional[Any] = None
    """
    默认选中的选项，默认值为 None
    """

    disabled: bool = False
    """
    整组失效，默认值为 False
    """

    popup_class_name: str = ""
    """
    下拉菜单的 className 属性
    """

    dropdown_match_select_width: Optional[Any] = None
    """
    下拉菜单和选择器同宽。默认将设置 min-width，当值小于选择框宽度时会被忽略。false 时会关闭虚拟滚动，默认值为 None
    """

    dropdown_style: Optional[Any] = None
    """
    下拉菜单的 style 属性，默认值为 None
    """

    field_names: FieldNames = None
    """
    自定义 options 中 label value children 的字段
    """

    label_in_value: bool = False
    """
    是否把每个选项的 label 包装到 value 中，
            会把 Select 的 value 类型从 string 变为 { value: string, label: ReactNode } 的格式，默认值为 False
    """

    list_height: int = 256
    """
    设置弹窗滚动高度 256，默认值为 256
    """

    loading: bool = False
    """
    加载中状态，默认值为 False
    """

    max_tag_count: int = 0
    """
    最多显示多少个 tag，响应式模式会对性能产生损耗，默认值为 0
    """

    max_tag_placeholder: str = ""
    """
    隐藏 tag 时显示的内容，默认值为 ""
    """

    max_tag_text_length: int = 0
    """
    最大显示的 tag 文本长度，默认值为 0
    """

    menu_item_selected_icon: Optional[Any] = None
    """
    自定义多选时当前选中的条目图标，默认值为 None
    """

    mode: str = ""
    """
    设置 Select 的模式为多选或标签 multiple | tags，默认值为 ""
    """

    not_found_content: str = ""
    """
    当下拉列表为空时显示的内容，默认值为 ""
    """

    open: bool = False
    """
    是否展开下拉菜单，默认值为 False
    """

    option_filter_prop: str = ""
    """
    搜索时过滤对应的 option 属性，如设置为 children 表示对内嵌内容进行搜索。
            若通过 options 属性配置选项内容，建议设置 optionFilterProp="label" 来对内容进行搜索，默认值为 ""
    """

    option_label_prop: str = ""
    """
    回填到选择框的 Option 的属性值，默认是 Option 的子元素。
            比如在子元素需要高亮效果时，此值可以设为 value，默认值为 ""
    """

    options: List[Option] = []
    """
    可选项数据源，默认值为空列表
    """

    placeholder: str = ""
    """
    选择框默认文本，默认值为 ""
    """

    placement: str = ""
    """
    选择框弹出的位置 bottomLeft bottomRight topLeft topRight
    """

    remove_icon: Optional[Any] = None
    """
    自定义的多选框清除图标，默认值为 None
    """

    search_value: str = ""
    """
    控制搜索文本，默认值为 ""
    """

    show_arrow: bool = True
    """
    是否显示下拉小箭头，默认值为 True
    """

    show_search: bool = False
    """
    配置是否可搜索，默认值为 False
    """

    size: str = ""
    """
    选择框大小
    """

    status: str = ""
    """
    设置校验状态 'error' | 'warning'
    """

    suffix_icon: Optional[Any] = None
    """
    自定义的选择框后缀图标，默认值为 None
    """

    token_separators: Optional[Any] = None
    """
    自动分词的分隔符，仅在 mode="tags" 时生效，默认值为 None
    """

    value: Optional[Any] = None
    """
    指定当前选中的条目，多选时为一个数组。
            （value 数组引用未变化时，Select 不会更新），默认值为 None
    """

    virtual: bool = True
    """
    设置 false 时关闭虚拟滚动，默认值为 True
    """

    load: Dict[str, str] = {}
    """
    单向联动，默认值为空字典
    """

    style: Dict[str, Any] = {}
    """
    自定义样式，默认值为空字典
    """

    def get_options(self) -> List[Option]:
        """
        获取当前可选项。

        Returns:
            List[Option]: 可选项列表。
        """
        return self.options

    def set_callback(self, closure: Optional[Callable[[Dict[str, Any]], Any]]):
        """
        设置回调函数。

        Args:
            closure (Optional[Callable[[Dict[str, Any]], Any]]): 回调函数。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        if closure is not None:
            self.callback = closure
        return self

    def get_callback(self) -> Any:
        """
        获取回调函数。

        Returns:
            Any: 回调函数。
        """
        return self.callback

    def build_options(
        self, items: Any, label_name: str, value_name: str
    ) -> List[Option]:
        """
        使用反射构建树结构。

        Args:
            items (Any): 包含选项数据的对象。
            label_name (str): 标签字段名。
            value_name (str): 值字段名。

        Returns:
            List[Option]: 构建好的选项列表。
        """
        options: List[Option] = []

        if not isinstance(items, list):
            return options

        for item in items:
            if hasattr(item, label_name) and hasattr(item, value_name):
                label = getattr(item, label_name)
                value = getattr(item, value_name)
                option = Option(label=label, value=value)
                options.append(option)

        return options

    def list_to_options(
        self, list_data: Any, label_name: str, value_name: str
    ) -> List[Option]:
        """
        将列表数据转换为选项列表。

        Args:
            list_data (Any): 列表数据。
            label_name (str): 标签字段名。
            value_name (str): 值字段名。

        Returns:
            List[Option]: 转换后的选项列表。
        """
        return self.build_options(list_data, label_name, value_name)

    def set_options(self, *options: Any):
        """
        设置属性，示例：[Option(value=1, label="男"), Option(value=2, label="女")]
        或者 set_options(options, "label_name", "value_name")

        Args:
            *options: 可变参数，不同数量有不同含义。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        if len(options) == 1:
            self.options = options[0]
            return self
        if len(options) == 3:
            self.options = self.list_to_options(options[0], options[1], options[2])
        return self

    def set_api(self, api: str):
        """
        设置获取数据接口。

        Args:
            api (str): 接口地址。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.api = api
        return self

    def set_allow_clear(self, allow_clear: bool):
        """
        设置是否可以点击清除图标删除内容。

        Args:
            allow_clear (bool): 是否允许清除。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.allow_clear = allow_clear
        return self

    def set_auto_clear_search_value(self, auto_clear_search_value: bool):
        """
        设置是否在选中项后清空搜索框。

        Args:
            auto_clear_search_value (bool): 是否自动清空搜索框。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.auto_clear_search_value = auto_clear_search_value
        return self

    def set_auto_focus(self, auto_focus: bool):
        """
        设置默认是否获取焦点。

        Args:
            auto_focus (bool): 是否自动获取焦点。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.auto_focus = auto_focus
        return self

    def set_bordered(self, bordered: bool):
        """
        设置是否有边框。

        Args:
            bordered (bool): 是否有边框。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.bordered = bordered
        return self

    def set_clear_icon(self, clear_icon: Any):
        """
        设置自定义的多选框清空图标。

        Args:
            clear_icon (Any): 清空图标。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.clear_icon = clear_icon
        return self

    def set_default_active_first_option(self, default_active_first_option: bool):
        """
        设置是否默认高亮第一个选项。

        Args:
            default_active_first_option (bool): 是否默认高亮第一个选项。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.default_active_first_option = default_active_first_option
        return self

    def set_default_open(self, default_open: bool):
        """
        设置是否默认展开下拉菜单。

        Args:
            default_open (bool): 是否默认展开。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.default_open = default_open
        return self

    def set_popup_class_name(self, popup_class_name: str):
        """
        设置下拉菜单的 className 属性。

        Args:
            popup_class_name (str): className 属性值。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.popup_class_name = popup_class_name
        return self

    def set_dropdown_match_select_width(self, dropdown_match_select_width: Any):
        """
        设置下拉菜单和选择器是否同宽。

        Args:
            dropdown_match_select_width (Any): 是否同宽。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.dropdown_match_select_width = dropdown_match_select_width
        return self

    def set_dropdown_style(self, dropdown_style: Any):
        """
        设置下拉菜单的 style 属性。

        Args:
            dropdown_style (Any): style 属性值。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.dropdown_style = dropdown_style
        return self

    def set_field_names(self, field_names: FieldNames):
        """
        设置自定义 options 中 label value children 的字段。

        Args:
            field_names (FieldNames): 字段名配置。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.field_names = field_names
        return self

    def set_label_in_value(self, label_in_value: bool):
        """
        设置是否把每个选项的 label 包装到 value 中。

        Args:
            label_in_value (bool): 是否包装。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.label_in_value = label_in_value
        return self

    def set_list_height(self, list_height: int):
        """
        设置弹窗滚动高度。

        Args:
            list_height (int): 滚动高度值。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.list_height = list_height
        return self

    def set_loading(self, loading: bool):
        """
        设置加载中状态。

        Args:
            loading (bool): 是否加载中。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.loading = loading
        return self

    def set_max_tag_count(self, max_tag_count: int):
        """
        设置最多显示多少个 tag。

        Args:
            max_tag_count (int): 最多显示的 tag 数量。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.max_tag_count = max_tag_count
        return self

    def set_max_tag_placeholder(self, max_tag_placeholder: str):
        """
        设置隐藏 tag 时显示的内容。

        Args:
            max_tag_placeholder (str): 显示内容。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.max_tag_placeholder = max_tag_placeholder
        return self

    def set_max_tag_text_length(self, max_tag_text_length: int):
        """
        设置最大显示的 tag 文本长度。

        Args:
            max_tag_text_length (int): 最大文本长度。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.max_tag_text_length = max_tag_text_length
        return self

    def set_menu_item_selected_icon(self, menu_item_selected_icon: Any):
        """
        设置自定义多选时当前选中的条目图标。

        Args:
            menu_item_selected_icon (Any): 条目图标。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.menu_item_selected_icon = menu_item_selected_icon
        return self

    def set_mode(self, mode: str):
        """
        设置 Select 的模式。

        Args:
            mode (str): 模式，如 'multiple', 'tags'。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.mode = mode
        return self

    def set_not_found_content(self, not_found_content: str):
        """
        设置当下拉列表为空时显示的内容。

        Args:
            not_found_content (str): 显示内容。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.not_found_content = not_found_content
        return self

    def set_open(self, open: bool):
        """
        设置是否展开下拉菜单。

        Args:
            open (bool): 是否展开。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.open = open
        return self

    def set_option_filter_prop(self, option_filter_prop: str):
        """
        设置搜索时过滤对应的 option 属性。

        Args:
            option_filter_prop (str): 属性名。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.option_filter_prop = option_filter_prop
        return self

    def set_option_label_prop(self, option_label_prop: str):
        """
        设置回填到选择框的 Option 的属性值。

        Args:
            option_label_prop (str): 属性值。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.option_label_prop = option_label_prop
        return self

    def set_placeholder(self, placeholder: str):
        """
        设置选择框默认文本。

        Args:
            placeholder (str): 默认文本。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.placeholder = placeholder
        return self

    def set_placement(self, placement: str):
        """
        设置选择框弹出的位置。

        Args:
            placement (str): 弹出位置，如 'bottomLeft', 'bottomRight' 等。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.placement = placement
        return self

    def set_remove_icon(self, remove_icon: Any):
        """
        设置自定义的多选框清除图标。

        Args:
            remove_icon (Any): 清除图标。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.remove_icon = remove_icon
        return self

    def set_search_value(self, search_value: str):
        """
        设置控制搜索文本。

        Args:
            search_value (str): 搜索文本。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.search_value = search_value
        return self

    def set_show_arrow(self, show_arrow: bool):
        """
        设置是否显示下拉小箭头。

        Args:
            show_arrow (bool): 是否显示。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.show_arrow = show_arrow
        return self

    def set_show_search(self, show_search: bool):
        """
        设置配置是否可搜索。

        Args:
            show_search (bool): 是否可搜索。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.show_search = show_search
        return self

    def set_size(self, size: str):
        """
        设置选择框大小。

        Args:
            size (str): 大小，如 'large', 'middle', 'small'。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.size = size
        return self

    def set_status(self, status: str):
        """
        设置校验状态。

        Args:
            status (str): 校验状态，如 'error', 'warning'。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.status = status
        return self

    def set_suffix_icon(self, suffix_icon: Any):
        """
        设置自定义的选择框后缀图标。

        Args:
            suffix_icon (Any): 后缀图标。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.suffix_icon = suffix_icon
        return self

    def set_token_separators(self, token_separators: Any):
        """
        设置自动分词的分隔符。

        Args:
            token_separators (Any): 分隔符。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.token_separators = token_separators
        return self

    def set_virtual(self, virtual: bool):
        """
        设置是否关闭虚拟滚动。

        Args:
            virtual (bool): 是否关闭。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.virtual = virtual
        return self

    def set_load(self, field: str, api: str):
        """
        设置单向联动。

        Args:
            field (str): 字段名。
            api (str): 接口地址。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.load = {"field": field, "api": api}
        return self

    def get_value_enum(self) -> Dict[Any, Any]:
        """
        获取当前列值的枚举 valueEnum。

        Returns:
            Dict[Any, Any]: 列值枚举字典。
        """
        data: Dict[Any, Any] = {}
        for option in self.options:
            data[option.value] = option.label
        return data

    def get_option_label(self, value: Any) -> str:
        """
        根据 value 值获取 Option 的 Label。

        Args:
            value (Any): 选项的值。

        Returns:
            str: 对应的标签，多个标签用逗号分隔。
        """
        labels: List[str] = []
        values: List[Any] = []

        if isinstance(value, str):
            if "[" in value or "{" in value:
                try:
                    values = json.loads(value)
                except json.JSONDecodeError:
                    pass

        if values:
            for option in self.options:
                for v in values:
                    if v == option.value:
                        labels.append(option.label)
        else:
            for option in self.options:
                if value == option.value:
                    labels.append(option.label)

        return ",".join(labels)

    def get_option_value(self, label: str) -> Union[List[Any], Any]:
        """
        根据 label 值获取 Option 的 Value。

        Args:
            label (str): 选项的标签，多个标签用逗号或中文逗号分隔。

        Returns:
            Union[List[Any], Any]: 对应的单个值或值列表。
        """
        values: List[Any] = []
        value: Any = None
        labels: List[str] = []

        get_labels = label.split(",")
        if len(get_labels) > 1:
            labels = get_labels
        get_labels = label.split("，")
        if len(get_labels) > 1:
            labels = get_labels

        if len(labels) > 1:
            for option in self.options:
                for get_label in labels:
                    if option.label == get_label:
                        values.append(option.value)
        else:
            for option in self.options:
                if option.label == label:
                    value = option.value

        if values:
            return values
        return value

    def get_option_labels(self) -> str:
        """
        获取所有 Option 的 Labels。

        Returns:
            str: 所有标签，用逗号分隔。
        """
        labels = [option.label for option in self.options]
        return ",".join(labels)

    def set_default_value(self, default_value: Any):
        self.default_value = default_value
        return self

    def set_value(self, value: Any):
        self.value = value
        return self
