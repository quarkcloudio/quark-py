from .search import Search


class Radio(Search):
    """单选组件"""

    def __init__(self, column: str = "", name: str = ""):
        self.component = "radioField"
        return self

    # 设置 Option
    def option(self, label: str, value):
        return {"value": value, "label": label}

    # 设置属性，示例：[{"value": 1, "label": "男"}, {"value": 2, "label": "女"}]
    #
    # 或者
    #
    # set_options(options, "label_name", "value_name")
    def set_options(self, *args):
        if len(args) == 1:
            if isinstance(args[0], list):
                self.radio_options = args[0]
                return self

        if len(args) == 3:
            # 假设 radio.list_to_options 实现了字段映射转换逻辑
            self.radio_options = self.list_to_options(args[0], args[1], args[2])

        return self

    @staticmethod
    def list_to_options(data, label_key, value_key):
        """模拟从列表结构生成选项"""
        return [{"label": item[label_key], "value": item[value_key]} for item in data]
