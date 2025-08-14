from typing import Any, Dict, List

from quark import Request

from .action import Action


class ModalForm(Action):
    """
    表示一个模态框表单组件，支持配置宽度、按钮文案、API 类型等。
    """

    action_type: str = "modalForm"

    # 弹出层宽度，默认值为 520
    width: int = 520

    # 关闭时销毁弹出层里的子元素，默认为 False
    destroy_on_close: bool = False

    # 获取取消按钮文案，默认为“取消”
    cancel_text: str = "取消"

    # 获取提交按钮文案，默认为“提交”
    submit_text: str = "提交"

    # 表单提交接口的类型，GET 或 POST，默认为 POST
    api_type: str = "POST"

    # 提交表单的数据是否打开新页面，只有在 GET 类型的时候有效，默认为 False
    target_blank: bool = False

    # 抽屉关闭时是否刷新表格数据，默认为 False
    reload: Any = "table"

    async def fields(self, request: Request) -> List[Any]:
        """
        表单字段定义
        """
        return []

    async def data(self, request: Request) -> Dict[str, Any]:
        """
        异步获取表单数据
        """
        return {}

    def get_width(self) -> int:
        """获取弹出层宽度"""
        return self.width

    def get_destroy_on_close(self) -> bool:
        """关闭时销毁 Modal 里的子元素"""
        return self.destroy_on_close

    def get_cancel_text(self) -> str:
        """获取取消按钮文案"""
        return self.cancel_text

    def get_submit_text(self) -> str:
        """获取提交按钮文案"""
        return self.submit_text

    def get_api_type(self) -> str:
        """表单提交接口的类型，GET 或 POST，默认为 POST"""
        return self.api_type

    def get_target_blank(self) -> bool:
        """提交表单的数据是否打开新页面，只有在 GET 类型的时候有效"""
        return self.target_blank
