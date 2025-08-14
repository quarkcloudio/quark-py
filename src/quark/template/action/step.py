from typing import List

from .action import Action


class Step(Action):
    """
    表示一个步骤导航组件，用于处理“上一步”和“下一步”的操作。
    """

    # 按钮名称，默认为 ["上一步", "下一步"]
    name: List[str] = ("上一步", "下一步")

    def __init__(self):
        self.action_type = "step"
        self.name = ["上一步", "下一步"]
