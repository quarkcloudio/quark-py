from ..component import Component
from typing import Any, Optional

class Item(Component):
    """
    表示下拉框中的一个项，包含了各种自定义选项，如标签、操作类型、模态框、抽屉、API 操作和加载状态等。
    """
    component: str = "itemStyle"
    label: str  # 标签
    block: bool = False  # 是否为块级元素
    danger: bool = False  # 是否为危险按钮
    disabled: bool = False  # 是否禁用按钮
    ghost: bool = False  # 是否为幽灵按钮
    icon: str = ""  # 图标
    shape: Optional[str] = None  # 按钮形状，可选值为 "circle"、"round" 或 None
    size: Optional[str] = None  # 按钮大小，可选值为 "large"、"middle"、"small" 或 None
    type: Optional[str] = None  # 按钮类型
    action_type: Optional[str] = None  # 操作类型，例如 "ajax"、"link"
    submit_form: Optional[Any] = None  # 提交的表单 key
    href: Optional[str] = None  # 跳转的 URL
    target: Optional[str] = None  # 跳转的目标（例如 "_blank"）
    modal: Optional[Any] = None  # 模态框组件
    drawer: Optional[Any] = None  # 抽屉组件
    confirm_title: Optional[str] = None  # 确认框的标题
    confirm_text: Optional[str] = None  # 确认框的文本
    confirm_type: Optional[str] = None  # 确认框的类型
    api: Optional[str] = None  # 调用的 API 地址
    reload: Optional[str] = None  # 执行操作后需要刷新的组件
    with_loading: bool = False  # 是否显示加载状态

    def set_label(self, label: str) -> "Item":
        """
        设置按钮的标签。

        Args:
            label (str): 按钮的标签

        Returns:
            Item: 当前实例，标签已更新
        """
        self.label = label
        return self

    def set_block(self, block: bool) -> "Item":
        """
        设置按钮是否为块级元素（占满父容器宽度）。

        Args:
            block (bool): 是否为块级元素

        Returns:
            Item: 当前实例，块级设置已更新
        """
        self.block = block
        return self

    def set_danger(self, danger: bool) -> "Item":
        """
        设置按钮是否为危险按钮。

        Args:
            danger (bool): 是否为危险按钮

        Returns:
            Item: 当前实例，危险按钮设置已更新
        """
        self.danger = danger
        return self

    def set_disabled(self, disabled: bool) -> "Item":
        """
        设置按钮是否禁用。

        Args:
            disabled (bool): 是否禁用

        Returns:
            Item: 当前实例，禁用状态已更新
        """
        self.disabled = disabled
        return self

    def set_ghost(self, ghost: bool) -> "Item":
        """
        设置按钮是否为幽灵按钮（背景透明）。

        Args:
            ghost (bool): 是否为幽灵按钮

        Returns:
            Item: 当前实例，幽灵按钮设置已更新
        """
        self.ghost = ghost
        return self

    def set_icon(self, icon: str) -> "Item":
        """
        设置按钮的图标。

        Args:
            icon (str): 图标名称，例如 "edit"

        Returns:
            Item: 当前实例，图标已更新
        """
        self.icon = f"icon-{icon}"
        return self

    def set_shape(self, shape: str) -> "Item":
        """
        设置按钮的形状。

        Args:
            shape (str): 按钮形状，可能的值为 "circle" 或 "round"

        Returns:
            Item: 当前实例，形状已更新
        """
        self.shape = shape
        return self

    def set_size(self, size: str) -> "Item":
        """
        设置按钮的大小。

        Args:
            size (str): 按钮大小，可能的值为 "large"、"middle" 或 "small"

        Returns:
            Item: 当前实例，大小已更新
        """
        self.size = size
        return self

    def set_action_type(self, action_type: str) -> "Item":
        """
        设置按钮的操作类型（例如 "ajax"、"link"）。

        Args:
            action_type (str): 操作类型

        Returns:
            Item: 当前实例，操作类型已更新
        """
        self.action_type = action_type
        return self

    def set_submit_form(self, form_key: str) -> "Item":
        """
        设置提交的表单 key。

        Args:
            form_key (str): 表单的 key 值

        Returns:
            Item: 当前实例，表单提交设置已更新
        """
        self.submit_form = form_key
        return self

    def set_href(self, href: str) -> "Item":
        """
        设置按钮的跳转地址。

        Args:
            href (str): 跳转的 URL 地址

        Returns:
            Item: 当前实例，跳转地址已更新
        """
        self.href = href
        return self

    def set_target(self, target: str) -> "Item":
        """
        设置跳转链接的目标，类似 a 标签中的 target 属性。

        Args:
            target (str): 跳转目标，例如 "_blank" 打开新标签页

        Returns:
            Item: 当前实例，跳转目标已更新
        """
        self.target = target
        return self

    def set_modal(self, modal: Any) -> "Item":
        """
        设置与按钮关联的模态框。

        Args:
            modal (Any): 模态框组件或回调函数

        Returns:
            Item: 当前实例，模态框已设置
        """
        self.modal = modal
        return self

    def set_drawer(self, drawer: Any) -> "Item":
        """
        设置与按钮关联的抽屉。

        Args:
            drawer (Any): 抽屉组件或回调函数

        Returns:
            Item: 当前实例，抽屉已设置
        """
        self.drawer = drawer
        return self

    def set_with_confirm(self, title: str, text: str, confirm_type: str) -> "Item":
        """
        设置在执行操作前的确认对话框。

        Args:
            title (str): 确认对话框的标题
            text (str): 确认对话框的文本
            confirm_type (str): 确认框的类型（例如 "confirm"）

        Returns:
            Item: 当前实例，确认框已设置
        """
        self.confirm_title = title
        self.confirm_text = text
        self.confirm_type = confirm_type
        return self

    def set_api(self, api: str) -> "Item":
        """
        设置执行操作时调用的 API。

        Args:
            api (str): API 地址

        Returns:
            Item: 当前实例，API 已设置
        """
        self.api = api
        self.action_type = "ajax"  # 设置操作类型为 "ajax"
        return self

    def set_reload(self, reload: str) -> "Item":
        """
        设置执行操作后需要刷新的组件。

        Args:
            reload (str): 刷新的组件

        Returns:
            Item: 当前实例，刷新组件已设置
        """
        self.reload = reload
        return self

    def set_with_loading(self, loading: bool) -> "Item":
        """
        设置是否显示加载状态。

        Args:
            loading (bool): 是否显示加载状态

        Returns:
            Item: 当前实例，加载状态已更新
        """
        self.with_loading = loading
        return self
