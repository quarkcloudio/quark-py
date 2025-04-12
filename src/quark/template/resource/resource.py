from dataclasses import dataclass, field
from typing import Optional, Any, List
import i18n

@dataclass
class Resource:

    # 页面标题
    title: str = ""
    
    # 页面子标题
    sub_title: str = ""
    
    # 页面是否携带返回Icon
    back_icon: bool = False

    # 表单页Form实例
    form: Optional[Any] = None

    # 列表页Table实例
    table: Optional[Any] = None

    # 列表Table组件中的搜索实例
    table_search: Optional[Any] = None

    # 列表Table组件中的Column实例
    table_column: Optional[Any] = None

    # 列表Table组件中的ToolBar实例
    table_tool_bar: Optional[Any] = None

    # 列表Table组件中的TreeBar实例
    table_tree_bar: Optional[Any] = None

    # 列表页表格标题后缀
    table_title_suffix: str = i18n.t('resource.table_title_suffix')

    # 列表页表格行为列显示文字（字段列名）
    table_action_column_title: str = "操作"

    # 列表页表格行为列的宽度
    table_action_column_width: int = 0

    # 列表页表格是否轮询数据（单位：秒）
    table_polling: int = 0

    # 列表页数据转换为树形结构
    # 可为 True 或 dict，如 {"pkName": "id", "pidName": "pid", "childrenName": "children", "rootId": 0}
    table_list_to_tree: Any = None

    # 列表是否具有导出功能
    export: bool = False

    # 列表导出按钮文字内容
    export_text: str = "导出"

    # 列表页分页配置（如每页数量或是否分页）
    page_size: Any = None

    # 指定每页可以显示多少条，如 [10, 20, 50, 100]
    page_size_options: List[int] = field(default_factory=list)

    # 全局排序规则
    query_order: str = ""

    # 列表页排序规则
    index_query_order: str = ""

    # 导出数据排序规则
    export_query_order: str = ""

    # 挂载模型
    model: Any = None