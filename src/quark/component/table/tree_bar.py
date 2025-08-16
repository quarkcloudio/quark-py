from pydantic import Field, model_validator
from typing import Any, List, Optional, Union
from ..component import Component


class FieldNames(Component):
    """
    定义树节点字段名称的结构。

    Attributes:
        title (str): 树节点的标题字段名称。
        key (str): 树节点的键字段名称。
        children (str): 树节点的子节点字段名称。
    """

    title: str
    key: str
    children: str


class TreeData(Component):
    """
    定义树节点的数据结构。

    Attributes:
        title (str): 树节点的标题。
        key (Any): 树节点的键，用于标识节点。
        children (List['TreeData']): 子节点列表。
        checkable (Optional[bool]): 是否可选中复选框。
        disable_checkbox (Optional[bool]): 是否禁用复选框。
        disabled (Optional[bool]): 是否禁用节点。
        icon (Optional[Any]): 自定义图标。
        is_leaf (Optional[bool]): 是否为叶子节点。
        selectable (Optional[bool]): 是否可选中节点。
    """

    title: Any
    key: Any
    children: List["TreeData"] = Field(default_factory=list)
    checkable: Optional[bool] = None
    disable_checkbox: Optional[bool] = None
    disabled: Optional[bool] = None
    icon: Optional[Any] = None
    is_leaf: Optional[bool] = None
    selectable: Optional[bool] = None


