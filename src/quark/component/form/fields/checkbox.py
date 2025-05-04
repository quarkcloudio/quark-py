from typing import Any, Optional, List, Dict, Union, Callable, TypeVar, Generic, get_args
from pydantic import BaseModel
from enum import Enum
import json
import re
import abc
import abc
import string
from functools import reduce
from operator import getitem
from collections.abc import Mapping

T = TypeVar("T")


class Option(BaseModel):
    """
    选项类，用于表示复选框中的每一个选项。
    """
    label: str  # 选项显示文本
    value: Any  # 选项值
    disabled: bool = False  # 是否禁用


class TableColumnAlign(str, Enum):
    left = "left"
    right = "right"
    center = "center"


class TableColumnFixed(str, Enum):
    true = "true"
    left = "left"
    right = "right"


# ----------------------------
# 子组件定义
# ----------------------------

class TableCol(BaseModel):
    span: int = 3
    offset: int = 0


class TableColumn(BaseModel):
    align: Optional[TableColumnAlign] = None  # 列对齐方式
    fixed: Optional[Union[bool, TableColumnFixed]] = None  # 列是否固定
    editable: bool = False  # 是否可编辑
    ellipsis: bool = False  # 是否自动缩略
    copyable: bool = False  # 是否支持复制
    filters: Optional[List[Dict[str, str]]] = None  # 筛选菜单项
    order: int = 0  # 查询表单权重
    sorter: Optional[bool] = None  # 可排序
    width: Optional[int] = None  # 列宽


class Rule(BaseModel):
    name: str = ""  # 字段名
    required: bool = False  # 是否必填
    message: str = ""  # 提示信息
    min_length: Optional[int] = None  # 最小长度
    max_length: Optional[int] = None  # 最大长度


class WhenItem(BaseModel):
    condition: str  # 条件表达式字符串
    body: List[Any]  # 条件满足时返回的内容
    condition_name: str  # 条件字段名
    condition_operator: str  # 条件操作符
    option: Any  # 条件值


class WhenComponent(BaseModel):
    items: List[WhenItem]  # When 组件包含的条件项列表


# ----------------------------
# 主组件类
# ----------------------------

