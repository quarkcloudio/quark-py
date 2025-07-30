from pydantic import model_validator
from typing import Any, List, Optional, Dict
from ...component import Component
from .base import Base


class FieldNames(Component):
    label: str = None  # 显示的标签文本
    value: str = None  # 选项的实际值
    children: str = None  # 子选项列表的字段名


class Option(Component):
    label: Optional[str] = None
    value: Any = None
    disabled: bool = None
    children: List["Option"] = None
    is_leaf: bool = None


class Cascader(Base):
    component: str = "cascaderField"
    """
    组件名称
    """

    allow_clear: bool = True
    """
    是否允许清除选择
    """

    auto_focus: bool = False
    """
    是否自动获取焦点
    """
    bordered: bool = True
    """
    是否有边框
    """

    clear_icon: Any = None
    """
    自定义清除图标
    """

    change_on_select: bool = False
    """
    点选每级菜单选项值都会发生变化
    """

    class_name: str = None
    """
    自定义类名
    """

    default_value: Any = None
    """
    默认选中项
    """

    disabled: Any = False
    """
    是否禁用
    """

    popup_class_name: str = None
    """
    浮层自定义类名
    """

    expand_icon: Any = None
    """
    次级菜单展开图标
    """

    expand_trigger: str = None
    """
    次级菜单展开方式（click 或 hover）
    """

    field_names: FieldNames = None
    """
    自定义 options 中 label、value、children 的字段
    """

    max_tag_count: int = None
    """
    最多显示多少个 tag
    """

    max_tag_placeholder: str = None
    """
    隐藏 tag 时显示的内容
    """

    max_tag_text_length: int = None
    """
    最大显示的 tag 文本长度
    """

    not_found_content: str = None
    """
    当下拉列表为空时显示的内容
    """

    open: bool = None
    """
    控制浮层显隐
    """

    options: List[Option] = []
    """
    可选项数据源
    """

    placeholder: str = None
    """
    输入框占位文本
    """

    placement: str = None
    """
    浮层预设位置
    """

    show_search: bool = None
    """
    是否在选择框中显示搜索框
    """

    size: str = None
    """
    输入框大小（large/middle/small）
    """

    status: str = None
    """
    校验状态（error/warning）
    """

    style: Dict[str, Any] = None
    """
    自定义样式
    """

    suffix_icon: Any = None
    """
    自定义选择框后缀图标
    """

    value: Any = None
    """
    当前选中值
    """

    multiple: bool = None
    """
    是否支持多选
    """

    show_checked_strategy: str = None
    """
    选中项回填策略
    """

    remove_icon: Any = None
    """
    自定义多选框清除图标
    """

    search_value: str = None
    """
    搜索值
    """

    dropdown_menu_column_style: Any = None
    """
    下拉菜单列的样式
    """

    @model_validator(mode="after")
    def init(self):
        self.set_key()
        self.set_width(400)
        self.placeholder = "请选择"
        return self

    def set_options(self, *args: Any):
        """
        设置选项数据源。
        支持多种参数形式：
        - 单个选项列表
        - 使用 list 转换为选项
        - 指定 rootId、parentKeyName、labelName、valueName 构建树形结构
        """
        if len(args) == 1:
            if isinstance(args[0], list):
                self.options = args[0]
                return self
        elif len(args) >= 4:
            root_id = args[1] if len(args) > 1 else 0
            parent_key_name = args[2]
            label_name = args[3]
            value_name = args[4] if len(args) > 4 else "id"
            self.options = self.list_to_options(
                args[0], root_id, parent_key_name, label_name, value_name
            )
            return self
        return self

    def list_to_options(
        self,
        data: List[Dict[str, Any]],
        root_id: int,
        parent_key_name: str,
        label_name: str,
        value_name: str,
    ) -> List[Option]:
        """
        将扁平列表转换为级联选项树。
        """
        tree = []
        for item in data:
            pid = item.get(parent_key_name)
            if pid == root_id:
                children = self.build_tree(
                    data, item.get(value_name), parent_key_name, label_name, value_name
                )
                tree.append(
                    Option(
                        label=item[label_name],
                        value=item[value_name],
                        children=children,
                    )
                )
        return tree

    def build_tree(
        self,
        data: List[Dict[str, Any]],
        pid: int,
        parent_key_name: str,
        label_name: str,
        value_name: str,
    ) -> List[Option]:
        """
        递归构建树结构。
        """
        children = []
        for item in data:
            if item.get(parent_key_name) == pid:
                child = Option(
                    label=item[label_name],
                    value=item[value_name],
                    children=self.build_tree(
                        data, item[value_name], parent_key_name, label_name, value_name
                    ),
                )
                children.append(child)
        return children

    def set_allow_clear(self, allow_clear: bool):
        self.allow_clear = allow_clear
        return self

    def set_auto_focus(self, auto_focus: bool):
        self.auto_focus = auto_focus
        return self

    def set_bordered(self, bordered: bool):
        self.bordered = bordered
        return self

    def set_clear_icon(self, clear_icon: Any):
        self.clear_icon = clear_icon
        return self

    def set_change_on_select(self, change_on_select: bool):
        self.change_on_select = change_on_select
        return self

    def set_class_name(self, class_name: str):
        self.class_name = class_name
        return self

    def set_default_value(self, default_value: Any):
        self.default_value = default_value
        return self

    def set_popup_class_name(self, popup_class_name: str):
        self.popup_class_name = popup_class_name
        return self

    def set_expand_icon(self, expand_icon: Any):
        self.expand_icon = expand_icon
        return self

    def set_expand_trigger(self, expand_trigger: str):
        self.expand_trigger = expand_trigger
        return self

    def set_field_names(self, field_names: FieldNames):
        self.field_names = field_names
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

    def set_not_found_content(self, not_found_content: str):
        self.not_found_content = not_found_content
        return self

    def set_open(self, open: bool):
        self.open = open
        return self

    def set_placeholder(self, placeholder: str):
        self.placeholder = placeholder
        return self

    def set_placement(self, placement: str):
        self.placement = placement
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

    def set_value(self, value: Any):
        self.value = value
        return self

    def set_multiple(self, multiple: bool):
        self.multiple = multiple
        return self

    def set_show_checked_strategy(self, strategy: str):
        self.show_checked_strategy = strategy
        return self

    def set_remove_icon(self, icon: Any):
        self.remove_icon = icon
        return self

    def set_search_value(self, value: str):
        self.search_value = value
        return self

    def set_dropdown_menu_column_style(self, style: Any):
        self.dropdown_menu_column_style = style
        return self
