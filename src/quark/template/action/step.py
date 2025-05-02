from dataclasses import dataclass
from typing import List
from quark_go_v3 import Context, Action


@dataclass
class Step(Action):
    """
    表示一个步骤导航组件，用于处理“上一步”和“下一步”的操作。
    """
    name: List[str] = ("上一步", "下一步")  # 按钮名称，默认为 ["上一步", "下一步"]

    def new(self, ctx: Context) -> "Step":
        """
        初始化方法，设置默认属性值。

        Args:
            ctx (Context): Quark 上下文对象。

        Returns:
            Step: 返回当前实例。
        """
        self.action_type = "step"
        self.name = ["上一步", "下一步"]
        return self