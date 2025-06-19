from quark.template.action import Action


class FormStep(Action):

    def __init__(self):

        # 文字
        self.name = ["上一步", "下一步"]

        # 类型
        self.type = "default"

        # 行为类型
        self.action_type = "step"

        # 设置在表单页展示
        self.set_show_on_form()
