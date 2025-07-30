from typing import Any, Dict, List, Optional
from .base import Base


class FieldNames(Base):
    label: str
    value: str
    children: str


class TreeData(Base):
    title: str
    value: Any
    children: List["TreeData"] = []
    disabled: bool = None
    disable_checkbox: bool = None
    selectable: bool = None
    checkable: bool = None


class TreeSelect(Base):
    component: str = "treeSelectField"
    """
    组件名称
    """

    allow_clear: bool = True
    """
    可以点击清除图标删除内容
    """

    auto_clear_search_value: bool = None
    """
    是否在选中项后清空搜索框，只在 mode 为 multiple 或 tags 时有效
    """

    bordered: bool = None
    """
    是否有边框
    """

    default_value: Optional[Any] = None
    """
    默认选中的选项
    """

    disabled: bool = None
    """
    整组失效
    """

    popup_class_name: Optional[str] = None
    """
    下拉菜单的 className 属性
    """

    dropdown_match_select_width: Optional[Any] = None
    """
    下拉菜单和选择器同宽。默认将设置 min-width，当值小于选择框宽度时会被忽略。false 时会关闭虚拟滚动
    """

    dropdown_style: Optional[Any] = None
    """
    下拉菜单的 style 属性
    """

    field_names: Optional[FieldNames] = None
    """
    自定义 options 中 label value children 的字段
    """

    label_in_value: bool = None
    """
    是否把每个选项的 label 包装到 value 中，会把 Select 的 value 类型从 string 变为 { value: string, label: ReactNode } 的格式
    """

    list_height: int = 256
    """
    设置弹窗滚动高度 256
    """

    max_tag_count: int = 0
    """
    最多显示多少个 tag，响应式模式会对性能产生损耗
    """

    max_tag_placeholder: Optional[str] = None
    """
    隐藏 tag 时显示的内容
    """

    max_tag_text_length: int = 0
    """
    最大显示的 tag 文本长度
    """

    multiple: bool = None
    """
    支持多选（当设置 treeCheckable 时自动变为 true）
    """

    not_found_content: Optional[str] = None
    """
    当下拉列表为空时显示的内容
    """

    placeholder: Optional[str] = None
    """
    选择框默认文本
    """

    placement: Optional[str] = None
    """
    选择框弹出的位置 bottomLeft bottomRight topLeft topRight
    """

    search_value: Optional[str] = None
    """
    控制搜索文本
    """

    show_arrow: bool = None
    """
    是否显示下拉小箭头
    """

    show_search: bool = None
    """
    配置是否可搜索
    """

    size: Optional[str] = None
    """
    选择框大小
    """

    status: Optional[str] = None
    """
    设置校验状态 'error' | 'warning'
    """

    suffix_icon: Optional[Any] = None
    """
    自定义的选择框后缀图标
    """

    switcher_icon: Optional[Any] = None
    """
    自定义树节点的展开/折叠图标
    """

    tree_checkable: bool = None
    """
    显示 Checkbox
    """

    tree_check_strictly: bool = None
    """
    checkable 状态下节点选择完全受控（父子节点选中状态不再关联），会使得 labelInValue 强制为 true
    """

    tree_data: List[TreeData] = []
    """
    treeNodes 数据，如果设置则不需要手动构造 TreeNode 节点（value 在整个树范围内唯一）
    """

    tree_data_simple_mode: Optional[Any] = None
    """
    使用简单格式的 treeData，具体设置参考可设置的类型 (此时 treeData 应变为这样的数据结构: [{id:1, pId:0, value:'1', title:"test1",...},...]， pId 是父节点的 id)
    """

    tree_default_expand_all: bool = True
    """
    默认展开所有树节点
    """

    tree_default_expanded_keys: List[Any] = None
    """
    默认展开的树节点
    """

    tree_expand_action: Optional[Any] = None
    """
    点击节点 title 时的展开逻辑，可选：false | click | doubleClick
    """

    tree_expanded_keys: List[Any] = None
    """
    设置展开的树节点
    """

    tree_icon: bool = None
    """
    是否展示 TreeNode title 前的图标，没有默认样式，如设置为 true，需要自行定义图标相关样式
    """

    tree_line: bool = True
    """
    是否展示线条样式
    """

    tree_node_filter_prop: Optional[str] = None
    """
    输入项过滤对应的 treeNode 属性
    """

    tree_node_label_prop: Optional[str] = None
    """
    作为显示的 prop 设置
    """

    value: Optional[Any] = None
    """
    指定当前选中的条目，多选时为一个数组。（value 数组引用未变化时，Select 不会更新）
    """

    virtual: bool = None
    """
    设置 false 时关闭虚拟滚动
    """

    style: Optional[Dict[str, Any]] = None
    """
    自定义样式
    """

    def __init__(self, **data):
        super().__init__(**data)
        self.component = "treeSelectField"
        self.colon = True
        self.label_align = "right"
        self.show_on_index = True
        self.show_on_detail = True
        self.show_on_creation = True
        self.show_on_update = True
        self.show_on_export = True
        self.show_on_import = True
        self.allow_clear = True
        self.tree_default_expand_all = True
        self.tree_line = True
        self.set_width(200)
        self.set_key("DEFAULT_KEY", False)

    def set_allow_clear(self, allow_clear: bool):
        self.allow_clear = allow_clear
        return self

    def set_auto_clear_search_value(self, auto_clear_search_value: bool):
        self.auto_clear_search_value = auto_clear_search_value
        return self

    def set_bordered(self, bordered: bool):
        self.bordered = bordered
        return self

    def set_popup_class_name(self, popup_class_name: str):
        self.popup_class_name = popup_class_name
        return self

    def set_dropdown_match_select_width(self, dropdown_match_select_width: Any):
        self.dropdown_match_select_width = dropdown_match_select_width
        return self

    def set_dropdown_style(self, dropdown_style: Any):
        self.dropdown_style = dropdown_style
        return self

    def set_field_names(self, field_names: FieldNames):
        self.field_names = field_names
        return self

    def set_label_in_value(self, label_in_value: bool):
        self.label_in_value = label_in_value
        return self

    def set_list_height(self, list_height: int):
        self.list_height = list_height
        return self

    def set_max_tag_count(self, max_tag_count: int):
        self.max_tag_count = max_tag_count
        return self

    def set_max_tag_placeholder(self, max_tag_placeholder: str):
        self.max_tag_placeholder = max_tag_placeholder
        return self

    def set_max_tag_text_length(self, max_tag_text_length: int):
        self.max_tag_text_length = max_tag_text_length
        return self

    def set_multiple(self, multiple: bool):
        self.multiple = multiple
        return self

    def set_not_found_content(self, not_found_content: str):
        self.not_found_content = not_found_content
        return self

    def set_placeholder(self, placeholder: str):
        self.placeholder = placeholder
        return self

    def set_placement(self, placement: str):
        self.placement = placement
        return self

    def set_search_value(self, search_value: str):
        self.search_value = search_value
        return self

    def set_show_arrow(self, show_arrow: bool):
        self.show_arrow = show_arrow
        return self

    def set_show_search(self, show_search: bool):
        self.show_search = show_search
        return self

    def set_size(self, size: str):
        self.size = size
        return self

    def set_status(self, status: str):
        self.status = status
        return self

    def set_suffix_icon(self, suffix_icon: Any):
        self.suffix_icon = suffix_icon
        return self

    def set_switcher_icon(self, switcher_icon: Any):
        self.switcher_icon = switcher_icon
        return self

    def set_tree_checkable(self, tree_checkable: bool):
        self.tree_checkable = tree_checkable
        return self

    def set_tree_check_strictly(self, tree_check_strictly: bool):
        self.tree_check_strictly = tree_check_strictly
        return self

    def build_tree(
        self,
        items: Any,
        pid: int,
        parent_key_name: str,
        title_name: str,
        value_name: str,
    ) -> List[TreeData]:
        tree = []

        for item in items:
            # 支持对象和字典两种格式
            if hasattr(item, value_name):
                value = getattr(item, value_name)
                parent_key = getattr(item, parent_key_name)
                title = getattr(item, title_name)
            elif isinstance(item, dict):
                value = item.get(value_name)
                parent_key = item.get(parent_key_name)
                title = item.get(title_name)
            else:
                # 如果既不是对象也不是字典，跳过该项
                continue

            if parent_key == pid:
                children = self.build_tree(
                    items, value, parent_key_name, title_name, value_name
                )
                option = TreeData(title=title, value=value, children=children)
                tree.append(option)

        return tree

    def list_to_tree_data(
        self,
        list_data: Any,
        root_id: int,
        parent_key_name: str,
        title_name: str,
        value_name: str,
    ) -> List[TreeData]:
        return self.build_tree(
            list_data, root_id, parent_key_name, title_name, value_name
        )

    def set_tree_data(self, *tree_data: Any):
        if len(tree_data) == 1:
            if isinstance(tree_data[0], list) and all(
                isinstance(item, TreeData) for item in tree_data[0]
            ):
                self.tree_data = tree_data[0]
                return self
        if len(tree_data) == 4:
            self.tree_data = self.list_to_tree_data(
                tree_data[0], 0, tree_data[1], tree_data[2], tree_data[3]
            )
        if len(tree_data) == 5:
            self.tree_data = self.list_to_tree_data(
                tree_data[0], tree_data[1], tree_data[2], tree_data[3], tree_data[4]
            )
        return self

    def get_tree_data(self) -> List[TreeData]:
        return self.tree_data

    def get_data(self) -> List[TreeData]:
        return self.tree_data

    def set_tree_data_simple_mode(self, tree_data_simple_mode: Any):
        self.tree_data_simple_mode = tree_data_simple_mode
        return self

    def set_tree_default_expand_all(self, tree_default_expand_all: bool):
        self.tree_default_expand_all = tree_default_expand_all
        return self

    def set_tree_default_expanded_keys(self, tree_default_expanded_keys: List[Any]):
        self.tree_default_expanded_keys = tree_default_expanded_keys
        return self

    def set_tree_expand_action(self, tree_expand_action: List[Any]):
        self.tree_expand_action = tree_expand_action
        return self

    def set_tree_expanded_keys(self, tree_expanded_keys: List[Any]):
        self.tree_expanded_keys = tree_expanded_keys
        return self

    def set_tree_icon(self, tree_icon: bool):
        self.tree_icon = tree_icon
        return self

    def set_tree_line(self, tree_line: bool):
        self.tree_line = tree_line
        return self

    def set_tree_node_filter_prop(self, tree_node_filter_prop: str):
        self.tree_node_filter_prop = tree_node_filter_prop
        return self

    def set_tree_node_label_prop(self, tree_node_label_prop: str):
        self.tree_node_label_prop = tree_node_label_prop
        return self

    def set_virtual(self, virtual: bool):
        self.virtual = virtual
        return self

    def set_style(self, style: Dict[str, Any]):
        self.style = style
        return self

    def set_default_value(self, default_value: Any):
        self.default_value = default_value
        return self

    def set_value(self, value: Any):
        self.value = value
        return self
