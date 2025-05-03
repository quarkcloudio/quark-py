from typing import List, Any
from .fields.when import Component as When
from .fields.text import Component as Text
from .fields.password import Component as Password
from .fields.image_captcha import Component as ImageCaptcha

def field_parser(field: Any, params: List[Any], placeholder: str) -> Any:
    """
    解析字段参数，并设置字段的相应属性。

    :param field: 字段组件
    :param params: 参数列表，可能包括名称、标签、回调等
    :param placeholder: 占位符，默认为空
    :return: 更新后的字段组件
    """
    if len(params) == 1:
        field.name = str(params[0])
    elif len(params) == 2:
        field.name = str(params[0])
        field.label = str(params[1])
    elif len(params) == 3:
        field.name = str(params[0])
        field.label = str(params[1])

        if callable(params[2]):
            field.callback = params[2]

    if placeholder and len(params) > 1:
        field.placeholder = placeholder + str(params[1])

    return field

def id(*params) -> 'IDComponent':
    """生成 ID 字段组件"""
    return field_parser(IDComponent(), params, "")

def hidden(*params) -> 'HiddenComponent':
    """生成隐藏字段组件"""
    return field_parser(HiddenComponent(), params, "")

def text(*params) -> 'Text':
    """生成文本框字段组件"""
    return field_parser(Text(), params, "请输入")

def text_area(*params) -> 'TextAreaComponent':
    """生成文本域字段组件"""
    return field_parser(TextAreaComponent(), params, "请输入")

def password(*params) -> 'Password':
    """生成密码框字段组件"""
    return field_parser(Password(), params, "请输入")

def radio(*params) -> 'RadioComponent':
    """生成单选框字段组件"""
    return field_parser(RadioComponent(), params, "")

def radio_option(label: str, value: Any) -> 'RadioOption':
    """生成单选框选项"""
    return RadioOption(label=label, value=value)

def checkbox(*params) -> 'CheckboxComponent':
    """生成多选框字段组件"""
    return field_parser(CheckboxComponent(), params, "")

def checkbox_option(label: str, value: Any) -> 'CheckboxOption':
    """生成多选框选项"""
    return CheckboxOption(label=label, value=value)

def date(*params) -> 'DateComponent':
    """生成日期字段组件"""
    return field_parser(DateComponent(), params, "")

def date_range(*params) -> 'DateRangeComponent':
    """生成日期范围字段组件"""
    return field_parser(DateRangeComponent(), params, "")

def datetime(*params) -> 'DatetimeComponent':
    """生成日期时间字段组件"""
    return field_parser(DatetimeComponent(), params, "")

def datetime_range(*params) -> 'DatetimeRangeComponent':
    """生成日期时间范围字段组件"""
    return field_parser(DatetimeRangeComponent(), params, "")

def switch(*params) -> 'SwitchComponent':
    """生成开关字段组件"""
    return field_parser(SwitchComponent(), params, "")

def tree(*params) -> 'TreeComponent':
    """生成树形选择字段组件"""
    return field_parser(TreeComponent(), params, "请选择")

def icon(*params) -> 'IconComponent':
    """生成图标选择字段组件"""
    return field_parser(IconComponent(), params, "请选择")

def select(*params) -> 'SelectComponent':
    """生成下拉框字段组件"""
    return field_parser(SelectComponent(), params, "请选择")

def select_option(label: str, value: Any) -> 'SelectOption':
    """生成下拉框选项"""
    return SelectOption(label=label, value=value)

def cascader(*params) -> 'CascaderComponent':
    """生成级联选择字段组件"""
    return field_parser(CascaderComponent(), params, "请选择")

def image(*params) -> 'ImageComponent':
    """生成图片选择字段组件"""
    return field_parser(ImageComponent(), params, "")

def file(*params) -> 'FileComponent':
    """生成文件上传字段组件"""
    return field_parser(FileComponent(), params, "")

