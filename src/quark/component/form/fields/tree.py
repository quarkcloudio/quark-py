from typing import Any, Dict, List, Optional

from .base import Base


class FieldNames(Base):
    """
    表示 Tree 组件字段名映射的类。

    Attributes:
        title (str): 对应树节点标题的字段名。
        key (str): 对应树节点键的字段名。
        children (str): 对应树节点子节点的字段名。
    """

    title: str
    key: str
    children: str


class TreeData(Base):
    """
    表示 Tree 组件树节点数据的类。

    Attributes:
        checkable (bool): 当树为 checkable 时，设置独立节点是否展示 Checkbox。
        disable_checkbox (bool): 禁掉 checkbox。
        disabled (bool): 禁掉响应。
        icon (Optional[Any]): 自定义图标。可接收组件，props 为当前节点 props。
        is_leaf (bool): 设置为叶子节点 (设置了 loadData 时有效)。为 false 时会强制将其作为父节点。
        key (Any): 被树的 (default)ExpandedKeys / (default)CheckedKeys / (default)SelectedKeys 属性所用。
            注意：整个树范围内的所有节点的 key 值不能重复！
        selectable (bool): 设置节点是否可被选中。
        title (str): 标题。
        children (List['TreeData']): 子节点。
    """

    checkable: bool = None
    disable_checkbox: bool = None
    disabled: bool = None
    icon: Optional[Any] = None
    is_leaf: bool = None
    key: Any
    selectable: bool = None
    title: str
    children: List["TreeData"] = []


