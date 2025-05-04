from typing import Union, List, Dict, Optional
from ..component import Component

class Space(Component):
    # 组件属性定义
    component: str = "space"
    align: Optional[str] = None
    direction: Optional[str] = None
    size: Optional[str] = "small"  # 默认值为 small
    split: Optional[str] = None
    wrap: Optional[bool] = False  # 默认不自动换行
    body: Optional[Union[str, List]] = None  # body 可以是字符串或列表
    style: Optional[Dict[str, str]] = None  # 样式设置，字典形式

    def set_style(self, style: Dict[str, str]) -> "Component":
        """
        设置组件样式
        
        :param style: 样式字典
        :return: 返回当前组件实例
        """
        self.style = style
        return self

    def set_align(self, align: str) -> "Component":
        """
        设置对齐方式
        
        :param align: 对齐方式 (例如 'left', 'center', 'right')
        :return: 返回当前组件实例
        """
        self.align = align
        return self

    def set_direction(self, direction: str) -> "Component":
        """
        设置间距方向
        
        :param direction: 间距方向 (例如 'vertical', 'horizontal')
        :return: 返回当前组件实例
        """
        self.direction = direction
        return self

    def set_size(self, size: str) -> "Component":
        """
        设置间距大小
        
        :param size: 间距大小 (例如 'small', 'medium', 'large')
        :return: 返回当前组件实例
        """
        self.size = size
        return self

    def set_split(self, split: str) -> "Component":
        """
        设置拆分卡片的方向 (vertical | horizontal)
        
        :param split: 拆分方向
        :return: 返回当前组件实例
        """
        self.split = split
        return self

    def set_wrap(self, wrap: bool) -> "Component":
        """
        设置是否自动换行，仅在 horizontal 时有效
        
        :param wrap: 是否自动换行
        :return: 返回当前组件实例
        """
        self.wrap = wrap
        return self

    def set_body(self, body: Union[str, List]) -> "Component":
        """
        设置容器控件里面的内容
        
        :param body: 内容，可以是字符串或列表
        :return: 返回当前组件实例
        """
        self.body = body
        return self