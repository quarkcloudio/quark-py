class Date:
    def __init__(self):
        self.component = None

    # 加载初始化数据
    def new(self, ctx):
        self.component = "dateField"
        return self