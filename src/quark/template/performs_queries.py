import json
from typing import Optional

from tortoise.expressions import Q
from tortoise.queryset import QuerySet

from quark import Request


class PerformsQueries:

    # 请求对象
    request: Request = None

    # 查询对象
    query: QuerySet = None

    # 全局查询排序
    query_order: str = None

    # 列表查询排序
    index_query_order: str = None

    # 导出查询排序
    export_query_order: str = None

    def __init__(
        self,
        request: Optional[Request] = None,
        query: Optional[QuerySet] = None,
        query_order: Optional[str] = None,
        index_query_order: Optional[str] = None,
        export_query_order: Optional[str] = None,
    ):
        self.request = request
        self.query = query
        self.query_order = query_order
        self.index_query_order = index_query_order
        self.export_query_order = export_query_order

    # 创建行为查询
    def build_action_query(self, query: QuerySet) -> QuerySet:
        return self.action_query(query)

    # 创建详情页查询
    def build_detail_query(self, query: QuerySet) -> QuerySet:
        return self.detail_query(query)

    # 创建编辑页查询
    def build_edit_query(self, query: QuerySet) -> QuerySet:
        return self.edit_query(query)

    # 创建表格行内编辑查询
    def build_editable_query(self, query: QuerySet) -> QuerySet:
        return self.editable_query(query)

    # 创建导出查询
    def build_export_query(self, search, column_filters) -> QuerySet:
        query = self.export_query(self.query)
        query = self.apply_search(query, search)
        query = self.apply_column_filters(query, column_filters)
        return query

    # 创建列表查询
    def build_index_query(self, search, column_filters) -> QuerySet:
        query = self.index_query(self.query)
        query = self.apply_search(query, search)
        query = self.apply_column_filters(query, column_filters)
        return query

    # 创建更新查询
    async def build_update_query(self, query: QuerySet) -> QuerySet:
        return await self.update_query(query)

    # 执行搜索表单查询
    def apply_search(self, query: QuerySet, search) -> QuerySet:
        json_string = self.request.query_params.get("search", {})
        if not json_string:
            return query

        data = json.loads(json_string)
        for v in search:
            column = v.get_column(v)
            value = data.get(column)
            if value is not None:
                query = v.apply(self.request, query, value)

        return query

    # 执行表格列上过滤器查询
    def apply_column_filters(self, query: QuerySet, filters) -> QuerySet:
        if not filters:
            return query
        for k, v in filters.items():
            if v is not None:
                query = query.filter(getattr(query, k).in_(v))
        return query

    def apply_index_orderings(self, query: QuerySet, orderings) -> QuerySet:
        default_order = self.query_order
        if not default_order:
            default_order = self.index_query_order
        if not default_order:
            default_order = "-id"
        return self.apply_orderings(query, orderings, default_order)

    def apply_export_orderings(self, query: QuerySet, orderings) -> QuerySet:
        default_order = self.query_order
        if not default_order:
            default_order = self.export_query_order
        if not default_order:
            default_order = "-id"
        return self.apply_orderings(query, orderings, default_order)

    # 执行排序查询
    def apply_orderings(
        self, query: QuerySet, orderings, default_order: str
    ) -> QuerySet:
        if not orderings:
            return query.order_by(default_order)
        for key, v in orderings.items():
            if v == "descend":
                query = query.order_by(getattr(query, key).desc())
            else:
                query = query.order_by(getattr(query, key).asc())
        return query

    # 行为查询
    def action_query(self, query: QuerySet) -> QuerySet:
        id_param = self.request.query_params.get("id")
        if id_param:
            ids = id_param.split(",") if "," in id_param else [id_param]
            query = query.filter(Q(id__in=ids))
        return query

    # 详情查询
    def detail_query(self, query: QuerySet) -> QuerySet:
        id_param = self.request.query_params.get("id")
        if id_param:
            query = query.filter(Q(id=id_param))
        return query

    # 编辑查询
    def edit_query(self, query: QuerySet) -> QuerySet:
        id_param = self.request.query_params.get("id")
        if id_param:
            query = query.filter(Q(id=id_param))
        return query

    # 表格行内编辑查询
    def editable_query(self, query: QuerySet) -> QuerySet:
        id_param = self.request.query_params.get("id")
        if id_param:
            query = query.filter(Q(id=id_param))
        return query

    # 导出查询
    def export_query(self, query: QuerySet) -> QuerySet:
        id_param = self.request.query_params.get("id")
        if id_param:
            ids = id_param.split(",") if "," in id_param else [id_param]
            query = query.filter(Q(id__in=ids))
        return query

    # 列表查询
    def index_query(self, query: QuerySet) -> QuerySet:
        return query

    # 更新查询
    async def update_query(self, query: QuerySet) -> QuerySet:
        data = await self.request.json() or {}
        if "id" in data:
            query = query.filter(id=data["id"])
        return query
