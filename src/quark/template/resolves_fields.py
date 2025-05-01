from typing import Any, List, Dict, Optional, Union
from abc import ABC, abstractmethod
from dataclasses import dataclass
import re
import inspect


def snake_case_name(name: str) -> str:
    """Convert camelCase to snake_case"""
    return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()


@dataclass
class Context:
    path: str = ""
    template: Any = None

    def path(self) -> str:
        return self.path


class FieldInterface(ABC):
    @abstractmethod
    def is_shown_on_index(self) -> bool:
        pass

    @abstractmethod
    def is_shown_on_creation(self) -> bool:
        pass

    @abstractmethod
    def is_shown_on_update(self) -> bool:
        pass

    @abstractmethod
    def is_shown_on_detail(self) -> bool:
        pass

    @abstractmethod
    def build_frontend_rules(self, path: str):
        pass

    def get_options(self) -> list:
        pass

    def get_value_enum(self) -> dict:
        pass

    def get_when(self) -> 'WhenComponent':
        pass


class ColumnComponent:
    def __init__(self):
        self.title = ""
        self.attribute = ""
        self.align = ""
        self.fixed = None
        self.ellipsis = False
        self.copyable = False
        self.filters = None
        self.order = 0
        self.sorter = None
        self.span = 1
        self.width = 0
        self.value_type = ""
        self.field_props = {}
        self.value_enum = {}

    def set_title(self, title: str):
        self.title = title
        return self

    def set_attribute(self, attribute: str):
        self.attribute = attribute
        return self

    def set_align(self, align: str):
        self.align = align
        return self

    def set_fixed(self, fixed: Optional[str]):
        self.fixed = fixed
        return self

    def set_ellipsis(self, ellipsis: bool):
        self.ellipsis = ellipsis
        return self

    def set_copyable(self, copyable: bool):
        self.copyable = copyable
        return self

    def set_filters(self, filters: Any):
        self.filters = filters
        return self

    def set_order(self, order: int):
        self.order = order
        return self

    def set_sorter(self, sorter: Any):
        self.sorter = sorter
        return self

    def set_span(self, span: int):
        self.span = span
        return self

    def set_width(self, width: int):
        self.width = width
        return self

    def set_value_type(self, value_type: str):
        self.value_type = value_type
        return self

    def set_field_props(self, props: Dict[str, Any]):
        self.field_props = props
        return self

    def set_value_enum(self, value_enum: Dict[str, Any]):
        self.value_enum = value_enum
        return self

    def set_editable(self, component: str, options: list, api: str):
        self.field_props["editable"] = {
            "component": component,
            "options": options,
            "api": api
        }
        return self


class WhenComponent:
    def __init__(self):
        self.items = []

    def get_when(self) -> 'WhenComponent':
        return self


class DescriptionsComponent:
    def __init__(self):
        self.style = {}
        self.init_api = None
        self.title = ""
        self.column = 2
        self.columns = []
        self.data_source = {}
        self.actions = []

    def init(self):
        return self

    def set_style(self, style: Dict[str, Any]):
        self.style = style
        return self

    def set_init_api(self, init_api: str):
        self.init_api = init_api
        return self

    def set_title(self, title: str):
        self.title = title
        return self

    def set_column(self, column: int):
        self.column = column
        return self

    def set_columns(self, columns: list):
        self.columns = columns
        return self

    def set_data_source(self, data_source: dict):
        self.data_source = data_source
        return self

    def set_actions(self, actions: list):
        self.actions = actions
        return self


class TableComponent:
    def get_table_column(self, ctx: Context) -> ColumnComponent:
        return ColumnComponent()

    def get_table_action_column_title(self) -> str:
        return "操作"

    def get_table_action_column_width(self) -> int:
        return 150

    def index_table_row_actions(self, ctx: Context):
        return []


