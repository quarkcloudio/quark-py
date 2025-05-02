import json
from datetime import datetime
from flask import request
from your_app import db
from your_app.models import YourModel  # 替换为实际模型类


class IndexRequest:
    def query_data(self, ctx):
        """
        查询并返回列表数据
        """
        template = self.get_template(ctx)  # 需要替换为你的模板实例获取方式
        model_instance = template.get_model()  # 获取模型类
        query = db.session.query(model_instance)

        searches = template.searches(request)
        filters = template.filters(request)
        column_filters = self.column_filters()
        orderings = self.orderings()

        # 构建查询
        query = template.build_index_query(query, searches, filters, column_filters, orderings)

        # 获取分页配置
        page_size = template.get_page_size()
        page_size_options = template.get_page_size_options()

        if not page_size or not isinstance(page_size, int):
            results = query.all()
            parsed_results = self.performs_list(results)
            return parsed_results

        # 分页参数
        data = request.args.get("search")
        search_params = {}
        if data:
            try:
                search_params = json.loads(data)
            except:
                pass

        page = int(search_params.get("current", 1))
        page_size = int(search_params.get("pageSize", page_size))

        # 获取总数
        total = query.count()

        # 获取当前页数据
        results = query.limit(page_size).offset((page - 1) * page_size).all()

        # 解析列表数据
        parsed_items = self.performs_list(results)

        # 列表显示前回调
        parsed_items = template.before_index_showing(parsed_items)

        return {
            "page": page,
            "pageSize": page_size,
            "pageSizeOptions": page_size_options,
            "total": total,
            "items": parsed_items,
        }

    def column_filters(self):
        """
        获取列过滤条件
        """
        filter_str = request.args.get("filter")
        if not filter_str:
            return {}
        try:
            return json.loads(filter_str)
        except:
            return {}

    def orderings(self):
        """
        获取排序规则
        """
        sorter_str = request.args.get("sorter")
        if not sorter_str:
            return {}
        try:
            return json.loads(sorter_str)
        except:
            return {}

    def performs_list(self, items):
        """
        处理列表字段
        """
        result = []
        template = self.get_template(request)
        index_fields = template.index_fields(request)

        for item in items:
            item_dict = item.to_dict() if hasattr(item, "to_dict") else item.__dict__
            fields = {}

            for field in index_fields:
                component = field.get("component")
                name = field.get("name")

                if component == "actionField":
                    # 行为字段
                    items_func = field.get("get_callback")
                    if items_func:
                        action_items = items_func(item_dict)
                    else:
                        action_items = field.get("items", [])

                    rendered_actions = []
                    for action in action_items:
                        # 初始化行为
                        action.init(request)
                        rendered_actions.append(template.build_action(request, action))

                    fields[name] = rendered_actions
                else:
                    callback = field.get("callback")
                    if callback:
                        fields[name] = callback(item_dict)
                    else:
                        value = item_dict.get(name)
                        if value is None:
                            continue

                        # JSON 字符串解析
                        if isinstance(value, str):
                            if value.startswith("[") or value.startswith("{"):
                                try:
                                    value = json.loads(value)
                                except:
                                    pass

                        # 时间字段格式化
                        if component in ["datetimeField", "dateField"]:
                            fmt = field.get("format", "")
                            fmt = (
                                fmt.replace("YYYY", "%Y")
                                .replace("MM", "%m")
                                .replace("DD", "%d")
                                .replace("HH", "%H")
                                .replace("mm", "%M")
                                .replace("ss", "%S")
                            )
                            if isinstance(value, datetime):
                                value = value.strftime(fmt)

                        # 图片字段处理
                        if component in ["imageField", "imagePickerField"]:
                            from your_app.services.attachment import get_image_url
                            value = get_image_url(value)

                        fields[name] = value

            result.append(fields)

        return result

    def get_template(self, req):
        """
        获取模板实例（需根据你的业务框架替换）
        """
        class MockTemplate:
            def get_model(self):
                return YourModel

            def get_page_size(self):
                return 20

            def get_page_size_options(self):
                return [10, 20, 50, 100]

            def index_fields(self, req):
                return []

            def before_index_showing(self, data):
                return data

            def build_index_query(self, query, searches, filters, column_filters, orderings):
                return query

            def actions(self, req):
                return []

            def build_action(self, req, action):
                return action.render(req)

        return MockTemplate()