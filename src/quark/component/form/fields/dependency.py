import json
from typing import Any, List

from pydantic import model_validator

from quark.component.form.fields.when import Item, When

from .base import Base


class Dependency(Base):

    component: str = "dependencyField"
    """
    组件名称
    """

    ignore_form_list_field: bool = False
    """
    是否忽略 FormList 上的字段，默为 False
    """

    names: List[str] = []
    """
    组件内容
    """

    @model_validator(mode="after")
    def init(self):
        self.only_on_forms()
        return self

    def set_when(self, *value: Any):
        """
        用法：
        set_when("name", 1, lambda: [field1, field2])
        set_when("name", ">", 1, lambda: [field1, field2])
        """
        w = When()
        i = Item(body=None)

        if len(value) == 3:
            # 默认 operator =
            name, option, callback = value
            operator = "="
        elif len(value) == 4:
            name, operator, option, callback = value
        else:
            raise ValueError("set_when 参数数量必须是3或4个")

        # 执行回调生成 body
        if callable(callback):
            i.body = callback()

        # 生成条件表达式
        get_option = str(option)
        if operator == "!=":
            i.condition = f"<%=String({name}) !== '{get_option}' %>"
        elif operator == "=":
            i.condition = f"<%=String({name}) === '{get_option}' %>"
        elif operator == ">":
            i.condition = f"<%=String({name}) > '{get_option}' %>"
        elif operator == "<":
            i.condition = f"<%=String({name}) < '{get_option}' %>"
        elif operator == "<=":
            i.condition = f"<%=String({name}) <= '{get_option}' %>"
        elif operator == ">=":
            i.condition = f"<%=String({name}) >= '{get_option}' %>"
        elif operator == "has":
            i.condition = f"<%=(String({name}).indexOf('{get_option}') !=-1) %>"
        elif operator == "in":
            json_str = json.dumps(option)
            i.condition = f"<%=({json_str}.indexOf({name}) !=-1) %>"
        else:
            i.condition = f"<%=String({name}) === '{get_option}' %>"

        i.condition_name = name
        i.condition_operator = operator
        i.option = option

        self.when_item.append(i)
        self.when = w.set_items(self.when_item)
        self.names.append(name)

        return self

    def set_ignore_form_list_field(self, ignore_form_list_field: bool):
        """
        忽略 FormList 上的字段。

        Args:
            ignore_form_list_field (bool): 是否忽略。

        Returns:
            Component: 当前组件实例，支持链式调用。
        """
        self.ignore_form_list_field = ignore_form_list_field
        return self
