from quark import Request

from ...component.form.fields.select import Option
from .search import Search


class Select(Search):
    """
    下拉框
    """

    component = "selectField"

    def __init__(self, column: str = "", name: str = ""):
        self.name = name
        self.column = column
        return self

    # 设置 Option
    def option(self, label: str, value):
        return Option(label=label, value=value)

    # 默认选项列表（子类可重写）
    def options(self, request: Request):
        return []

    # 单向联动，返回数据类型：{"field": "you_want_load_field", "api": "admin/resource_name/action/select-options"}
    def load(self, request: Request):
        return {"field": "", "api": ""}

    # 设置属性，示例：
    # [{"value": 1, "label": "新闻"}, {"value": 2, "label": "音乐"}, {"value": 3, "label": "体育"}]
    #
    # 或者
    #
    # set_options(options, "label_name", "value_name")
    def set_options(self, *args):
        if len(args) == 1 and isinstance(args[0], list):
            self.select_options = args[0]
            return self

        if len(args) == 3:
            # 假设 list_to_options 是一个用于从列表中提取 label 和 value 的方法
            self.select_options = self.list_to_options(args[0], args[1], args[2])

        return self

    @staticmethod
    def list_to_options(data, label_key, value_key):
        """模拟从列表结构生成选项"""
        return [{"label": item[label_key], "value": item[value_key]} for item in data]
