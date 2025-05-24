from flask import request
from typing import Any, List, Dict, Optional
from ..component.table.column import Column as ColumnComponent
from ..component.descriptions.descriptions import Descriptions as DescriptionsComponent
from ..component.table.column import Column


class ResolvesFields:

    # 字段
    fields: Optional[Any] = None

    # 表格列组件
    table_column: Column = None

    # 行内操作
    table_row_actions: Optional[Any] = None

    # 表格行内操作列标题
    table_action_column_title: str = "操作"

    # 表格行内操作列宽度
    table_action_column_width: int = 150

    def set_fields(self, fields) -> "ResolvesFields":
        """设置字段"""
        self.fields = fields
        return self

    def set_table_column(self, column) -> "ResolvesFields":
        """设置表格列组件"""
        self.table_column = column
        return self

    def set_table_row_actions(self, actions) -> "ResolvesFields":
        """设置行内操作"""
        self.table_row_actions = actions
        return self

    def set_table_action_column_title(self, title) -> "ResolvesFields":
        """设置行内操作列标题"""
        self.table_action_column_title = title
        return self

    def set_table_action_column_width(self, width) -> "ResolvesFields":
        """设置行内操作列宽度"""
        self.table_action_column_width = width
        return self

    def get_fields(self, include_when: bool = True) -> List[Any]:
        return self._find_fields(self.fields, include_when)

    def _find_fields(self, fields: List[Any], include_when: bool) -> List[Any]:
        result = []
        for field in fields:
            if not hasattr(field, "body"):
                result.append(field)
                if include_when and hasattr(field, "when"):
                    result.extend(self._get_when_fields(field))
            else:
                sub_fields = self._find_fields(field.body, include_when)
                result.extend(sub_fields)
        return result

    def _get_when_fields(self, item: Any) -> List[Any]:
        when_fields = []
        if not hasattr(item, "when") or getattr(item, "when") is None:
            return when_fields
        when_comp = getattr(item, "when")
        for option in when_comp.items:
            if option.body:
                if isinstance(option.body, list):
                    when_fields.extend(option.body)
                else:
                    when_fields.append(option.body)
        return when_fields

    def index_fields(self) -> List[Any]:
        return [f for f in self.get_fields() if f.is_shown_on_index()]

    def index_table_columns(self) -> List[ColumnComponent]:
        columns = []
        for field in self.index_fields():
            col = self._field_to_column(field)
            if col:
                columns.append(col)
        row_actions = self.table_row_actions
        if row_actions:
            action_col = (
                self.table_column.set_title(self.table_action_column_title)
                .set_width(self.table_action_column_width)
                .set_attribute("action")
                .set_value_type("option")
                .set_actions(row_actions)
                .set_fixed("right")
            )
            columns.append(action_col)
        return columns

    def _field_to_column(self, field: Any) -> ColumnComponent:
        name = getattr(field, "name", "")
        label = getattr(field, "label", "")
        component = getattr(field, "component", "")
        align = getattr(field, "align", "")
        fixed = getattr(field, "fixed", None)
        editable = getattr(field, "editable", False)
        ellipsis = getattr(field, "ellipsis", None)
        copyable = getattr(field, "copyable", None)
        filters = getattr(field, "filters", None)
        order = getattr(field, "order", None)
        sorter = getattr(field, "sorter", None)
        span = getattr(field, "span", None)
        column_width = getattr(field, "column_width", None)

        col = (
            ColumnComponent()
            .set_title(label)
            .set_attribute(name)
            .set_align(align)
            .set_fixed(fixed)
            .set_ellipsis(ellipsis)
            .set_copyable(copyable)
            .set_filters(filters)
            .set_order(order)
            .set_sorter(sorter)
            .set_span(span)
            .set_width(column_width)
        )

        if component == "idField":
            if getattr(field, "on_index_displayed", False):
                col.set_value_type("text")
            else:
                return None
        elif component == "hiddenField":
            return None
        elif component == "textField":
            col.set_value_type("text")
        elif component == "textAreaField":
            col.set_value_type("text")
        elif component == "editorField":
            col.set_value_type("text")
        elif component == "treeSelectField":
            col.set_value_type("treeSelect").set_field_props(
                {"options": field.get_options()}
            )
        elif component == "cascaderField":
            col.set_value_type("cascader").set_field_props(
                {"options": field.get_options()}
            )
        elif component == "selectField":
            opts = field.get_options()
            col.set_value_type("select").set_field_props({"options": opts})
            if isinstance(filters, bool) and filters:
                col.set_value_enum(field.get_value_enum())
        elif component == "checkboxField":
            col.set_value_type("checkbox").set_field_props(
                {"options": field.get_options()}
            )
            if isinstance(filters, bool) and filters:
                col.set_value_enum(field.get_value_enum())
        elif component == "radioField":
            col.set_value_type("radio").set_field_props(
                {"options": field.get_options()}
            )
            if isinstance(filters, bool) and filters:
                col.set_value_enum(field.get_value_enum())
        elif component == "switchField":
            col.set_value_type("switch").set_value_enum(field.get_options())
        elif component == "imageField":
            col.set_value_type("image")
        elif component == "imagePickerField":
            col.set_value_type("image")
        elif component == "actionField":
            col.set_value_type("action")
        else:
            col.set_value_type(component)

        if editable:
            editable_api = request.path.replace("/index", "/editable")
            col.set_editable(component, field.get_options(), editable_api)

        return col

    def creation_fields(self) -> List[Any]:
        return [f for f in self.get_fields() if f.is_shown_on_creation()]

    def update_fields(self) -> List[Any]:
        return [f for f in self.get_fields() if f.is_shown_on_update()]

    def detail_fields(self) -> List[Any]:
        return [f for f in self.get_fields() if f.is_shown_on_detail()]

    def export_fields(self) -> List[Any]:
        return [
            f
            for f in self.get_fields()
            if getattr(f, "is_shown_on_export", lambda: False)()
        ]

    def import_fields(self) -> List[Any]:
        return [
            f
            for f in self.get_fields()
            if getattr(f, "is_shown_on_import", lambda: False)()
        ]

    def creation_form_fields_parser(self, fields: List[Any]) -> List[Any]:
        result = []
        for field in fields:
            if hasattr(field, "body"):
                body = getattr(field, "body")
                parsed_body = self.creation_form_fields_parser(body)
                setattr(field, "body", parsed_body)
                result.append(field)
            else:
                comp = getattr(field, "component", "")
                if "Field" in comp:
                    when = getattr(field, "when", None)
                    if when:
                        for item in when.items:
                            if item.body:
                                if isinstance(item.body, list):
                                    item.body = self.creation_form_fields_parser(
                                        item.body
                                    )
                                else:
                                    item.body.build_frontend_rules()
                    if field.is_shown_on_creation():
                        field.build_frontend_rules()
                        result.append(field)
                else:
                    result.append(field)
        return result

    def update_form_fields_parser(self, fields: List[Any]) -> List[Any]:
        result = []
        for field in fields:
            if hasattr(field, "body"):
                body = getattr(field, "body")
                parsed_body = self.update_form_fields_parser(body)
                setattr(field, "body", parsed_body)
                result.append(field)
            else:
                comp = getattr(field, "component", "")
                if "Field" in comp:
                    when = getattr(field, "when", None)
                    if when:
                        for item in when.items:
                            if item.body:
                                if isinstance(item.body, list):
                                    item.body = self.update_form_fields_parser(
                                        item.body
                                    )
                                else:
                                    item.body.build_frontend_rules()
                    if field.is_shown_on_update():
                        field.build_frontend_rules()
                        result.append(field)
                else:
                    result.append(field)
        return result

    def detail_fields_parser(
        self, init_api: Any, fields: List[Any], data: Dict[str, Any]
    ) -> DescriptionsComponent:
        cols = []
        for field in fields:
            if hasattr(field, "body"):
                body = getattr(field, "body")
                parsed_body = self.detail_fields_parser(init_api, body, data)
                setattr(field, "body", parsed_body)
                cols.append(field)
            elif field.is_shown_on_detail():
                col = self._field_to_column(field)
                if col:
                    cols.append(col)

        return (
            DescriptionsComponent()
            .set_style({"padding": "24px"})
            .set_init_api(init_api)
            .set_title("")
            .set_column(2)
            .set_columns(cols)
            .set_data_source(data)
            .set_actions(self.detail_actions())
        )

    def detail_actions(self) -> List[Any]:
        return []
