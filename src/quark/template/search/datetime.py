class Datetime:
    def __init__(self):
        self.component = None

    # 加载初始化数据
    def new(self, ctx):
        self.component = "datetimeField"
        return self