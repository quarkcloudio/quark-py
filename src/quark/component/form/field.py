from typing import List, Any
from .fields.id import ID
from .fields.hidden import Hidden
from .fields.text import Text
from .fields.textarea import Textarea
from .fields.password import Password
from .fields.radio import Radio
from .fields.radio import Option as RadioOption
from .fields.image_captcha import ImageCaptcha
from .fields.checkbox import Checkbox
from .fields.checkbox import Option as CheckboxOption
from .fields.date import Date
from .fields.date_range import DateRange
from .fields.datetime import Datetime
from .fields.datetime_range import DatetimeRange
from .fields.switch import Switch
from .fields.tree import Tree
from .fields.icon import Icon
from .fields.select import Select
from .fields.select import Option as SelectOption
from .fields.cascader import Cascader
from .fields.cascader import Option as CascaderOption
from .fields.image import Image
from .fields.file import File
from .fields.display import Display
from .fields.editor import Editor
from .fields.group import Group
from .fields.list import List as ListField
from .fields.map import Map
from .fields.geofence import Geofence
from .fields.month import Month
from .fields.number import Number
from .fields.quarter import Quarter
from .fields.search import Search
from .fields.time_range import TimeRange
from .fields.time import Time
from .fields.week import Week
from .fields.year import Year
from .fields.selects import Selects
from .fields.tree_select import TreeSelect
from .fields.space import Space
from .fields.compact import Compact
from .fields.fieldset import Fieldset
from .fields.dependency import Dependency
from .fields.transfer import Transfer
from .fields.sms_captcha import SmsCaptcha
from .fields.image_picker import ImagePicker
from .fields.action import Action


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

def id(*params) -> 'ID':
    """生成 ID 字段组件"""
    return field_parser(ID(), params, "")

def hidden(*params) -> 'Hidden':
    """生成隐藏字段组件"""
    return field_parser(Hidden(), params, "")

def text(*params) -> 'Text':
    """生成文本框字段组件"""
    return field_parser(Text(), params, "请输入")

def textarea(*params) -> 'Textarea':
    """生成文本域字段组件"""
    return field_parser(Textarea(), params, "请输入")

def password(*params) -> 'Password':
    """生成密码框字段组件"""
    return field_parser(Password(), params, "请输入")

def radio(*params) -> 'Radio':
    """生成单选框字段组件"""
    return field_parser(Radio(), params, "")

def radio_option(label: str, value: Any) -> 'RadioOption':
    """生成单选框选项"""
    return RadioOption(label=label, value=value)

def checkbox(*params) -> 'Checkbox':
    """生成多选框字段组件"""
    return field_parser(Checkbox(), params, "")

def checkbox_option(label: str, value: Any) -> 'CheckboxOption':
    """生成多选框选项"""
    return CheckboxOption(label=label, value=value)

def date(*params) -> 'Date':
    """生成日期字段组件"""
    return field_parser(Date(), params, "")

def date_range(*params) -> 'DateRange':
    """生成日期范围字段组件"""
    return field_parser(DateRange(), params, "")

def datetime(*params) -> 'Datetime':
    """生成日期时间字段组件"""
    return field_parser(Datetime(), params, "")

def datetime_range(*params) -> 'DatetimeRange':
    """生成日期时间范围字段组件"""
    return field_parser(DatetimeRange(), params, "")

def switch(*params) -> 'Switch':
    """生成开关字段组件"""
    return field_parser(Switch(), params, "")

def tree(*params) -> 'Tree':
    """生成树形选择字段组件"""
    return field_parser(Tree(), params, "请选择")

def icon(*params) -> 'Icon':
    """生成图标选择字段组件"""
    return field_parser(Icon(), params, "请选择")

def select(*params) -> 'Select':
    """生成下拉框字段组件"""
    return field_parser(Select(), params, "请选择")

