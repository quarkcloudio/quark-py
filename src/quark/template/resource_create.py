from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Protocol
from typing_extensions import Self  # 或者 from typing import Self (Python 3.11+)

class Stringy:
    """模拟 github.com/gobeam/stringy 替换逻辑"""
    def __init__(self, value: str):
        self.value = value

    def replace_last(self, old: str, new: str) -> 'Stringy':
        parts = self.value.rsplit(old, 1)
        return Stringy(new.join(parts))

def stringy(value: str) -> Stringy:
    return Stringy(value)

# Context 模拟
@dataclass
class Context:
    path: str
    template: 'Resourcer'

# 接口定义（Protocol）
class Resourcer(Protocol):
    def form_api(self, ctx: 'Context') -> str: ...
    def get_title(self) -> str: ...

# 主模板类
class Template:
    def creation_api(self, ctx: Context) -> str:
        """
        获取创建表单提交接口地址
        """
        template = ctx.template
        form_api = template.form_api(ctx)
        if form_api:
            return form_api

        uri = ctx.path.split('/')
        last_segment = uri[-1]

        if last_segment == "index":
            return stringy(ctx.path).replace_last("/index", "/store").value
        elif last_segment == "form":
            return stringy(ctx.path).replace_last("/form", "/store").value

        return stringy(ctx.path).replace_last("/create", "/store").value

    def creation_component_render(self, ctx: Context, data: Dict[str, Any]) -> Any:
        """
        渲染创建页面组件
        """
        title = self.form_title(ctx)
        form_extra_actions = self.form_extra_actions(ctx)
        api = self.creation_api(ctx)
        fields = self.creation_fields_within_components(ctx)
        form_actions = self.form_actions(ctx)

        return self.form_component_render(
            ctx,
            title,
            form_extra_actions,
            api,
            fields,
            form_actions,
            data
        )

    def creation_fields_within_components(self, ctx: Context) -> Any:
        """
        创建页字段，子类实现
        """
        return []

    def form_title(self, ctx: Context) -> str:
        """
        表单标题，默认使用模板中的标题 + “创建”
        """
        template = ctx.template
        title = template.get_title()
        return title + "创建"

    def form_extra_actions(self, ctx: Context) -> Any:
        """
        表单页右上角自定义区域行为，子类可重写
        """
        return None

    def form_actions(self, ctx: Context) -> List[Any]:
        """
        表单页操作按钮，子类实现
        """
        return []

    def form_component_render(self, ctx: Context, title: str, extra: Any,
                             api: str, fields: Any, actions: List[Any],
                             data: Dict[str, Any]) -> Dict[str, Any]:
        """
        默认的表单渲染方法（模拟返回 JSON 格式响应）
        """
        return {
            "title": title,
            "extra": extra,
            "api": api,
            "fields": fields,
            "actions": actions,
            "data": data
        }

    def before_creating(self, ctx: Context) -> Dict[str, Any]:
        """
        创建页面显示前回调
        """
        return {}