def display(*params: str) -> 'DisplayComponent':
    """生成文本展示组件"""
    field = DisplayComponent()
    if len(params) == 1:
        field.set_label(" ").set_value(params[0]).set_colon(False)
    elif len(params) == 2:
        field.set_label(params[0]).set_value(params[1])
    return field

def editor(*params) -> 'EditorComponent':
    """生成富文本编辑器组件"""
    return field_parser(EditorComponent(), params, "")

def group(*options) -> 'GroupComponent':
    """生成分组字段组件"""
    field = GroupComponent()

    if len(options) == 1:
        field.set_body(options[0])

    if len(options) == 2:
        field.set_title(options[0]).set_body(options[1])

    return field

def list(*params) -> 'ListComponent':
    """生成列表字段组件"""
    return field_parser(ListComponent(), params, "")

def map(*params) -> 'MapComponent':
    """生成地图选择字段组件"""
    return field_parser(MapComponent(), params, "")

def geofence(*params) -> 'GeofenceComponent':
    """生成地理围栏选择字段组件"""
    return field_parser(GeofenceComponent(), params, "")

def month(*params) -> 'MonthComponent':
    """生成月份选择字段组件"""
    return field_parser(MonthComponent(), params, "")

def number(*params) -> 'NumberComponent':
    """生成数字输入框字段组件"""
    return field_parser(NumberComponent(), params, "请输入")

def quarter(*params) -> 'QuarterComponent':
    """生成季度选择字段组件"""
    return field_parser(QuarterComponent(), params, "")

def search(*params) -> 'SearchComponent':
    """生成搜索字段组件"""
    return field_parser(SearchComponent(), params, "")

def time_range(*params) -> 'TimeRangeComponent':
    """生成时间范围字段组件"""
    return field_parser(TimeRangeComponent(), params, "")

def time(*params) -> 'TimeComponent':
    """生成时间选择字段组件"""
    return field_parser(TimeComponent(), params, "")

def week(*params) -> 'WeekComponent':
    """生成周选择字段组件"""
    return field_parser(WeekComponent(), params, "")

def year(*params) -> 'YearComponent':
    """生成年份选择字段组件"""
    return field_parser(YearComponent(), params, "")

def selects(body: Any) -> 'SelectsComponent':
    """生成联动选择组件"""
    field = SelectsComponent().set_body(body)
    return field

def tree_select(*params) -> 'TreeSelectComponent':
    """生成树形选择联动组件"""
    return field_parser(TreeSelectComponent(), params, "")

def space(*options) -> 'SpaceComponent':
    """生成间距布局组件"""
    field = SpaceComponent()

    if len(options) == 1:
        field.set_body(options[0])

    if len(options) == 2:
        field.set_label(options[0]).set_body(options[1])

    return field

def compact(label: str, items: List[Any]) -> 'CompactComponent':
    """生成紧凑布局组件"""
    field = CompactComponent().set_label(label).set_body(items)
    return field

def field_set(*params) -> 'FieldSetComponent':
    """生成字段集合组件"""
    return field_parser(FieldSetComponent(), params, "")

def dependency() -> 'DependencyComponent':
    """数据联动组件"""
    return DependencyComponent()

def transfer(*params) -> 'TransferComponent':
    """穿梭框组件"""
    return field_parser(TransferComponent(), params, "")

def image_captcha(*params) -> 'ImageCaptcha':
    """图形验证码组件"""
    return field_parser(ImageCaptcha(), params, "")

def sms_captcha(*params) -> 'SmsCaptchaComponent':
    """短信验证码组件"""
    return field_parser(SmsCaptchaComponent(), params, "")

def image_picker(*params) -> 'ImagePickerComponent':
    """图片选择器组件"""
    return field_parser(ImagePickerComponent(), params, "")

def sku(*params) -> 'SkuComponent':
    """商品Sku组件"""
    return field_parser(SkuComponent(), params, "")

def action(*params) -> 'ActionComponent':
    """行为组件"""
    return field_parser(ActionComponent(), params, "")