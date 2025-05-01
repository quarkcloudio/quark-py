from typing import List, Dict, Any

class Template:
    def __init__(self, template):
        self.template = template
    
    def index_table_menu_items(self, ctx) -> List[Dict[str, str]]:
        # 假设 ctx.template 是一个 Resourcer 类型的实例，返回对应的 MenuItems
        template = ctx.template  # 这里假设ctx对象有template属性
        return template.menu_items(ctx)
    
    def index_table_menu(self, ctx) -> Dict[str, Any]:
        # 获取菜单项
        items = self.index_table_menu_items(ctx)
        if items is None:
            return {}
        
        # 返回表格菜单
        return {
            "type": "tab",
            "items": items
        }
