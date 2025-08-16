from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field
from tortoise.models import Model
from tortoise.queryset import QuerySet

from quark import Request

from ..component.form.form import Form
from ..component.pagecontainer.pagecontainer import PageContainer
from ..component.pagecontainer.pageheader import PageHeader
from ..component.table.column import Column
from ..component.table.search import Search
from ..component.table.table import Table
from ..component.table.tool_bar import ToolBar
from ..component.table.tree_bar import TreeBar
from .request.action import ActionRequest
from .request.detail import DetailRequest
from .request.edit import EditRequest
from .request.editable import EditableRequest
from .request.index import IndexRequest
from .request.update import UpdateRequest
from .resolves_fields import ResolvesFields
from .resource_create import ResourceCreate
from .resource_detail import ResourceDetail
from .resource_edit import ResourceEdit
from .resource_form import ResourceForm
from .resource_index import ResourceIndex


class Resource(
    BaseModel, ResourceIndex, ResourceForm, ResourceCreate, ResourceEdit, ResourceDetail
):
    """资源：增删改查"""

    # 页面标题
    title: str = Field(default="")

    # 页面副标题
    sub_title: str = Field(default="")

    # 是否显示返回图标
    back_icon: Any = Field(default=True)

    # 是否启用导出功能
    export: bool = Field(default=False)

    # 导出按钮的文本内容
    export_text: str = Field(default="导出")

    # 导出接口的路径
    export_path: str = Field(default="/api/admin/{resource}/export")

    # 每页显示的数据条数，默认为 10
    page_size: Any = Field(default=10)

    # 可选的每页条数选项
    page_size_options: List[int] = Field(default_factory=lambda: [10, 20, 50, 100])

    # 全局数据排序规则
    query_order: str = Field(default="-created_at")

    # 列表页面的排序规则
    index_query_order: str = Field(default="")

    # 导出数据时的排序规则
    export_query_order: str = Field(default="")

    # 数据模型对象
    model: Any = Field(default=None)

    # 表单组件实例
    form: Form = Field(default_factory=Form)

    # 表格组件实例
    table: Table = Field(default_factory=Table)

    # 表格搜索组件
    table_search: Search = Field(default_factory=Search)

    # 表格列配置组件
    table_column: Column = Field(default_factory=Column)

    # 表格工具栏组件
    table_tool_bar: ToolBar = Field(default_factory=ToolBar)

    # 表格树形筛选组件
    table_tree_bar: TreeBar = Field(default_factory=TreeBar)

    # 表格标题后缀文字
    table_title_suffix: str = Field(default="列表")

    # 操作列标题
    table_action_column_title: str = Field(default="操作")

    # 操作列宽度，单位为像素
    table_action_column_width: int = Field(default=150)

    # 表格数据轮询间隔时间（秒）
    table_polling: Any = Field(default=None)

    # 是否将表格数据转换为树形结构
    table_list_to_tree: bool = Field(default=False)

    async def init(self, request: Request) -> Any:
        """初始化"""
        return self

    async def fields(self, request: Request) -> List[Any]:
        """字段定义"""
        return []

    async def searches(self, request: Request) -> List[Any]:
        """搜索项定义"""
        return []

    async def actions(self, request: Request) -> List[Any]:
        """行为定义"""
        return []

    async def menu_items(self, request: Request) -> List[Dict[str, str]]:
        """菜单项定义"""
        return []

    async def get_model(self) -> Model:
        """获取模型实例"""
        if self.model is None:
            raise ValueError("Model not set")
        return self.model()

    async def before_exporting(self, request: Request, data: List[Dict]) -> List[Any]:
        """导出前处理"""
        return [item for item in data]

    async def after_exporting(self, request: Request, result: Any) -> Any:
        """导出后处理"""
        return result

    async def before_importing(
        self, request: Request, data: List[List[Any]]
    ) -> List[List[Any]]:
        """导入前处理"""
        return data

    async def before_editable(
        self, request: Request, id: Any, field: str, value: Any
    ) -> Optional[Exception]:
        """行内编辑前处理"""
        return None

    async def after_editable(
        self, request: Request, id: Any, field: str, value: Any
    ) -> Optional[Exception]:
        """行内编辑后处理"""
        return None

    async def before_action(
        self, request: Request, uri_key: str, query: QuerySet
    ) -> Optional[Exception]:
        """
        回调：在行为执行之前调用。
        """
        return None

    async def after_action(
        self, request: Request, uri_key: str, query: QuerySet
    ) -> Optional[Exception]:
        """
        回调：在行为执行之后调用。
        """
        return None

    async def page_component_render(self, request: Request, body: Any) -> Any:
        """页面组件渲染"""
        return await self.page_container_component_render(request, body)

    async def page_container_component_render(
        self, request: Request, body: Any
    ) -> PageContainer:
        """页面容器组件渲染"""
        header = PageHeader().set_title(self.title).set_sub_title(self.sub_title)
        if not self.back_icon:
            header.set_back_icon(False)
        return PageContainer().set_header(header).set_body(body)

    async def query(self, request: Request) -> QuerySet:
        """
        全局查询
        """
        return self.model.all()

    async def index_query(self, request: Request) -> QuerySet:
        """
        列表查询
        """
        return await self.query(request)

    async def index_render(self, request: Request) -> Any:
        """列表页渲染"""

        # 获取搜索项
        searches = await self.searches(request)

        # 获取列表查询
        query = await self.index_query(request)

        # 获取列表页字段
        index_fields = ResolvesFields(
            request=request,
            fields=await self.fields(request),
        ).index_fields()

        result = await IndexRequest(
            request=request,
            resource=self,
            query=query,
            query_order=self.query_order,
            index_query_order=self.index_query_order,
            fields=index_fields,
            searches=searches,
            page_size=self.page_size,
            page_size_options=self.page_size_options,
        ).query_data()

        # 页面组件渲染
        return await self.page_component_render(
            request, await self.index_component_render(request, result)
        )

    async def creation_render(self, request: Request) -> Any:
        """列表页渲染"""

        data = await self.before_creating(request)

        # 页面组件渲染
        return await self.page_component_render(
            request, await self.creation_component_render(request, data)
        )

    async def store_render(self, request: Request) -> Any:
        """创建方法"""
        model = await self.get_model()

        data = await request.json()

        return await self.form_handle(request, model, data)

    async def edit_render(self, request: Request) -> Any:
        """编辑页渲染"""

        query = await self.query(request)

        fields = ResolvesFields(request, await self.fields(request)).update_fields()

        data = await EditRequest(
            request=request, resource=self, query=query, fields=fields
        ).fill_data()

        data = await self.before_editing(request, data)

        # 页面组件渲染
        return await self.page_component_render(
            request, await self.update_component_render(request, data)
        )

    async def edit_values_render(self, request: Request) -> Any:
        query = await self.query(request)

        fields = ResolvesFields(request, await self.fields(request)).update_fields()

        return await EditRequest(
            request=request, resource=self, query=query, fields=fields
        ).values()

    async def save_render(self, request: Request) -> Any:
        """更新方法"""
        fields = ResolvesFields(
            request, await self.fields(request)
        ).update_fields_without_when()

        model = await self.get_model()

        query = await self.query(request)

        return await UpdateRequest(
            request=request, resource=self, model=model, query=query, fields=fields
        ).handle()

    async def editable_render(self, request: Request) -> Any:
        """表格行内编辑"""
        return await EditableRequest(
            request=request, resource=self, query=await self.query(request)
        ).handle()

    async def action_render(self, request: Request) -> Any:
        """行为渲染"""
        return await ActionRequest(
            request=request,
            resource=self,
            query=await self.query(request),
            actions=await self.actions(request),
            fields=await self.fields(request),
        ).handle()

    async def action_values_render(self, request: Request) -> Any:
        """行为值渲染"""
        return await ActionRequest(
            request=request,
            resource=self,
            query=await self.query(request),
            actions=await self.actions(request),
            fields=await self.fields(request),
        ).values()

    async def detail_render(self, request: Request) -> Any:
        """详情页渲染"""

        query = await self.query(request)

        fields = ResolvesFields(request, await self.fields(request)).detail_fields()

        data = await DetailRequest(
            request=request, resource=self, query=query, fields=fields
        ).fill_data()

        data = await self.before_detail_showing(request, data)

        # 页面组件渲染
        return await self.page_component_render(
            request, await self.detail_component_render(request, data)
        )

    async def detail_values_render(self, request: Request) -> Any:
        """获取详情页值"""

        query = await self.query(request)

        fields = ResolvesFields(request, await self.fields(request)).detail_fields()

        return await DetailRequest(
            request=request, resource=self, query=query, fields=fields
        ).values()

    async def form_render(self, request: Request) -> Any:
        """列表页渲染"""

        data = await self.before_form_showing(request)

        # 页面组件渲染
        return await self.page_component_render(
            request, await self.creation_component_render(request, data)
        )
