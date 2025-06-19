from quark.template.action import Action


class FormExtraBack(Action):

    def __init__(self):

        # 文字
        self.name = "返回上一页"

        # 类型
        self.type = "link"

        # 行为类型
        self.action_type = "back"

        # 在表单页右上角自定义区域展示
        self.set_show_on_form_extra()

        # 在详情页右上角自定义区域展示
        self.set_show_on_detail_extra()
