from dataclasses import dataclass
from quark.template.resource import Resource
from quark.model.action_log import ActionLog as ActionLogModel
from quark.component.form import field
from typing import List, Dict


@dataclass
class ActionLog(Resource):
    """
    日志管理
    """

    def __post_init__(self):

        # 页面标题
        self.title = "日志"

        # 模型
        self.model = ActionLogModel

        return self

    def fields(self) -> List[Dict]:
        """字段定义"""
        return [
            field.id("id", "ID"),
        ]
