from typing import Dict, Optional, Any
from .base import Base


class Option(Base):
    """
    表示 Switch 组件选项的类，包含选中和未选中时的内容。

    Attributes:
        checked_children (Any): 选中时的内容。
        un_checked_children (Any): 未选中时的内容。
    """

    checked_children: Any = None
    un_checked_children: Any = None


class Switch(Base):

    component: str = "switchField"
    """
    组件名称
    """

    auto_focus: bool = False
    """
    默认获取焦点，默认值为 False
    """

    checked: bool = False
    """
    指定当前是否选中，默认值为 False
    """

    checked_children: Optional[Any] = None
    """
    选中时的内容
    """

    class_name: Optional[str] = None
    """
    Switch 器类名
    """

    default_checked: bool = False
    """
    初始是否选中，默认值为 False
    """

    default_value: Optional[Any] = None
    """
    默认选中的选项
    """

    disabled: bool = False
    """
    整组失效，默认值为 False
    """

    loading: bool = False
    """
    加载中状态，默认值为 False
    """

    size: Optional[str] = None
    """
    选择框大小
    """

    un_checked_children: Optional[Any] = None
    """
    自定义的选择框后缀图标
    """

    value: Optional[Any] = None
    """
    值
    """

    def get_options(self) -> Dict[int, Any]:
        """
        获取当前可选项。

        Returns:
            Dict[int, Any]: 可选项字典。
        """
        data: Dict[int, Any] = {0: self.un_checked_children, 1: self.checked_children}
        return data

    def set_options(self, options: Option):
        """
        设置选项。

        Args:
            options (Option): 选项对象。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.checked_children = options.checked_children
        self.un_checked_children = options.un_checked_children
        return self

    def set_auto_focus(self, auto_focus: bool):
        """
        设置默认获取焦点。

        Args:
            auto_focus (bool): 是否默认获取焦点。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.auto_focus = auto_focus
        return self

    def set_checked(self, checked: bool):
        """
        指定当前是否选中。

        Args:
            checked (bool): 是否选中。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.checked = checked
        return self

    def set_checked_children(self, checked_children: Any):
        """
        设置选中时的内容。

        Args:
            checked_children (Any): 选中时的内容。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.checked_children = checked_children
        return self

    def set_class_name(self, class_name: str):
        """
        设置 Switch 器类名。

        Args:
            class_name (str): 类名。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.class_name = class_name
        return self

    def set_default_checked(self, default_checked: bool):
        """
        设置初始是否选中。

        Args:
            default_checked (bool): 初始是否选中。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.default_checked = default_checked
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

    def set_size(self, size: str):
        """
        设置选择框大小。

        Args:
            size (str): 选择框大小。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.size = size
        return self

    def set_un_checked_children(self, un_checked_children: Any):
        """
        设置非选中时的内容。

        Args:
            un_checked_children (Any): 非选中时的内容。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.un_checked_children = un_checked_children
        return self

    def set_true_value(self, value: Any):
        """
        设置选中时的内容。

        Args:
            value (Any): 选中时的内容。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.checked_children = value
        return self

    def set_false_value(self, value: Any):
        """
        设置非选中时的内容。

        Args:
            value (Any): 非选中时的内容。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.un_checked_children = value
        return self

    def set_default_value(self, default_value: Any):
        self.default_value = default_value
        return self

    def set_value(self, value: Any):
        self.value = value
        return self

    def get_value_enum(self) -> Dict[int, Any]:
        """
        获取当前列值的枚举 value_enum。

        Returns:
            Dict[int, Any]: 列值枚举字典。
        """
        data: Dict[int, Any] = {0: self.un_checked_children, 1: self.checked_children}
        return data

    def get_option_label(self, value: Any) -> Any:
        """
        根据 value 值获取 Option 的 Label。

        Args:
            value (Any): 值。

        Returns:
            Any: Option 的 Label。
        """
        if value == 1:
            return self.checked_children
        else:
            return self.un_checked_children

    def get_option_value(self, label: str) -> bool:
        """
        根据 label 值获取 Option 的 Value。

        Args:
            label (str): 标签。

        Returns:
            bool: Option 的 Value。
        """
        return self.checked_children == label

    def get_option_labels(self) -> str:
        """
        获取 Option 的 Labels。

        Returns:
            str: Option 的 Labels 字符串。
        """
        label_string = ""
        if isinstance(self.checked_children, str) and isinstance(
            self.un_checked_children, str
        ):
            label_string = f"{self.checked_children},{self.un_checked_children}"
        return label_string.strip(",")
