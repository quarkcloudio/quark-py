import json
from sqlalchemy import or_, and_
from flask import request
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Template:

    def __init__(self):
        pass

    # 创建行为查询
    def build_action_query(self, ctx, query):
        template = ctx.get('template')
        query = self.initialize_query(ctx, query)
        query = template.action_query(ctx, query)
        return query

    # 创建详情页查询
    def build_detail_query(self, ctx, query):
        template = ctx.get('template')
        query = self.initialize_query(ctx, query)
        query = template.detail_query(ctx, query)
        return query

    # 创建编辑页查询
    def build_edit_query(self, ctx, query):
        template = ctx.get('template')
        query = self.initialize_query(ctx, query)
        query = template.edit_query(ctx, query)
        return query

    # 创建表格行内编辑查询
    def build_editable_query(self, ctx, query):
        template = ctx.get('template')
        query = self.initialize_query(ctx, query)
        query = template.editable_query(ctx, query)
        return query

    # 创建导出查询
    def build_export_query(self, ctx, query, search, filters, column_filters, orderings):
        template = ctx.get('template')
        query = self.initialize_query(ctx, query)
        query = template.export_query(ctx, query)
        query = self.apply_search(ctx, query, search)
        query = self.apply_filters(query, filters)
        query = self.apply_column_filters(query, column_filters)
        default_order = template.get_query_order()
        if not default_order:
            default_order = template.get_export_query_order()
        if not default_order:
            default_order = "id desc"
        query = self.apply_orderings(query, orderings, default_order)
        return query

    # 创建列表查询
    def build_index_query(self, ctx, query, search, filters, column_filters, orderings):
        template = ctx.get('template')
        query = self.initialize_query(ctx, query)
        query = template.index_query(ctx, query)
        query = self.apply_search(ctx, query, search)
        query = self.apply_filters(query, filters)
        query = self.apply_column_filters(query, column_filters)
        default_order = template.get_query_order()
        if not default_order:
            default_order = template.get_index_query_order()
        if not default_order:
            default_order = "id desc"
        query = self.apply_orderings(query, orderings, default_order)
        return query

    # 创建更新查询
    def build_update_query(self, ctx, query):
        template = ctx.get('template')
        query = self.initialize_query(ctx, query)
        query = template.update_query(ctx, query)
        return query

    # 初始化查询
    def initialize_query(self, ctx, query):
        template = ctx.get('template')
        return template.query(ctx, query)

    # 执行搜索表单查询
    def apply_search(self, ctx, query, search):
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
                query = v.apply(ctx, query, value)

        return query

    # 执行表格列上过滤器查询
    def apply_column_filters(self, query, filters):
        if not filters:
            return query
        for k, v in filters.items():
            if v is not None:
                query = query.filter(getattr(query, k).in_(v))
        return query

    # 执行过滤器查询
    def apply_filters(self, query, filters):
        # todo: 可根据实际需求进一步实现
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

    # 全局查询
    def query(self, ctx, query):
        return query

    # 行为查询
    def action_query(self, ctx, query):
        id_param = request.args.get("id")
        if id_param:
            ids = id_param.split(",") if "," in id_param else [id_param]
            query = query.filter(query.id.in_(ids))
        return query

    # 详情查询
    def detail_query(self, ctx, query):
        id_param = request.args.get("id")
        if id_param:
            query = query.filter(query.id == id_param)
        return query

    # 编辑查询
    def edit_query(self, ctx, query):
        id_param = request.args.get("id")
        if id_param:
            query = query.filter(query.id == id_param)
        return query

    # 表格行内编辑查询
    def editable_query(self, ctx, query):
        data = request.args
        if data:
            if "id" in data:
                query = query.filter(query.id == data["id"])
        return query

    # 导出查询
    def export_query(self, ctx, query):
        id_param = request.args.get("id")
        if id_param:
            ids = id_param.split(",") if "," in id_param else [id_param]
            query = query.filter(query.id.in_(ids))
        return query

    # 列表查询
    def index_query(self, ctx, query):
        return query

    # 更新查询
    def update_query(self, ctx, query):
        data = request.get_json() or {}
        if "id" in data:
            query = query.filter(query.id == data["id"])
        return query
