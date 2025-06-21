from typing import Dict, List, Optional, Any
from .base import Base


class Option(Base):
    """
    表示搜索组件选项的类。

    Attributes:
        label (str): 选项显示的标签。
        value (Any): 选项对应的值。
        disabled (bool): 选项是否禁用，默认为 False。
    """

    label: str
    value: Any
    disabled: bool = False


class Search(Base):

    component: str = "searchField"
    """
    组件名称
    """

    allow_clear: bool = True
    """
    可以点击清除图标删除内容，默认值为 True
    """

    placeholder: str = "请输入要搜索的内容"
    """
    占位符，默认值为 "请输入要搜索的内容"
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
    用于设置 Search options 类型 default | button
    """

    size: Optional[str] = None
    """
    大小，只对按钮样式生效, large | middle | small
    """

    value: Optional[Any] = None
    """
    指定选中项
    """

    style: Dict[str, Any] = {}
    """
    自定义样式，默认值为空字典
    """

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

    def set_option_type(self, option_type: str):
        """
        设置 Search options 类型。

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
