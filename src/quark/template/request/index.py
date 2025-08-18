import json
from typing import Any

from tortoise.queryset import QuerySet

from quark import Request

from ...services.attachment import AttachmentService
from ..performs_queries import PerformsQueries
from ..resolves_actions import ResolvesActions


class IndexRequest:

    # 请求对象
    request: Request = None

    # 查询对象
    query: QuerySet = None

    # 列表页字段
    fields: list = None

    # 搜索项
    searches: list = None

    # 全局数据排序规则
    query_order: str = None

    # 列表页面的排序规则
    index_query_order: str = None

    # 分页数量
    page_size: int = None

    # 分页配置
    page_size_options: list = None

    def __init__(
        self,
        request: Request,
        resource: Any,
        query: QuerySet,
        query_order: str,
        index_query_order: str,
        fields: list,
        searches: list,
        page_size: int,
        page_size_options: list,
    ):
        self.request = request
        self.resource = resource
        self.query = query
        self.query_order = query_order
        self.index_query_order = index_query_order
        self.fields = fields
        self.searches = searches
        self.page_size = page_size
        self.page_size_options = page_size_options

    async def query_data(self):
        """
        查询并返回列表数据
        """

        # 获取列过滤条件
        column_filters = self.column_filters()

        # 获取排序规则
        orderings = self.orderings()

        # 构建查询
        query = PerformsQueries(
            request=self.request,
            query=self.query,
        ).build_index_query(self.searches, column_filters)

        # 获取分页配置
        page_size = self.page_size
        page_size_options = self.page_size_options
        if not page_size or not isinstance(page_size, int):
            index_query = PerformsQueries(
                request=self.request,
                query_order=self.query_order,
                index_query_order=self.index_query_order,
            ).apply_index_orderings(query, orderings)

            results = await index_query.all()
            return await self.performs_list(results)

        # 分页参数
        data = self.request.query_params.get("search")
        search_params = {}
        if data:
            try:
                search_params = json.loads(data)
            except:
                pass

        page = int(search_params.get("current", 1))
        page_size = int(search_params.get("pageSize", page_size))

        # 获取总数
        total = await query.count()

        # 获取排序规则
        index_query = PerformsQueries(
            request=self.request,
            query_order=self.query_order,
            index_query_order=self.index_query_order,
        ).apply_index_orderings(query, orderings)

        # 获取当前页数据
        results = (
            await index_query.limit(page_size).offset((page - 1) * page_size).all()
        )

        # 解析列表数据
        parsed_items = await self.performs_list(results)

        # 构建返回数据
        data = {
            "page": page,
            "pageSize": page_size,
            "pageSizeOptions": page_size_options,
            "total": total,
            "items": parsed_items,
        }

        return data

    def column_filters(self):
        """
        获取列过滤条件
        """
        filter_str = self.request.query_params.get("filter")
        column_filters = {}
        try:
            column_filters = json.loads(filter_str)
        except:
            pass
        return column_filters

    def orderings(self):
        """
        获取排序规则
        """
        sorter_str = self.request.query_params.get("sorter")
        orderings = {}
        try:
            orderings = json.loads(sorter_str)
        except:
            pass
        return orderings

    async def performs_list(self, items):
        """
        处理列表字段
        """
        result = []
        index_fields = self.fields
        for item in items:
            fields = {}

            for field in index_fields:
                component = field.component
                name = field.name

                if component == "actionField":
                    items_callback = field.callback
                    if items_callback:
                        action_items = await items_callback(item)
                    else:
                        action_items = field.items

                    rendered_actions = []
                    for action in action_items:
                        rendered_actions.append(
                            await ResolvesActions(self.request).build_action(action)
                        )

                    fields[name] = rendered_actions
                else:
                    callback = field.callback
                    if callback:
                        fields[name] = await callback(item)
                    else:
                        value = getattr(item, name, None)
                        if value is None:
                            continue

                        # JSON 字符串解析
                        if isinstance(value, str):
                            if value.startswith("[") or value.startswith("{"):
                                try:
                                    value = json.loads(value)
                                except:
                                    pass

                        # 单独解析时间和日期组件
                        if component in ["datetimeField", "dateField"]:
                            format_str = field.format
                            format_str = format_str.replace("YYYY", "%Y")
                            format_str = format_str.replace("MM", "%m")
                            format_str = format_str.replace("DD", "%d")
                            format_str = format_str.replace("HH", "%H")
                            format_str = format_str.replace("mm", "%M")
                            format_str = format_str.replace("ss", "%S")

                            value = value.strftime(format_str)

                        # 图片字段处理
                        if component in ["imageField", "imagePickerField"]:
                            value = AttachmentService().get_image_url(value)

                        fields[name] = value

            result.append(fields)

        return await self.resource.before_index_showing(self.request, result)
