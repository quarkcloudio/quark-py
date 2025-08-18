from typing import Any, Dict, List, Optional

from .base import Base


class DataSource(Base):
    """
    表示 Transfer 组件数据源的类。

    Attributes:
        key (Any): 数据源项的主键。
        title (str): 数据源项的标题。
        description (str): 数据源项的描述信息。
        disabled (bool): 数据源项是否禁用，默认为 False。
    """

    key: Any = None
    title: Optional[str] = None
    description: Optional[str] = None
    disabled: bool = False


class Transfer(Base):

    component: str = "transferField"
    """
    组件名称
    """

    data_source: List[DataSource] = []
    """
    数据源，其中的数据将会被渲染到左边一栏中，target_keys 中指定的除外
    """

    disabled: bool = False
    """
    是否禁用，默认值为 False
    """

    selections_icon: Optional[Any] = None
    """
    自定义下拉菜单图标
    """

    filter_option: Optional[Any] = None
    """
    根据搜索内容进行筛选，接收 inputValue option 两个参数，
            当 option 符合筛选条件时，应返回 true，反之则返回 false
    """

    footer: Optional[Any] = None
    """
    底部渲染函数
    """

    list_style: Optional[Dict[str, Any]] = None
    """
    两个穿梭框的自定义样式
    """

    locale: Optional[Dict[str, str]] = None
    """
    各种语言,{ itemUnit: 项, itemsUnit: 项, searchPlaceholder: 请输入搜索内容 }
    """

    one_way: bool = False
    """
    展示为单向样式，默认值为 False
    """

    operations: List[str] = []
    """
    操作文案集合，顺序从上至下
    """

    operation_style: Optional[Dict[str, Any]] = None
    """
    操作栏的自定义样式
    """

    pagination: Optional[Any] = None
    """
    使用分页样式，自定义渲染列表下无效
    """

    select_all_labels: Optional[Any] = None
    """
    自定义顶部多选框标题的集合
    """

    selected_keys: List[str] = []
    """
    设置哪些项应该被选中
    """

    show_search: bool = False
    """
    是否显示搜索框，默认值为 False
    """

    show_select_all: bool = False
    """
    是否展示全选勾选框，默认值为 False
    """

    status: Optional[str] = None
    """
    设置校验状态,'error' | 'warning'
    """

    target_keys: List[str] = []
    """
    显示在右侧框数据的 key 集合
    """

    titles: List[str] = []
    """
    标题集合，顺序从左至右
    """

    style: Optional[Dict[str, Any]] = None
    """
    自定义样式
    """

    default_value: Optional[Any] = None
    """
    默认的选中项
    """

    value: Optional[Any] = None
    """
    指定选中项
    """

    def build_data_source(
        self, items: Any, key_name: str, title_name: str, description_name: str
    ) -> List[DataSource]:
        """
        使用反射构建数据源。

        Args:
            items (Any): 包含数据源的对象。
            key_name (str): 主键字段名。
            title_name (str): 标题字段名。
            description_name (str): 描述字段名。

        Returns:
            List[DataSource]: 构建好的数据源列表。
        """
        options: List[DataSource] = []

        if not isinstance(items, list):
            return options

        for item in items:
            if isinstance(item, dict):
                key = item.get(key_name)
                title = item.get(title_name, "")
                description = item.get(description_name, "")
            else:
                key = getattr(item, key_name, None)
                title = getattr(item, title_name, "")
                description = getattr(item, description_name, "")

            if key is not None and title:
                option = DataSource(key=key, title=title, description=description)
                options.append(option)

        return options

    def list_to_data_source(
        self, list_: Any, key_name: str, title_name: str, description_name: str
    ) -> List[DataSource]:
        """
        将列表转换为数据源。

        Args:
            list_ (Any): 包含数据的列表。
            key_name (str): 主键字段名。
            title_name (str): 标题字段名。
            description_name (str): 描述字段名。

        Returns:
            List[DataSource]: 转换后的数据源列表。
        """
        return self.build_data_source(list_, key_name, title_name, description_name)

    def set_data_source(self, *data_source: Any):
        """
        设置数据源。

        Args:
            *data_source: 可变参数，不同数量有不同含义。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        if len(data_source) == 1:
            if isinstance(data_source[0], list) and all(
                isinstance(item, DataSource) for item in data_source[0]
            ):
                self.data_source = data_source[0]
        elif len(data_source) == 4:
            self.data_source = self.list_to_data_source(
                data_source[0], data_source[1], data_source[2], data_source[3]
            )
        return self

    def set_selections_icon(self, selections_icon: Any):
        """
        设置自定义下拉菜单图标。

        Args:
            selections_icon (Any): 下拉菜单图标。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.selections_icon = selections_icon
        return self

    def set_filter_option(self, filter_option: Any):
        """
        设置根据搜索内容进行筛选的函数。

        Args:
            filter_option (Any): 筛选函数。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.filter_option = filter_option
        return self

    def set_footer(self, footer: Any):
        """
        设置底部渲染函数。

        Args:
            footer (Any): 底部渲染函数。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.footer = footer
        return self

    def set_list_style(self, list_style: Dict[str, Any]):
        """
        设置两个穿梭框的自定义样式。

        Args:
            list_style (Dict[str, Any]): 样式字典。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.list_style = list_style
        return self

    def set_locale(self, locale: Dict[str, str]):
        """
        设置各种语言配置。

        Args:
            locale (Dict[str, str]): 语言配置字典。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.locale = locale
        return self

    def set_one_way(self, one_way: bool):
        """
        设置展示为单向样式。

        Args:
            one_way (bool): 是否展示为单向样式。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.one_way = one_way
        return self

    def set_operations(self, operations: List[str]):
        """
        设置操作文案集合。

        Args:
            operations (List[str]): 操作文案列表。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.operations = operations
        return self

    def set_operation_style(self, operation_style: Dict[str, Any]):
        """
        设置操作栏的自定义样式。

        Args:
            operation_style (Dict[str, Any]): 样式字典。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.operation_style = operation_style
        return self

    def set_pagination(self, pagination: Any):
        """
        设置使用分页样式。

        Args:
            pagination (Any): 分页样式配置。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.pagination = pagination
        return self

    def set_select_all_labels(self, select_all_labels: Any):
        """
        设置自定义顶部多选框标题的集合。

        Args:
            select_all_labels (Any): 多选框标题集合。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.select_all_labels = select_all_labels
        return self

    def set_selected_keys(self, selected_keys: List[str]):
        """
        设置哪些项应该被选中。

        Args:
            selected_keys (List[str]): 选中项的 key 列表。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.selected_keys = selected_keys
        return self

    def set_show_search(self, show_search: bool):
        """
        设置是否显示搜索框。

        Args:
            show_search (bool): 是否显示搜索框。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.show_search = show_search
        return self

    def set_show_select_all(self, show_select_all: bool):
        """
        设置是否展示全选勾选框。

        Args:
            show_select_all (bool): 是否展示全选勾选框。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.show_select_all = show_select_all
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

    def set_target_keys(self, target_keys: List[str]):
        """
        设置显示在右侧框数据的 key 集合。

        Args:
            target_keys (List[str]): key 集合。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.target_keys = target_keys
        return self

    def set_titles(self, titles: List[str]):
        """
        设置标题集合。

        Args:
            titles (List[str]): 标题列表。

        Returns:
            Component: 返回当前实例，支持链式调用。
        """
        self.titles = titles
        return self

    def set_default_value(self, default_value: Any):
        self.default_value = default_value
        return self

    def set_value(self, value: Any):
        self.value = value
        return self