class TreeBar(Component):
    """
    定义树形组件的数据结构和操作方法。

    Attributes:
        component (str): 组件名称。
        name (str): 字段名，支持数组。
        auto_expand_parent (bool): 是否自动展开父节点。
        block_node (bool): 是否节点占据一行。
        checkable (bool): 是否节点前添加 Checkbox 复选框。
        checked_keys (List[Any]): 受控选中复选框的树节点。
        check_strictly (bool): checkable 状态下节点选择完全受控。
        default_checked_keys (List[Any]): 默认选中复选框的树节点。
        default_expand_all (bool): 默认展开所有树节点。
        default_expanded_keys (List[Any]): 默认展开指定的树节点。
        default_expand_parent (bool): 默认展开父节点。
        default_selected_keys (List[Any]): 默认选中的树节点。
        default_value (Optional[Any]): 默认选中的选项。
        disabled (bool): 整组失效。
        draggable (bool): 设置节点可拖拽。
        expanded_keys (List[Any]): 受控展开指定的树节点。
        field_names (Optional[FieldNames]): 自定义 options 中 label value children 的字段。
        height (Optional[int]): 设置虚拟滚动容器高度。
        icon (Optional[Any]): 自定义树节点图标。
        multiple (bool): 支持点选多个节点。
        placeholder (str): 占位文本。
        root_class_name (Optional[str]): 添加在 Tree 最外层的 className。
        root_style (Optional[Any]): 添加在 Tree 最外层的 style。
        selectable (bool): 是否可选中。
        selected_keys (List[Any]): 受控设置选中的树节点。
        show_icon (bool): 是否展示 TreeNode title 前的图标。
        show_line (bool): 是否展示连接线。
        switcher_icon (Optional[Any]): 自定义树节点的展开/折叠图标。
        tree_data (List[TreeData]): treeNodes 数据。
        value (Optional[Any]): 指定当前选中的条目。
        virtual (bool): 设置 false 时关闭虚拟滚动。
        style (dict): 自定义样式。
    """

    component: str = "treeBar"
    name: str = "treeBarSelectedKeys"
    auto_expand_parent: bool = False
    block_node: bool = False
    checkable: bool = False
    checked_keys: Optional[List[Any]] = None
    check_strictly: bool = False
    default_checked_keys: Optional[List[Any]] = None
    default_expand_all: bool = True
    default_expanded_keys: Optional[List[Any]] = None
    default_expand_parent: bool = False
    default_selected_keys: Optional[List[Any]] = None
    default_value: Optional[Any] = None
    disabled: bool = False
    draggable: bool = False
    expanded_keys: Optional[List[Any]]= None
    field_names: Optional[FieldNames] = None
    height: Optional[int] = None
    icon: Optional[Any] = None
    multiple: bool = False
    placeholder: str = "请输入搜索内容"
    root_class_name: Optional[str] = None
    root_style: Optional[Any] = None
    selectable: bool = True
    selected_keys: Optional[List[Any]] = None
    show_icon: bool = False
    show_line: bool = True
    switcher_icon: Optional[Any] = None
    tree_data: Optional[List[TreeData]] = None
    value: Optional[Any] = None
    virtual: bool = False
    style: dict = Field(default_factory=dict)

    @model_validator(mode="after")
    def init(self):
        self.set_key()
        return self

    # 设置方法（链式调用）
    def set_name(self, name: str):
        """
        设置字段名。

        Args:
            name (str): 字段名。

        Returns:
            TreeBar: 当前实例。
        """
        self.name = name
        return self

    def set_width(self, width: Union[str, int]):
        """
        设置宽度。

        Args:
            width (Union[str, int]): 宽度值。

        Returns:
            TreeBar: 当前实例。
        """
        self.style["width"] = width
        return self

    def set_auto_expand_parent(self, auto_expand_parent: bool):
        """
        设置是否自动展开父节点。

        Args:
            auto_expand_parent (bool): 是否自动展开父节点。

        Returns:
            TreeBar: 当前实例。
        """
        self.auto_expand_parent = auto_expand_parent
        return self

    def set_block_node(self, block_node: bool):
        """
        设置是否节点占据一行。

        Args:
            block_node (bool): 是否节点占据一行。

        Returns:
            TreeBar: 当前实例。
        """
        self.block_node = block_node
        return self

    def set_checkable(self, checkable: bool):
        """
        设置是否节点前添加 Checkbox 复选框。

        Args:
            checkable (bool): 是否节点前添加 Checkbox 复选框。

        Returns:
            TreeBar: 当前实例。
        """
        self.checkable = checkable
        return self

    def set_checked_keys(self, checked_keys: List[Any]):
        """
        设置受控选中复选框的树节点。

        Args:
            checked_keys (List[Any]): 受控选中复选框的树节点。

        Returns:
            TreeBar: 当前实例。
        """
        self.checked_keys = checked_keys
        return self

    def set_check_strictly(self, check_strictly: bool):
        """
        设置 checkable 状态下节点选择完全受控。

        Args:
            check_strictly (bool): 是否 checkable 状态下节点选择完全受控。

        Returns:
            TreeBar: 当前实例。
        """
        self.check_strictly = check_strictly
        return self

    def set_default_checked_keys(self, default_checked_keys: List[Any]):
        """
        设置默认选中复选框的树节点。

        Args:
            default_checked_keys (List[Any]): 默认选中复选框的树节点。

        Returns:
            TreeBar: 当前实例。
        """
        self.default_checked_keys = default_checked_keys
        return self

    def set_default_expand_all(self, default_expand_all: bool):
        """
        设置默认展开所有树节点。

        Args:
            default_expand_all (bool): 是否默认展开所有树节点。

        Returns:
            TreeBar: 当前实例。
        """
        self.default_expand_all = default_expand_all
        return self

    def set_default_expanded_keys(self, default_expanded_keys: List[Any]):
        """
        设置默认展开指定的树节点。

        Args:
            default_expanded_keys (List[Any]): 默认展开指定的树节点。

        Returns:
            TreeBar: 当前实例。
        """
        self.default_expanded_keys = default_expanded_keys
        return self

    def set_default_expand_parent(self, default_expand_parent: bool):
        """
        设置默认展开父节点。

        Args:
            default_expand_parent (bool): 是否默认展开父节点。

        Returns:
            TreeBar: 当前实例。
        """
        self.default_expand_parent = default_expand_parent
        return self

    def set_default_selected_keys(self, default_selected_keys: List[Any]):
        """
        设置默认选中的树节点。

        Args:
            default_selected_keys (List[Any]): 默认选中的树节点。

        Returns:
            TreeBar: 当前实例。
        """
        self.default_selected_keys = default_selected_keys
        return self

    def set_draggable(self, draggable: bool):
        """
        设置是否节点可拖拽。

        Args:
            draggable (bool): 是否节点可拖拽。

        Returns:
            TreeBar: 当前实例。
        """
        self.draggable = draggable
        return self

    def set_expanded_keys(self, expanded_keys: List[Any]):
        """
        设置受控展开指定的树节点。

        Args:
            expanded_keys (List[Any]): 受控展开指定的树节点。

        Returns:
            TreeBar: 当前实例。
        """
        self.expanded_keys = expanded_keys
        return self

    def set_field_names(self, field_names: FieldNames):
        """
        设置自定义 options 中 label value children 的字段。

        Args:
            field_names (FieldNames): 自定义字段名称。

        Returns:
            TreeBar: 当前实例。
        """
        self.field_names = field_names
        return self

    def set_height(self, height: int):
        """
        设置虚拟滚动容器高度。

        Args:
            height (int): 高度值。

        Returns:
            TreeBar: 当前实例。
        """
        self.height = height
        return self

    def set_icon(self, icon: Any):
        """
        设置自定义树节点图标。

        Args:
            icon (Any): 图标。

        Returns:
            TreeBar: 当前实例。
        """
        self.icon = icon
        return self

    def set_multiple(self, multiple: bool):
        """
        设置是否支持点选多个节点。

        Args:
            multiple (bool): 是否支持点选多个节点。

        Returns:
            TreeBar: 当前实例。
        """
        self.multiple = multiple
        return self

    def set_placeholder(self, placeholder: str):
        """
        设置占位文本。

        Args:
            placeholder (str): 占位文本。

        Returns:
            TreeBar: 当前实例。
        """
        self.placeholder = placeholder
        return self

    def set_root_class_name(self, root_class_name: str):
        """
        设置添加在 Tree 最外层的 className。

        Args:
            root_class_name (str): className。

        Returns:
            TreeBar: 当前实例。
        """
        self.root_class_name = root_class_name
        return self

    def set_root_style(self, root_style: Any):
        """
        设置添加在 Tree 最外层的 style。

        Args:
            root_style (Any): style。

        Returns:
            TreeBar: 当前实例。
        """
        self.root_style = root_style
        return self

    def set_selectable(self, selectable: bool):
        """
        设置是否可选中。

        Args:
            selectable (bool): 是否可选中。

        Returns:
            TreeBar: 当前实例。
        """
        self.selectable = selectable
        return self

    def set_selected_keys(self, selected_keys: List[Any]):
        """
        设置受控选中的树节点。

        Args:
            selected_keys (List[Any]): 受控选中的树节点。

        Returns:
            TreeBar: 当前实例。
        """
        self.selected_keys = selected_keys
        return self

    def set_show_icon(self, show_icon: bool):
        """
        设置是否展示 TreeNode title 前的图标。

        Args:
            show_icon (bool): 是否展示图标。

        Returns:
            TreeBar: 当前实例。
        """
        self.show_icon = show_icon
        return self

    def set_show_line(self, show_line: bool):
        """
        设置是否展示连接线。

        Args:
            show_line (bool): 是否展示连接线。

        Returns:
            TreeBar: 当前实例。
        """
        self.show_line = show_line
        return self

    def set_switcher_icon(self, switcher_icon: Any):
        """
        设置自定义树节点的展开/折叠图标。

        Args:
            switcher_icon (Any): 展开/折叠图标。

        Returns:
            TreeBar: 当前实例。
        """
        self.switcher_icon = switcher_icon
        return self

    def build_tree(
        self,
        items: Any,
        pid: Any,
        parent_key_name: str,
        key_name: str,
        title_name: str,
    ) -> List[TreeData]:
        """
        使用递归构建树结构。

        Args:
            items (Any): 树节点数据列表。
            pid (int): 父节点 ID。
            parent_key_name (str): 父节点键名称。
            key_name (str): 节点键名称。
            title_name (str): 节点标题名称。

        Returns:
            List[TreeData]: 树结构数据列表。
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
        list_data: Any,
        root_id: int,
        parent_key_name: str,
        key_name: str,
        title_name: str,
    ) -> List[TreeData]:
        """
        将列表数据转换为树结构数据。

        Args:
            list_data (Any): 列表数据。
            root_id (int): 根节点 ID。
            parent_key_name (str): 父节点键名称。
            key_name (str): 节点键名称。
            title_name (str): 节点标题名称。

        Returns:
            List[TreeData]: 树结构数据列表。
        """
        return self.build_tree(
            list_data, root_id, parent_key_name, key_name, title_name
        )

    def set_tree_data(self, *tree_data: Any):
        """
        设置树节点数据。

        Args:
            tree_data (Union[List[TreeData], int, str]): 树节点数据。

        Returns:
            TreeBar: 当前实例。
        """
        if len(tree_data) == 1 and isinstance(tree_data[0], list):
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

    def set_style(self, style: dict):
        """
        设置自定义样式。

        Args:
            style (dict): 样式字典。

        Returns:
            TreeBar: 当前实例。
        """
        self.style = style
        return self
