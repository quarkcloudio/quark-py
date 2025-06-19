from quark.template.action import Action


class FormSubmit(Action):

    def __init__(self):

        # 文字
        self.name = "提交"

        # 类型（按钮颜色/样式）
        self.type = "primary"

        # 行为类型：submit 表单提交
        self.action_type = "submit"

        # 是否启用 loading 效果（仅 ajax、submit 类型支持）
        self.with_loading = True

        # 设置仅在表单中展示
        self.set_only_on_form(True)
