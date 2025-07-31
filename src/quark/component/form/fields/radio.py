import json
from typing import Dict, List, Optional, Any
from .base import Base


class Option(Base):
    """
    表示单选按钮选项的类。

    Attributes:
        label (str): 选项显示的标签。
        value (Any): 选项对应的值。
        disabled (bool): 选项是否禁用，默认为 False。
    """

    label: str
    value: Any
    disabled: bool = False


class Radio(Base):

    component: str = "radioField"
    """
    组件名称
    """

    button_style: Optional[Any] = None
    """
    RadioButton 的风格样式，目前有描边和填色两种风格 outline | solid
    """

    default_value: Optional[Any] = None
    """
    默认选中的选项
    """

    disabled: bool = False
    """
    整组失效，默认值为 False
    """

    options: List[Option] = []
    """
    可选项数据源
    """

    option_type: Optional[str] = None
    """
    用于设置 Radio options 类型 default | button
    """

    size: Optional[str] = None
    """
    大小，只对按钮样式生效, large | middle | small
    """

    value: Optional[Any] = None
    """
    指定选中项
    """

    def get_options(self) -> List[Option]:
        """
        获取当前可选项。

        Returns:
            List[Option]: 可选项列表。
        """
        return self.options

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
            if isinstance(options[0], list) and all(
                isinstance(option, Option) for option in options[0]
            ):
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

    def set_button_style(self, button_style: Any):
        """
        设置 RadioButton 的风格样式。

        Args:
            button_style (Any): 风格样式信息。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.button_style = button_style
        return self

    def set_option_type(self, option_type: str):
        """
        设置 Radio options 类型。

        Args:
            option_type (str): 类型，如 'default', 'button'。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.option_type = option_type
        return self

    def set_size(self, size: str):
        """
        设置控件大小。

        Args:
            size (str): 大小，如 'large', 'middle', 'small'。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.size = size
        return self

    def set_default_value(self, default_value: Any):
        self.default_value = default_value
        return self

    def set_value(self, value: Any):
        self.value = value
        return self

    def get_value_enum(self) -> Dict[Any, Any]:
        """
        获取当前列值的枚举 valueEnum。

        Returns:
            Dict[Any, Any]: 列值枚举字典。
        """
        data: Dict[Any, Any] = {}
        for v in self.options:
            data[v.value] = v.label
        return data

    def get_option_label(self, value: Any) -> str:
        """
        根据 value 值获取 Option 的 Label。

        Args:
            value (Any): 要查找的 value 值。

        Returns:
            str: 对应的 Label 字符串。
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

    def get_option_value(self, label: str) -> Any:
        """
        根据 label 值获取 Option 的 Value。

        Args:
            label (str): 要查找的 label 值。

        Returns:
            Any: 对应的 Value。
        """
        values: List[Any] = []
        get_labels = label.split(",")
        if len(get_labels) == 1:
            get_labels = label.split("，")

        if len(get_labels) > 1:
            for v in self.options:
                for get_label in get_labels:
                    if v.label == get_label:
                        values.append(v.value)
        else:
            for v in self.options:
                if v.label == label:
                    return v.value

        return values

    def get_option_labels(self) -> str:
        """
        获取 Option 的 Labels。

        Returns:
            str: 所有 Option 的 Label 组成的字符串。
        """
        labels = [option.label for option in self.options]
        return ",".join(labels)
