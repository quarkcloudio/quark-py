from quark.template.action import Action


class FormReset(Action):

    def __init__(self):

        # 文字
        self.name = "重置"

        # 类型
        self.type = "default"

        # 行为类型
        self.action_type = "reset"

        # 设置在表单页展示
        self.set_show_on_form()