class Template(TableComponent, ABC):
    def __init__(self):
        super().__init__()

    def fields(self, ctx: Context) -> List[FieldInterface]:
        return []

    def get_fields(self, ctx: Context, include_when: bool = True) -> List[FieldInterface]:
        return self._find_fields(self.fields(ctx), include_when)

    def _find_fields(self, fields: List[FieldInterface], include_when: bool) -> List[FieldInterface]:
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

    def _get_when_fields(self, item: FieldInterface) -> List[FieldInterface]:
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

    def index_fields(self, ctx: Context) -> List[FieldInterface]:
        return [f for f in self.get_fields(ctx) if f.is_shown_on_index()]

    def index_table_columns(self, ctx: Context) -> List[ColumnComponent]:
        columns = []
        for field in self.index_fields(ctx):
            col = self._field_to_column(ctx, field)
            if col:
                columns.append(col)
        row_actions = self.index_table_row_actions(ctx)
        if row_actions:
            action_col = (
                self.get_table_column(ctx)
                .set_title(self.get_table_action_column_title())
                .set_width(self.get_table_action_column_width())
                .set_attribute("action")
                .set_value_type("option")
                .set_actions(row_actions)
                .set_fixed("right")
            )
            columns.append(action_col)
        return columns

    def _field_to_column(self, ctx: Context, field: FieldInterface) -> ColumnComponent:
        name = getattr(field, "name", "")
        label = getattr(field, "label", "")
        component = getattr(field, "component", "")
        align = getattr(field, "align", "")
        fixed = getattr(field, "fixed", None)
        editable = getattr(field, "editable", False)
        ellipsis = getattr(field, "ellipsis", False)
        copyable = getattr(field, "copyable", False)
        filters = getattr(field, "filters", None)
        order = getattr(field, "order", 0)
        sorter = getattr(field, "sorter", None)
        span = getattr(field, "span", 1)
        column_width = getattr(field, "column_width", 0)

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
            col.set_value_type("treeSelect").set_field_props({"options": field.get_options()})
        elif component == "cascaderField":
            col.set_value_type("cascader").set_field_props({"options": field.get_options()})
        elif component == "selectField":
            opts = field.get_options()
            col.set_value_type("select").set_field_props({"options": opts})
            if isinstance(filters, bool) and filters:
                col.set_value_enum(field.get_value_enum())
        elif component == "checkboxField":
            col.set_value_type("checkbox").set_field_props({"options": field.get_options()})
            if isinstance(filters, bool) and filters:
                col.set_value_enum(field.get_value_enum())
        elif component == "radioField":
            col.set_value_type("radio").set_field_props({"options": field.get_options()})
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
            editable_api = ctx.path.replace("/index", "/editable")
            col.set_editable(component, field.get_options(), editable_api)

        return col

    def creation_fields(self, ctx: Context) -> List[FieldInterface]:
        return [f for f in self.get_fields(ctx) if f.is_shown_on_creation()]

    def update_fields(self, ctx: Context) -> List[FieldInterface]:
        return [f for f in self.get_fields(ctx) if f.is_shown_on_update()]

    def detail_fields(self, ctx: Context) -> List[FieldInterface]:
        return [f for f in self.get_fields(ctx) if f.is_shown_on_detail()]

    def export_fields(self, ctx: Context) -> List[FieldInterface]:
        return [f for f in self.get_fields(ctx) if getattr(f, "is_shown_on_export", lambda: False)()]

    def import_fields(self, ctx: Context) -> List[FieldInterface]:
        return [f for f in self.get_fields(ctx) if getattr(f, "is_shown_on_import", lambda: False)()]

    def creation_form_fields_parser(self, ctx: Context, fields: List[Any]) -> List[Any]:
        result = []
        for field in fields:
            if hasattr(field, "body"):
                body = getattr(field, "body")
                parsed_body = self.creation_form_fields_parser(ctx, body)
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
                                    item.body = self.creation_form_fields_parser(ctx, item.body)
                                else:
                                    item.body.build_frontend_rules(ctx.path)
                    if field.is_shown_on_creation():
                        field.build_frontend_rules(ctx.path)
                        result.append(field)
                else:
                    result.append(field)
        return result

    def update_form_fields_parser(self, ctx: Context, fields: List[Any]) -> List[Any]:
        result = []
        for field in fields:
            if hasattr(field, "body"):
                body = getattr(field, "body")
                parsed_body = self.update_form_fields_parser(ctx, body)
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
                                    item.body = self.update_form_fields_parser(ctx, item.body)
                                else:
                                    item.body.build_frontend_rules(ctx.path)
                    if field.is_shown_on_update():
                        field.build_frontend_rules(ctx.path)
                        result.append(field)
                else:
                    result.append(field)
        return result

    def detail_fields_parser(self, ctx: Context, init_api: Any, fields: List[Any], data: Dict[str, Any]) -> DescriptionsComponent:
        cols = []
        for field in fields:
            if hasattr(field, "body"):
                body = getattr(field, "body")
                parsed_body = self.detail_fields_parser(ctx, init_api, body, data)
                setattr(field, "body", parsed_body)
                cols.append(field)
            elif field.is_shown_on_detail():
                col = self._field_to_column(ctx, field)
                if col:
                    cols.append(col)

        return (
            DescriptionsComponent()
            .init()
            .set_style({"padding": "24px"})
            .set_init_api(init_api)
            .set_title("")
            .set_column(2)
            .set_columns(cols)
            .set_data_source(data)
            .set_actions(self.detail_actions(ctx))
        )

    def detail_actions(self, ctx: Context) -> List[Any]:
        return []