def select_option(label: str, value: Any) -> 'SelectOption':
    """生成下拉框选项"""
    return SelectOption(label=label, value=value)

def cascader(*params) -> 'Cascader':
    """生成级联选择字段组件"""
    return field_parser(Cascader(), params, "请选择")

def image(*params) -> 'Image':
    """生成图片选择字段组件"""
    return field_parser(Image(), params, "")

def file(*params) -> 'File':
    """生成文件上传字段组件"""
    return field_parser(File(), params, "")

def display(*params: str) -> 'Display':
    """生成文本展示组件"""
    field = Display()
    if len(params) == 1:
        field.set_label(" ").set_value(params[0]).set_colon(False)
    elif len(params) == 2:
        field.set_label(params[0]).set_value(params[1])
    return field

def editor(*params) -> 'Editor':
    """生成富文本编辑器组件"""
    return field_parser(Editor(), params, "")

def group(*options) -> 'Group':
    """生成分组字段组件"""
    field = Group()

    if len(options) == 1:
        field.set_body(options[0])

    if len(options) == 2:
        field.set_title(options[0]).set_body(options[1])

    return field

def list(*params) -> 'ListField':
    """生成列表字段组件"""
    return field_parser(ListField(), params, "")

def map(*params) -> 'Map':
    """生成地图选择字段组件"""
    return field_parser(Map(), params, "")

def geofence(*params) -> 'Geofence':
    """生成地理围栏选择字段组件"""
    return field_parser(Geofence(), params, "")

def month(*params) -> 'Month':
    """生成月份选择字段组件"""
    return field_parser(Month(), params, "")

def number(*params) -> 'Number':
    """生成数字输入框字段组件"""
    return field_parser(Number(), params, "请输入")

def quarter(*params) -> 'Quarter':
    """生成季度选择字段组件"""
    return field_parser(Quarter(), params, "")

def search(*params) -> 'Search':
    """生成搜索字段组件"""
    return field_parser(Search(), params, "")

def time_range(*params) -> 'TimeRange':
    """生成时间范围字段组件"""
    return field_parser(TimeRange(), params, "")

def time(*params) -> 'Time':
    """生成时间选择字段组件"""
    return field_parser(Time(), params, "")

def week(*params) -> 'Week':
    """生成周选择字段组件"""
    return field_parser(Week(), params, "")

def year(*params) -> 'Year':
    """生成年份选择字段组件"""
    return field_parser(Year(), params, "")

def selects(body: Any) -> 'Selects':
    """生成联动选择组件"""
    field = Selects().set_body(body)
    return field

def tree_select(*params) -> 'TreeSelect':
    """生成树形选择联动组件"""
    return field_parser(TreeSelect(), params, "")

def space(*options) -> 'Space':
    """生成间距布局组件"""
    field = Space()

    if len(options) == 1:
        field.set_body(options[0])

    if len(options) == 2:
        field.set_label(options[0]).set_body(options[1])

    return field

def compact(label: str, items: List[Any]) -> 'Compact':
    """生成紧凑布局组件"""
    field = Compact().set_label(label).set_body(items)
    return field

def fieldset(*params) -> 'Fieldset':
    """生成字段集合组件"""
    return field_parser(Fieldset(), params, "")

def dependency() -> 'Dependency':
    """数据联动组件"""
    return Dependency()

def transfer(*params) -> 'Transfer':
    """穿梭框组件"""
    return field_parser(Transfer(), params, "")

def image_captcha(*params) -> 'ImageCaptcha':
    """图形验证码组件"""
    return field_parser(ImageCaptcha(), params, "")

def sms_captcha(*params) -> 'SmsCaptcha':
    """短信验证码组件"""
    return field_parser(SmsCaptcha(), params, "")

def image_picker(*params) -> 'ImagePicker':
    """图片选择器组件"""
    return field_parser(ImagePicker(), params, "")

def action(*params) -> 'Action':
    """行为组件"""
    return field_parser(Action(), params, "")