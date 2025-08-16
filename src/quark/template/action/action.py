from typing import Any, List

from tortoise.queryset import QuerySet

from quark import Request


class Action:
    """
    行为类，用于在管理系统中定义按钮、操作等。
    """

    # 设置按钮文字；支持js表达式例如：<%= (status==1 ? '禁用' : '启用') %>，行为在表格行时，可以使用当前行的任意字段值
    name: Any = None

    # 执行成功后刷新的组件
    reload: str = ""

    # 行为接口接收的参数，当行为在表格行展示的时候，可以配置当前行的任意字段
    api_params: List[str] = []

    # 行为接口
    api: str = ""

    # 【必填】这是 action 最核心的配置，来指定该 action 的作用类型，支持：ajax、link、url、drawer、dialog、confirm、cancel、prev、next、copy、close。
    action_type: str = "ajax"

    # 当 action 的作用类型为submit的时候，可以指定提交哪个表格，submitForm为提交表单的key值，为空时提交当前表单
    submit_form: str = ""

    # 设置按钮的图标组件
    icon: Any = None

    # 设置按钮类型，primary | ghost | dashed | link | text | default
    type: str = ""

    # 设置按钮大小,large | middle | small | default
    size: str = ""

    # 是否具有loading，当action 的作用类型为ajax,submit时有效
    with_loading: bool = False

    # 行为表单字段
    fields: Any = None

    # 确认标题
    confirm_title: str = ""

    # 确认文字描述
    confirm_text: str = ""

    # 确认类型
    confirm_type: str = ""

    # 只在列表页展示
    only_on_index: bool = False

    # 只在表单页展示
    only_on_form: bool = False

    # 只在详情页展示
    only_on_detail: bool = False

    # 在列表页展示
    show_on_index: bool = False

    # 在列表页行展示
    show_on_index_table_row: bool = False

    # 在列表页弹出层展示
    show_on_index_table_alert: bool = False

    # 在表单页展示
    show_on_form: bool = False

    # 在表单页扩展栏展示
    show_on_form_extra: bool = False

    # 在详情页展示
    show_on_detail: bool = False

    # 在详情页扩展栏展示
    show_on_detail_extra: bool = False

    async def handle(self, request: Request, query: QuerySet) -> Any:
        """执行行为句柄"""
        raise NotImplementedError("method not implemented")

    def get_uri_key(self, action: Any) -> str:
        """行为key"""
        class_name = action.__class__.__name__
        return class_name.lower()

    def get_name(self) -> Any:
        """获取名称"""
        return self.name

    def get_reload(self) -> str:
        """执行成功后刷新的组件"""
        return self.reload

    def get_api_params(self) -> List[str]:
        """行为接口接收的参数，当行为在表格行展示的时候，可以配置当前行的任意字段"""
        return self.api_params

    def get_api(self) -> str:
        """执行行为的接口"""
        return self.api

    def get_action_type(self) -> str:
        """【必填】这是 action 最核心的配置，来指定该 action 的作用类型"""
        return self.action_type

    def get_submit_form(self) -> str:
        """当 action 的作用类型为submit的时候，可以指定提交哪个表格"""
        return self.submit_form

    def get_type(self) -> str:
        """设置按钮类型，primary | ghost | dashed | link | text | default"""
        return self.type

    def get_size(self) -> str:
        """设置按钮大小,large | middle | small | default"""
        return self.size

    def get_with_loading(self) -> bool:
        """是否具有loading，当action 的作用类型为ajax,submit时有效"""
        return self.with_loading

    def get_icon(self) -> Any:
        """设置按钮的图标组件"""
        return self.icon

    def get_fields(self) -> Any:
        """行为表单字段"""
        return self.fields

    def get_confirm_title(self) -> str:
        """确认标题"""
        return self.confirm_title

    def get_confirm_text(self) -> str:
        """确认文字"""
        return self.confirm_text

    def get_confirm_type(self) -> str:
        """确认类型"""
        return self.confirm_type

    def set_name(self, name: str):
        """设置名称"""
        self.name = name

    def set_reload(self, component_key: str):
        """设置执行成功后刷新的组件"""
        self.reload = component_key

    def set_api_params(self, api_params: List[str]):
        """行为接口接收的参数，当行为在表格行展示的时候，可以配置当前行的任意字段"""
        self.api_params = api_params

    def set_api(self, api: str):
        """执行行为的接口"""
        self.api = api

    def set_action_type(self, action_type: str):
        """【必填】这是 action 最核心的配置，来指定该 action 的作用类型"""
        self.action_type = action_type

    def set_submit_form(self, submit_form: str):
        """当 action 的作用类型为submit的时候，可以指定提交哪个表格"""
        self.submit_form = submit_form

    def set_type(self, button_type: str):
        """设置按钮类型，primary | ghost | dashed | link | text | default"""
        self.type = button_type

    def set_size(self, size: str):
        """设置按钮大小,large | middle | small | default"""
        self.size = size

    def set_with_loading(self, loading: bool):
        """是否具有loading，当action 的作用类型为ajax,submit时有效"""
        self.with_loading = loading

    def set_icon(self, icon: str):
        """设置按钮的图标组件"""
        self.icon = icon

    def set_fields(self, fields: Any):
        """行为表单字段"""
        self.fields = fields

    def set_confirm_title(self, confirm_title: str):
        """确认标题"""
        self.confirm_title = confirm_title

    def set_confirm_text(self, confirm_text: str):
        """确认文字"""
        self.confirm_text = confirm_text

    def set_confirm_type(self, confirm_type: str):
        """确认类型"""
        self.confirm_type = confirm_type

    def with_confirm(self, title: str, text: str, confirm_type: str):
        """设置行为前的确认操作"""
        self.confirm_title = title
        self.confirm_text = text
        self.confirm_type = confirm_type

    def set_only_on_index(self, value: bool):
        """只在列表页展示"""
        self.only_on_index = value
        self.show_on_index = value
        self.show_on_detail = not value
        self.show_on_index_table_row = not value
        self.show_on_index_table_alert = not value
        self.show_on_form = not value
        self.show_on_form_extra = not value
        self.show_on_detail_extra = not value

    def set_except_on_index(self):
        """除了列表页外展示"""
        self.show_on_detail = True
        self.show_on_index_table_row = True
        self.show_on_index_table_alert = True
        self.show_on_form = True
        self.show_on_form_extra = True
        self.show_on_detail_extra = True
        self.show_on_index = False

    def set_only_on_form(self, value: bool):
        """只在表单页展示"""
        self.show_on_form = value
        self.show_on_index_table_alert = not value
        self.show_on_index = not value
        self.show_on_detail = not value
        self.show_on_index_table_row = not value
        self.show_on_form_extra = not value
        self.show_on_detail_extra = not value

    def set_except_on_form(self):
        """除了表单页外展示"""
        self.show_on_index_table_alert = True
        self.show_on_index = True
        self.show_on_detail = True
        self.show_on_index_table_row = True
        self.show_on_form = False
        self.show_on_form_extra = True
        self.show_on_detail_extra = True

    def set_only_on_form_extra(self, value: bool):
        """只在表单页右上角自定义区域展示"""
        self.show_on_form = not value
        self.show_on_index_table_alert = not value
        self.show_on_index = not value
        self.show_on_detail = not value
        self.show_on_index_table_row = not value
        self.show_on_form_extra = value
        self.show_on_detail_extra = not value

    def set_except_on_form_extra(self):
        """除了表单页右上角自定义区域外展示"""
        self.show_on_index_table_alert = True
        self.show_on_index = True
        self.show_on_detail = True
        self.show_on_index_table_row = True
        self.show_on_form = True
        self.show_on_form_extra = False
        self.show_on_detail_extra = True

    def set_only_on_detail(self, value: bool):
        """只在详情页展示"""
        self.only_on_detail = value
        self.show_on_detail = value
        self.show_on_index = not value
        self.show_on_index_table_row = not value
        self.show_on_index_table_alert = not value
        self.show_on_form = not value
        self.show_on_form_extra = not value
        self.show_on_detail_extra = not value

    def set_except_on_detail(self):
        """除了详情页外展示"""
        self.show_on_index = True
        self.show_on_detail = False
        self.show_on_index_table_row = True
        self.show_on_index_table_alert = True
        self.show_on_form = True
        self.show_on_form_extra = True
        self.show_on_detail_extra = True

    def set_only_on_detail_extra(self, value: bool):
        """只在详情页右上角自定义区域展示"""
        self.show_on_form = not value
        self.show_on_index_table_alert = not value
        self.show_on_index = not value
        self.show_on_detail = not value
        self.show_on_index_table_row = not value
        self.show_on_form_extra = not value
        self.show_on_detail_extra = value

    def set_except_on_detail_extra(self):
        """除了详情页右上角自定义区域外展示"""
        self.show_on_index_table_alert = True
        self.show_on_index = True
        self.show_on_detail = True
        self.show_on_index_table_row = True
        self.show_on_form = True
        self.show_on_form_extra = True
        self.show_on_detail_extra = False

    def set_only_on_index_table_row(self, value: bool):
        """在表格行内展示"""
        self.show_on_index_table_row = value
        self.show_on_index = not value
        self.show_on_detail = not value
        self.show_on_index_table_alert = not value
        self.show_on_form = not value
        self.show_on_form_extra = not value
        self.show_on_detail_extra = not value

    def set_except_on_index_table_row(self):
        """除了表格行内外展示"""
        self.show_on_index_table_row = False
        self.show_on_index = True
        self.show_on_detail = True
        self.show_on_index_table_alert = True
        self.show_on_form = True
        self.show_on_form_extra = True
        self.show_on_detail_extra = True

    def set_only_on_index_table_alert(self, value: bool):
        """在表格多选弹出层展示"""
        self.show_on_index_table_alert = value
        self.show_on_index = not value
        self.show_on_detail = not value
        self.show_on_index_table_row = not value
        self.show_on_form = not value
        self.show_on_form_extra = not value
        self.show_on_detail_extra = not value

    def set_except_on_index_table_alert(self):
        """除了表格多选弹出层外展示"""
        self.show_on_index_table_alert = False
        self.show_on_index = True
        self.show_on_detail = True
        self.show_on_index_table_row = True
        self.show_on_form = True
        self.show_on_form_extra = True
        self.show_on_detail_extra = True

    def set_show_on_index(self):
        """在列表页展示"""
        self.show_on_index = True

    def set_show_on_form(self):
        """在表单页展示"""
        self.show_on_form = True

    def set_show_on_form_extra(self):
        """在表单页右上角自定义区域展示"""
        self.show_on_form_extra = True

    def set_show_on_detail(self):
        """在详情页展示"""
        self.show_on_detail = True

    def set_show_on_detail_extra(self):
        """在详情页右上角自定义区域展示"""
        self.show_on_detail_extra = True

    def set_show_on_index_table_row(self):
        """在表格行内展示"""
        self.show_on_index_table_row = True

    def set_show_on_index_table_alert(self):
        """在多选弹出层展示"""
        self.show_on_index_table_alert = True

    def shown_on_index(self) -> bool:
        """判断是否在列表页展示"""
        if self.only_on_index:
            return True
        if self.only_on_detail:
            return False
        if self.only_on_form:
            return False
        return self.show_on_index

    def shown_on_form(self) -> bool:
        """判断是否在表单页展示"""
        if self.only_on_form:
            return True
        if self.only_on_detail:
            return False
        if self.only_on_index:
            return False
        return self.show_on_form

    def shown_on_detail(self) -> bool:
        """判断是否在详情页展示"""
        if self.only_on_detail:
            return True
        if self.only_on_index:
            return False
        if self.only_on_form:
            return False
        return self.show_on_detail

    def shown_on_index_table_row(self) -> bool:
        """判断是否在表格行内展示"""
        return self.show_on_index_table_row

    def shown_on_index_table_alert(self) -> bool:
        """判断是否在多选弹出层展示"""
        return self.show_on_index_table_alert

    def shown_on_form_extra(self) -> bool:
        """判断是否在表单页右上角自定义区域展示"""
        return self.show_on_form_extra

    def shown_on_detail_extra(self) -> bool:
        """判断是否在详情页右上角自定义区域展示"""
        return self.show_on_detail_extra
