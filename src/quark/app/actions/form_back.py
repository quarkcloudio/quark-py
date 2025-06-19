from quark.template.action import Action


class FormBack(Action):

    def __init__(self):

        # 文字
        self.name = "返回上一页"

        # 类型
        self.type = "default"

        # 行为类型
        self.action_type = "back"

        # 在表单页展示
        self.set_show_on_form()

        # 在详情页展示
        self.set_show_on_detail()