class Component(BaseModel):
    """
    复选框组件主类，封装了所有与复选框相关的属性和方法。
    """

    component_key: str = ""  # 组件唯一标识
    component: str = "checkboxField"  # 组件名称

    # Form 相关属性
    row_props: Optional[Dict[str, Any]] = None  # Grid 模式下传递给 Row 的属性
    col_props: Optional[Dict[str, Any]] = None  # Grid 模式下传递给 Col 的属性
    secondary: bool = False  # 是否是次要控件
    colon: bool = True  # 是否显示冒号
    extra: Optional[str] = None  # 额外提示信息
    has_feedback: bool = False  # 是否展示校验图标
    help: Optional[str] = None  # 提示信息
    hidden: bool = False  # 是否隐藏字段
    initial_value: Optional[Any] = None  # 初始值
    label: Optional[str] = None  # 标签文本
    label_align: str = "right"  # 标签对齐方式
    label_col: Optional[Union[Dict[str, Any], TableCol]] = None  # 标签布局
    name: Optional[str] = None  # 字段名
    no_style: bool = False  # 不带样式
    required: bool = False  # 是否必填
    tooltip: Optional[str] = None  # 悬浮提示
    value_prop_name: Optional[str] = None  # 值属性名
    wrapper_col: Optional[Union[Dict[str, Any], TableCol]] = None  # 控件布局

    # 表格列相关
    column: TableColumn = TableColumn()  # 列配置
    align: Optional[str] = None  # 对齐方式
    fixed: Optional[Union[bool, str]] = None  # 是否固定
    editable: bool = False  # 是否可编辑
    ellipsis: bool = False  # 自动缩略
    copyable: bool = False  # 支持复制
    filters: Optional[Any] = None  # 筛选项
    order: int = 0  # 排序权重
    sorter: Optional[Any] = None  # 排序器
    span: int = 0  # 包含列数
    column_width: int = 0  # 列宽

    # 数据与行为
    api: Optional[str] = None  # 数据接口
    ignore: bool = False  # 是否忽略保存
    rules: List[Rule] = []  # 全局校验规则
    creation_rules: List[Rule] = []  # 创建页规则
    update_rules: List[Rule] = []  # 编辑页规则
    frontend_rules: List[Rule] = []  # 前端规则
    when: Optional[WhenComponent] = None  # When 组件
    when_item: List[WhenItem] = []  # When 项
    show_on_index: bool = True  # 列表页可见
    show_on_detail: bool = True  # 详情页可见
    show_on_creation: bool = True  # 创建页可见
    show_on_update: bool = True  # 编辑页可见
    show_on_export: bool = True  # 导出页可见
    show_on_import: bool = True  # 导入页可见
    callback: Optional[Callable[[Dict[str, Any]], Any]] = None  # 回调函数

    # 值相关
    default_value: Optional[Any] = None  # 默认值
    disabled: bool = False  # 是否禁用
    value: Optional[Any] = None  # 当前值
    options: List[Option] = []  # 选项列表

    class Config:
        arbitrary_types_allowed = True  # 允许任意类型

    # ----------------------------
    # 初始化
    # ----------------------------

    def init(self) -> "Component":
        """初始化组件默认值"""
        self.component = "checkboxField"
        self.colon = True
        self.label_align = "right"
        self.show_on_index = True
        self.show_on_detail = True
        self.show_on_creation = True
        self.show_on_update = True
        self.show_on_export = True
        self.show_on_import = True
        self.column = TableColumn()
        return self

    def set_key(self, key: str, crypt: bool = True) -> "Component":
        """设置组件 Key，可加密"""
        # 这里可以使用 hex.Make 实现加密逻辑
        self.component_key = key
        return self

    def set_tooltip(self, tooltip: str) -> "Component":
        """设置悬浮提示"""
        self.tooltip = tooltip
        return self

    def set_row_props(self, props: Dict[str, Any]) -> "Component":
        """设置 Row 属性"""
        self.row_props = props
        return self

    def set_col_props(self, props: Dict[str, Any]) -> "Component":
        """设置 Col 属性"""
        self.col_props = props
        return self

    def set_secondary(self, secondary: bool) -> "Component":
        """设置是否次要控件"""
        self.secondary = secondary
        return self

    def set_colon(self, colon: bool) -> "Component":
        """设置是否显示冒号"""
        self.colon = colon
        return self

    def set_extra(self, extra: str) -> "Component":
        """设置额外提示信息"""
        self.extra = extra
        return self

    def set_has_feedback(self, feedback: bool) -> "Component":
        """设置是否有反馈图标"""
        self.has_feedback = feedback
        return self

    def set_help(self, help_text: str) -> "Component":
        """设置帮助信息"""
        self.help = help_text
        return self

    def set_no_style(self) -> "Component":
        """不带样式"""
        self.no_style = True
        return self

    def set_label(self, label: str) -> "Component":
        """设置标签文本"""
        self.label = label
        return self

    def set_label_align(self, align: str) -> "Component":
        """设置标签对齐方式"""
        self.label_align = align
        return self

    def set_label_col(self, col: Any) -> "Component":
        """设置标签布局"""
        self.label_col = col
        return self

    def set_name(self, name: str) -> "Component":
        """设置字段名"""
        self.name = name
        return self

    def set_required(self) -> "Component":
        """设置为必填"""
        self.required = True
        return self

    def set_value_prop_name(self, prop: str) -> "Component":
        """设置值属性名"""
        self.value_prop_name = prop
        return self

    def set_wrapper_col(self, col: Any) -> "Component":
        """设置控件布局"""
        self.wrapper_col = col
        return self

    def set_column(self, func: Callable[[TableColumn], TableColumn]) -> "Component":
        """设置列配置"""
        self.column = func(self.column)
        return self

    def set_align(self, align: str) -> "Component":
        """设置列对齐方式"""
        self.align = align
        return self

    def set_fixed(self, fixed: Any) -> "Component":
        """设置列是否固定"""
        self.fixed = fixed
        return self

    def set_editable(self, editable: bool) -> "Component":
        """设置是否可编辑"""
        self.editable = editable
        return self

    def set_ellipsis(self, ellipsis: bool) -> "Component":
        """设置自动缩略"""
        self.ellipsis = ellipsis
        return self

    def set_copyable(self, copyable: bool) -> "Component":
        """设置是否可复制"""
        self.copyable = copyable
        return self

    def set_filters(self, filters: Any) -> "Component":
        """设置筛选项"""
        if isinstance(filters, dict):
            tmp_filters = [{"text": v, "value": k} for k, v in filters.items()]
            self.filters = tmp_filters
        else:
            self.filters = filters
        return self

    def set_order(self, order: int) -> "Component":
        """设置查询权重"""
        self.order = order
        return self

    def set_sorter(self, sorter: bool) -> "Component":
        """设置是否可排序"""
        self.sorter = sorter
        return self

    def set_span(self, span: int) -> "Component":
        """设置列跨度"""
        self.span = span
        return self

    def set_column_width(self, width: int) -> "Component":
        """设置列宽"""
        self.column_width = width
        return self

    def set_value(self, value: Any) -> "Component":
        """设置当前值"""
        self.value = value
        return self

    def set_default(self, value: Any) -> "Component":
        """设置默认值"""
        self.default_value = value
        return self

    def set_disabled(self, disabled: bool) -> "Component":
        """设置是否禁用"""
        self.disabled = disabled
        return self

    def set_ignore(self, ignore: bool) -> "Component":
        """设置是否忽略保存"""
        self.ignore = ignore
        return self

    def set_when(self, *args) -> "Component":
        """设置 When 条件"""
        w = WhenComponent(items=self.when_item)

        if len(args) == 2:
            operator = "="
            option = args[0]
            callback = args[1]
        elif len(args) == 3:
            operator = args[0]
            option = args[1]
            callback = args[2]
        else:
            raise ValueError("参数数量必须为2或3")

        body = callback()
        condition = f"<%=String({self.name}) {operator} '{option}' %>"
        item = WhenItem(
            condition=condition,
            body=body,
            condition_name=self.name,
            condition_operator=operator,
            option=option
        )
        self.when_item.append(item)
        self.when = WhenComponent(items=self.when_item)
        return self

    def build_options(self, items: List[T], label_name: str, value_name: str) -> List[Option]:
        """通过反射构建选项列表"""
        options = []
        for item in items:
            try:
                value = getattr(item, value_name)
                label = getattr(item, label_name)
            except AttributeError:
                continue
            options.append(Option(label=label, value=value))
        return options

    def list_to_options(self, items: List[T], label_name: str, value_name: str) -> List[Option]:
        """从列表中构建选项"""
        return self.build_options(items, label_name, value_name)

    def set_options(self, *args) -> "Component":
        """设置选项"""
        if len(args) == 1 and isinstance(args[0], list):
            self.options = args[0]
        elif len(args) == 3:
            self.options = self.list_to_options(*args)
        return self

    def get_option_label(self, value: Any) -> str:
        """根据值获取标签"""
        labels = [opt.label for opt in self.options if opt.value == value]
        return ", ".join(labels)

    def get_option_value(self, label: str) -> Any:
        """根据标签获取值"""
        labels = re.split(r"[,，]", label)
        values = [opt.value for opt in self.options if opt.label in labels]
        return values if len(values) > 1 else values[0] if values else None

    def get_option_labels(self) -> str:
        """获取所有标签"""
        return ", ".join(opt.label for opt in self.options)

    def set_callback(self, closure: Callable[[Dict[str, Any]], Any]) -> "Component":
        """设置回调函数"""
        self.callback = closure
        return self

    def is_shown_on_index(self) -> bool:
        """是否在列表页显示"""
        return self.show_on_index

    def is_shown_on_detail(self) -> bool:
        """是否在详情页显示"""
        return self.show_on_detail

    def is_shown_on_creation(self) -> bool:
        """是否在创建页显示"""
        return self.show_on_creation

    def is_shown_on_update(self) -> bool:
        """是否在更新页显示"""
        return self.show_on_update

    def only_on_index(self) -> "Component":
        """仅在列表页显示"""
        self._reset_visibility()
        self.show_on_index = True
        return self

    def _reset_visibility(self):
        """重置所有显示状态"""
        self.show_on_index = False
        self.show_on_detail = False
        self.show_on_creation = False
        self.show_on_update = False
        self.show_on_export = False
        self.show_on_import = False