class Tree(Base):

    component: str = "treeField"
    """
    组件名称
    """

    auto_expand_parent: bool = False
    """
    是否自动展开父节点，默认值为 False
    """

    block_node: bool = False
    """
    是否节点占据一行，默认值为 False
    """

    checkable: bool = True
    """
    节点前添加 Checkbox 复选框，默认值为 True
    """

    checked_keys: List[Any] = []
    """
    （受控）选中复选框的树节点，默认值为 []
    """

    check_strictly: bool = False
    """
    checkable 状态下节点选择完全受控（父子节点选中状态不再关联），默认值为 False
    """

    default_checked_keys: List[Any] = []
    """
    默认选中复选框的树节点，默认值为 []
    """

    default_expand_all: bool = False
    """
    默认展开所有树节点，默认值为 False
    """

    default_expanded_keys: List[Any] = []
    """
    默认展开指定的树节点，默认值为 []
    """

    default_expand_parent: bool = False
    """
    默认展开父节点，默认值为 False
    """

    default_selected_keys: List[Any] = []
    """
    默认选中的树节点，默认值为 []
    """

    default_value: Optional[Any] = None
    """
    默认选中的选项，默认值为 None
    """

    disabled: bool = False
    """
    整组失效，默认值为 False
    """

    draggable: bool = False
    """
    设置节点可拖拽，可以通过 icon: false 关闭拖拽提示图标，默认值为 False
    """

    expanded_keys: List[Any] = []
    """
    （受控）展开指定的树节点，默认值为 []
    """

    field_names: Optional[FieldNames] = None
    """
    自定义 options 中 label value children 的字段，默认值为 None
    """

    height: int = None
    """
    设置虚拟滚动容器高度，设置后内部节点不再支持横向滚动
    """

    icon: Optional[Any] = None
    """
    自定义树节点图标
    """

    multiple: bool = False
    """
    支持点选多个节点（节点本身），默认值为 False
    """

    placeholder: Optional[str] = None
    """
    占位文本，默认值为 None
    """

    root_class_name: str = None
    """
    添加在 Tree 最外层的 className，默认值为 ""
    """

    root_style: Optional[Any] = None
    """
    添加在 Tree 最外层的 style，默认值为 None
    """

    selectable: bool = True
    """
    是否可选中，默认值为 True
    """

    selected_keys: List[Any] = []
    """
    （受控）设置选中的树节点，默认值为 []
    """

    show_icon: bool = False
    """
    是否展示 TreeNode title 前的图标，没有默认样式，
            如设置为 true，需要自行定义图标相关样式，默认值为 False
    """

    show_line: bool = False
    """
    是否展示连接线，默认值为 False
    """

    switcher_icon: Optional[Any] = None
    """
    自定义树节点的展开/折叠图标，默认值为 None
    """

    tree_data: List[TreeData] = []
    """
    treeNodes 数据，如果设置则不需要手动构造 TreeNode 节点，默认值为 []
    """

    value: Optional[Any] = None
    """
    指定当前选中的条目，多选时为一个数组，默认值为 None
    """

    virtual: bool = True
    """
    设置 false 时关闭虚拟滚动，默认值为 True
    """

    style: Optional[Dict[str, Any]] = None
    """
    自定义样式，默认值为 None
    """

    def get_options(self) -> List[TreeData]:
        """
        获取当前可选项。

        Returns:
            List[TreeData]: 当前可选项列表。
        """
        return self.tree_data

    def set_auto_expand_parent(self, auto_expand_parent: bool):
        """
        设置是否自动展开父节点。

        Args:
            auto_expand_parent (bool): 是否自动展开父节点。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.auto_expand_parent = auto_expand_parent
        return self

    def set_block_node(self, block_node: bool):
        """
        设置是否节点占据一行。

        Args:
            block_node (bool): 是否节点占据一行。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.block_node = block_node
        return self

    def set_checkable(self, checkable: bool):
        """
        设置节点前是否添加 Checkbox 复选框。

        Args:
            checkable (bool): 是否添加复选框。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.checkable = checkable
        return self

    def set_checked_keys(self, checked_keys: List[Any]):
        """
        设置（受控）选中复选框的树节点。

        Args:
            checked_keys (List[Any]): 选中的树节点 key 列表。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.checked_keys = checked_keys
        return self

    def set_check_strictly(self, check_strictly: bool):
        """
        设置 checkable 状态下节点选择是否完全受控。

        Args:
            check_strictly (bool): 是否完全受控。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.check_strictly = check_strictly
        return self

    def set_default_checked_keys(self, default_checked_keys: List[Any]):
        """
        设置默认选中复选框的树节点。

        Args:
            default_checked_keys (List[Any]): 默认选中的树节点 key 列表。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.default_checked_keys = default_checked_keys
        return self

    def set_default_expand_all(self, default_expand_all: bool):
        """
        设置默认是否展开所有树节点。

        Args:
            default_expand_all (bool): 是否展开所有树节点。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.default_expand_all = default_expand_all
        return self

    def set_default_expanded_keys(self, default_expanded_keys: List[Any]):
        """
        设置默认展开指定的树节点。

        Args:
            default_expanded_keys (List[Any]): 默认展开的树节点 key 列表。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.default_expanded_keys = default_expanded_keys
        return self

    def set_default_expand_parent(self, default_expand_parent: bool):
        """
        设置默认是否展开父节点。

        Args:
            default_expand_parent (bool): 是否展开父节点。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.default_expand_parent = default_expand_parent
        return self

    def set_default_selected_keys(self, default_selected_keys: List[Any]):
        """
        设置默认选中的树节点。

        Args:
            default_selected_keys (List[Any]): 默认选中的树节点 key 列表。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.default_selected_keys = default_selected_keys
        return self

    def set_draggable(self, draggable: bool):
        """
        设置节点是否可拖拽。

        Args:
            draggable (bool): 是否可拖拽。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.draggable = draggable
        return self

    def set_expanded_keys(self, expanded_keys: List[Any]):
        """
        设置（受控）展开指定的树节点。

        Args:
            expanded_keys (List[Any]): 展开的树节点 key 列表。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.expanded_keys = expanded_keys
        return self

    def set_field_names(self, field_names: Optional[FieldNames]):
        """
        设置自定义 options 中 label value children 的字段。

        Args:
            field_names (Optional[FieldNames]): 字段名映射对象。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.field_names = field_names
        return self

    def set_height(self, height: int):
        """
        设置虚拟滚动容器高度。

        Args:
            height (int): 容器高度。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.height = height
        return self

    def set_icon(self, icon: Any):
        """
        设置自定义树节点图标。

        Args:
            icon (Any): 树节点图标。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.icon = icon
        return self

    def set_multiple(self, multiple: bool):
        """
        设置是否支持点选多个节点。

        Args:
            multiple (bool): 是否支持多选。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.multiple = multiple
        return self

    def set_placeholder(self, placeholder: str):
        """
        设置占位文本。

        Args:
            placeholder (str): 占位文本内容。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.placeholder = placeholder
        return self

    def set_root_class_name(self, root_class_name: str):
        """
        设置添加在 Tree 最外层的 className。

        Args:
            root_class_name (str): className 名称。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.root_class_name = root_class_name
        return self

    def set_root_style(self, root_style: Any):
        """
        设置添加在 Tree 最外层的 style。

        Args:
            root_style (Any): 样式信息。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.root_style = root_style
        return self

    def set_selectable(self, selectable: bool):
        """
        设置节点是否可选中。

        Args:
            selectable (bool): 是否可选中。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.selectable = selectable
        return self

    def set_selected_keys(self, selected_keys: List[Any]):
        """
        设置（受控）选中的树节点。

        Args:
            selected_keys (List[Any]): 选中的树节点 key 列表。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.selected_keys = selected_keys
        return self

    def set_show_icon(self, show_icon: bool):
        """
        设置是否展示 TreeNode title 前的图标。

        Args:
            show_icon (bool): 是否展示图标。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.show_icon = show_icon
        return self

    def set_show_line(self, show_line: bool):
        """
        设置是否展示连接线。

        Args:
            show_line (bool): 是否展示连接线。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.show_line = show_line
        return self

    def set_switcher_icon(self, switcher_icon: Any):
        """
        设置自定义树节点的展开/折叠图标。

        Args:
            switcher_icon (Any): 展开/折叠图标。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.switcher_icon = switcher_icon
        return self

    def build_tree(
        self, items: Any, pid: int, parent_key_name: str, key_name: str, title_name: str
    ) -> List[TreeData]:
        """
        使用反射构建树结构。

        Args:
            items (Any): 包含树节点数据的对象。
            pid (int): 父节点 ID。
            parent_key_name (str): 父节点键名。
            key_name (str): 节点键名。
            title_name (str): 节点标题名。

        Returns:
            List[TreeData]: 构建好的树节点数据列表。
        """
        tree = []

        for item in items:
            # 支持对象和字典两种格式
            if hasattr(item, key_name):
                key = getattr(item, key_name)
                parent_key = getattr(item, parent_key_name)
                title = getattr(item, title_name)
            elif isinstance(item, dict):
                key = item.get(key_name)
                parent_key = item.get(parent_key_name)
                title = item.get(title_name)
            else:
                # 如果既不是对象也不是字典，跳过该项
                continue

            if parent_key == pid:
                children = self.build_tree(
                    items, key, parent_key_name, key_name, title_name
                )
                option = TreeData(title=title, key=key, children=children)
                tree.append(option)

        return tree

    def list_to_tree_data(
        self,
        list_: Any,
        root_id: int,
        parent_key_name: str,
        key_name: str,
        title_name: str,
    ) -> List[TreeData]:
        """
        将列表转换为树节点数据。

        Args:
            list_ (Any): 包含树节点数据的列表。
            root_id (int): 根节点 ID。
            parent_key_name (str): 父节点键名。
            key_name (str): 节点键名。
            title_name (str): 节点标题名。

        Returns:
            List[TreeData]: 转换后的树节点数据列表。
        """
        return self.build_tree(list_, root_id, parent_key_name, key_name, title_name)

    def set_tree_data(self, *tree_data: Any):
        """
        设置可选项数据源。

        Args:
            *tree_data: 可变参数，不同数量有不同含义。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        if len(tree_data) == 1:
            if isinstance(tree_data[0], list) and all(
                isinstance(item, TreeData) for item in tree_data[0]
            ):
                self.tree_data = tree_data[0]
        elif len(tree_data) == 4:
            self.tree_data = self.list_to_tree_data(
                tree_data[0], 0, tree_data[1], tree_data[2], tree_data[3]
            )
        elif len(tree_data) == 5:
            self.tree_data = self.list_to_tree_data(
                tree_data[0], tree_data[1], tree_data[2], tree_data[3], tree_data[4]
            )
        return self

    def set_style(self, style: Dict[str, Any]):
        """
        设置自定义样式。

        Args:
            style (Dict[str, Any]): 样式字典。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.style = style
        return self

    def set_default_value(self, default_value: Any):
        self.default_value = default_value
        return self

    def set_value(self, value: Any):
        self.value = value
        return self
