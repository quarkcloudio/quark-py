from dataclasses import dataclass
from typing import List, Dict, Any
from quark_go_v3 import Context, Action


@dataclass
class ModalForm(Action):
    """
    表示一个模态框表单组件，支持配置宽度、按钮文案、API 类型等。
    """
    width: int = 520  # 弹出层宽度，默认值为 520
    destroy_on_close: bool = False  # 关闭时销毁弹出层里的子元素，默认为 False
    cancel_text: str = "取消"  # 获取取消按钮文案，默认为“取消”
    submit_text: str = "提交"  # 获取提交按钮文案，默认为“提交”
    api_type: str = "POST"  # 表单提交接口的类型，GET 或 POST，默认为 POST
    target_blank: bool = False  # 提交表单的数据是否打开新页面，只有在 GET 类型的时候有效，默认为 False

    def new(self, ctx: Context) -> "ModalForm":
        """
        初始化方法，设置默认属性值。

        Args:
            ctx (Context): Quark 上下文对象。

        Returns:
            ModalForm: 返回当前实例。
        """
        self.action_type = "modalForm"
        self.reload = "table"
        self.cancel_text = "取消"
        self.submit_text = "提交"
        self.api_type = "POST"
        self.target_blank = False
        return self

    def fields(self, ctx: Context) -> List[Any]:
        """
        表单字段定义。

        Args:
            ctx (Context): Quark 上下文对象。

        Returns:
            list: 返回表单字段列表。
        """
        return []

    def data(self, ctx: Context) -> Dict[str, Any]:
        """
        异步获取表单数据。

        Args:
            ctx (Context): Quark 上下文对象。

        Returns:
            dict: 返回表单数据。
        """
        return {}

    @property
    def get_width(self) -> int:
        """获取弹出层宽度"""
        return self.width

    @property
    def get_destroy_on_close(self) -> bool:
        """关闭时销毁 Modal 里的子元素"""
        return self.destroy_on_close

    @property
    def get_cancel_text(self) -> str:
        """获取取消按钮文案"""
        return self.cancel_text

    @property
    def get_submit_text(self) -> str:
        """获取提交按钮文案"""
        return self.submit_text

    @property
    def get_api_type(self) -> str:
        """表单提交接口的类型，GET 或 POST，默认为 POST"""
        return self.api_type

    @property
    def get_target_blank(self) -> bool:
        """提交表单的数据是否打开新页面，只有在 GET 类型的时候有效"""
        return self.target_blank