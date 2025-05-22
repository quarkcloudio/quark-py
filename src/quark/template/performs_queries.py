import json
from flask import request
from typing import Any, Optional

class PerformsQueries:

    # 查询对象
    query: Optional[Any] = None

    # 全局查询排序
    query_order: Optional[str] = None

    # 列表查询排序
    index_query_order: Optional[str] = None

    # 导出查询排序
    export_query_order: Optional[str] = None

    def set_query(self, query) -> 'PerformsQueries':
        """设置查询对象"""
        self.query = query
        return self

    def set_query_order(self, query_order) -> 'PerformsQueries':
        """设置全局查询排序"""
        self.query_order = query_order
        return self

    def set_index_query_order(self, index_query_order) -> 'PerformsQueries':
        """设置列表查询排序"""
        self.index_query_order = index_query_order
        return self
    
    def set_export_query_order(self, export_query_order) -> 'PerformsQueries':
        """设置导出查询排序"""
        self.export_query_order = export_query_order
        return self

    # 创建行为查询
    def build_action_query(self, query):
        return self.action_query(query)

    # 创建详情页查询
    def build_detail_query(self, query):
        return self.detail_query(query)

    # 创建编辑页查询
    def build_edit_query(self, query):
        return self.edit_query(query)

    # 创建表格行内编辑查询
    def build_editable_query(self, query):
        return self.editable_query(query)

    # 创建导出查询
    def build_export_query(self, search, column_filters, orderings):
        query = self.export_query(self.query)
        query = self.apply_search(query, search)
        query = self.apply_column_filters(query, column_filters)
        default_order = self.query_order
        if not default_order:
            default_order = self.export_query_order
        if not default_order:
            default_order = "id desc"
        query = self.apply_orderings(query, orderings, default_order)
        return query

    # 创建列表查询
    def build_index_query(self, search, column_filters, orderings):
        query = self.apply_search(self.query, search)
        query = self.apply_column_filters(query, column_filters)
        default_order = self.query_order
        if not default_order:
            default_order = self.index_query_order
        if not default_order:
            default_order = "id desc"
        query = self.apply_orderings(query, orderings, default_order)
        return query

    # 创建更新查询
    def build_update_query(self, query):
        return self.update_query(query)

    # 执行搜索表单查询
    def apply_search(self, query, search):
        queries = ctx.get('queries', {})
        data = {}
        if "search" not in queries:
            return query
        try:
            data = json.loads(queries["search"])
        except json.JSONDecodeError:
            return query

        for v in search:
            column = v.get_column(v)
            value = data.get(column)
            if value is not None:
                query = v.apply(query, value)

        return query

    # 执行表格列上过滤器查询
    def apply_column_filters(self, query, filters):
        if not filters:
            return query
        for k, v in filters.items():
            if v is not None:
                query = query.filter(getattr(query, k).in_(v))
        return query

    # 执行排序查询
    def apply_orderings(self, query, orderings, default_order):
        if not orderings:
            return query.order_by(default_order)
        for key, v in orderings.items():
            if v == "descend":
                query = query.order_by(getattr(query, key).desc())
            else:
                query = query.order_by(getattr(query, key).asc())
        return query

    # 行为查询
    def action_query(self, query):
        id_param = request.args.get("id")
        if id_param:
            ids = id_param.split(",") if "," in id_param else [id_param]
            query = query.filter(query.id.in_(ids))
        return query

    # 详情查询
    def detail_query(self, query):
        id_param = request.args.get("id")
        if id_param:
            query = query.filter(query.id == id_param)
        return query

    # 编辑查询
    def edit_query(self, query):
        id_param = request.args.get("id")
        if id_param:
            query = query.filter(query.id == id_param)
        return query

    # 表格行内编辑查询
    def editable_query(self, query):
        data = request.args
        if data:
            if "id" in data:
                query = query.filter(query.id == data["id"])
        return query

    # 导出查询
    def export_query(self, query):
        id_param = request.args.get("id")
        if id_param:
            ids = id_param.split(",") if "," in id_param else [id_param]
            query = query.filter(query.id.in_(ids))
        return query

    # 列表查询
    def index_query(self, query):
        return query

    # 更新查询
    def update_query(self, query):
        data = request.get_json() or {}
        if "id" in data:
            query = query.filter(query.id == data["id"])
        return query
