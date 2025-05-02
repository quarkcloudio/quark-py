import json
from datetime import datetime
from flask import request, send_file, Response
from your_app.models import YourModel  # 替换为实际模型
from your_app import db
from openpyxl import Workbook
from openpyxl.utils import get_column_letter


class ExportRequest:
    def handle(self):
        """
        处理导出逻辑
        """
        template = self.get_template()

        data = self.query_data()
        fields = template.export_fields(request)

        wb = Workbook()
        ws = wb.active
        ws.title = "Sheet1"

        # 写入表头
        for col_idx, field in enumerate(fields, start=1):
            label = field.get("label", "")
            ws[f"{get_column_letter(col_idx)}1"] = label

        # 写入数据行
        for row_idx, item in enumerate(data, start=2):
            for col_idx, field in enumerate(fields, start=1):
                name = field.get("name")
                component = field.get("component")

                value = None
                if component == "inputNumberField" or component == "textField":
                    value = item.get(name)
                elif component in ["selectField", "checkboxField", "radioField"]:
                    option_label = field.get("getOptionLabel")(item.get(name))
                    value = option_label
                elif component == "switchField":
                    option_label = field.get("getOptionLabel")(item.get(name))
                    value = option_label
                else:
                    value = item.get(name)

                # 特殊格式处理
                if component in ["datetimeField", "dateField"]:
                    format_str = field.get("format", "")
                    format_str = (
                        format_str.replace("YYYY", "%Y")
                        .replace("MM", "%m")
                        .replace("DD", "%d")
                        .replace("HH", "%H")
                        .replace("mm", "%M")
                        .replace("ss", "%S")
                    )
                    if isinstance(value, datetime):
                        value = value.strftime(format_str)

                ws[f"{get_column_letter(col_idx)}{row_idx}"] = value

        # 返回 Excel 文件流
        from io import BytesIO
        output = BytesIO()
        wb.save(output)
        output.seek(0)

        filename = f"data_{datetime.now().strftime('%Y%m%d%H%M%S')}.xlsx"
        headers = {
            "Content-Disposition": f"attachment; filename={filename}",
            "Content-Type": "application/octet-stream",
        }

        return Response(
            output.getvalue(),
            mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            headers=headers,
        )

    def get_template(self):
        """
        获取模板实例（需根据你的业务框架替换）
        """
        # 示例返回一个 mock 对象
        class MockTemplate:
            def export_fields(self, req):
                return []

            def build_export_query(self, query, searches, filters, column_filters, orderings):
                return query

            def before_exporting(self, data):
                return data

        return MockTemplate()

    def query_data(self):
        """
        查询数据
        """
        template = self.get_template()
        model_instance = self.get_model()  # 可以是 YourModel.query 或其他模型类
        query = db.session.query(model_instance)

        searches = template.searches(request) if hasattr(template, "searches") else {}
        filters = template.filters(request) if hasattr(template, "filters") else {}

        column_filters = self.column_filters()
        orderings = self.orderings()

        query = template.build_export_query(query, searches, filters, column_filters, orderings)
        result = query.all()

        return self.performs_list(result)

    def performs_list(self, data):
        """
        处理列表数据格式化
        """
        result = []
        template = self.get_template()
        export_fields = template.export_fields(request)

        for item in data:
            item_dict = item.to_dict() if hasattr(item, "to_dict") else item.__dict__
            fields = {}

            for field in export_fields:
                name = field.get("name")
                callback = field.get("callback")

                if callback:
                    fields[name] = callback(item_dict)
                else:
                    value = item_dict.get(name)
                    component = field.get("component")

                    if component in ["datetimeField", "dateField"]:
                        fmt = field.get("format", "").replace("YYYY", "%Y").replace("MM", "%m").replace("DD", "%d")
                        if isinstance(value, datetime):
                            fields[name] = value.strftime(fmt)
                        else:
                            fields[name] = value
                    else:
                        fields[name] = value

            result.append(fields)

        return template.before_exporting(result)

    def column_filters(self):
        filter_json = request.args.get("filter")
        if not filter_json:
            return {}
        try:
            return json.loads(filter_json)
        except Exception:
            return {}

    def orderings(self):
        sorter_json = request.args.get("sorter")
        if not sorter_json:
            return {}
        try:
            return json.loads(sorter_json)
        except Exception:
            return {}

    def get_model(self):
        """
        获取模型类
        """
        return YourModel