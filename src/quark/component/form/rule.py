from pydantic import Field
from ..component import Component
from typing import Any, List, Optional


class Rule(Component):
    """
    表单验证规则
    """

    # 需要验证的字段名称
    name: str = Field(None, exclude=True)

    # 规则类型，max | min | unique | required
    rule_type: str = Field(None, exclude=True)

    # 仅在 type 为 array 类型时有效，用于指定数组元素的校验规则
    default_field: Optional[Any] = None

    # 是否匹配枚举中的值（需要将 type 设置为 enum）
    enum: List[Any] = None

    # 仅在 type 为 array 或 object 类型时有效，用于指定子元素的校验规则
    fields: Optional[Any] = None

    # string 类型时为字符串长度；number 类型时为确定数字； array 类型时为数组长度
    length: int = None

    # 必须设置 type：string 类型为字符串最大长度；number 类型时为最大值；array 类型时为数组最大长度
    max_value: int = Field(alias="max", default=None)

    # 错误信息，不设置时会通过模板自动生成
    message: str = None

    # 必须设置 type：string 类型为字符串最小长度；number 类型时为最小值；array 类型时为数组最小长度
    min_value: int = Field(alias="min", default=None)

    # 正则表达式匹配
    pattern: str = None

    # 是否为必选字段
    required_value: bool = Field(alias="required", default=None)

    # type：unique时，指定验证的表名
    unique_table: str = Field(None, exclude=True)

    # type：unique时，指定需验证表中的字段
    unique_table_field: str = Field(None, exclude=True)

    # type：unique时，忽略符合条件验证的列，例如：{id}
    unique_ignore_value: str = Field(None, exclude=True)

    # 字段类型，string | number | boolean | method | regexp | integer | float | array | object | enum | date | url | hex | email | any
    rule_type_field: str = None

    # 转换前端验证规则，剔除前端不支持的 unique
    @staticmethod
    def convert_to_frontend_rules(rules: List["Rule"]) -> List["Rule"]:
        return [rule for rule in rules if rule.rule_type != "unique"]

    # 必须设置 type：string 类型；为字符串最大长度；number 类型时为最大值；array 类型时为数组最大长度
    @staticmethod
    def max(max_value: int, message: str) -> "Rule":
        rule = Rule()
        return rule.set_max(max_value).set_message(message)

    # 必须设置 type：string 类型为字符串最小长度；number 类型时为最小值；array 类型时为数组最小长度
    @staticmethod
    def min(min_value: int, message: str) -> "Rule":
        rule = Rule()
        return rule.set_min(min_value).set_message(message)

    # 正则表达式匹配
    @staticmethod
    def regexp(pattern: str, message: str) -> "Rule":
        rule = Rule()
        return rule.set_regexp(pattern).set_message(message)

    # 必须为字符串
    @staticmethod
    def string(message: str) -> "Rule":
        rule = Rule()
        return rule.set_string().set_message(message)

    # 必须为数字
    @staticmethod
    def number(message: str) -> "Rule":
        rule = Rule()
        return rule.set_number().set_message(message)

    # 必须为布尔类型
    @staticmethod
    def boolean(message: str) -> "Rule":
        rule = Rule()
        return rule.set_boolean().set_message(message)

    # 必须为整型
    @staticmethod
    def integer(message: str) -> "Rule":
        rule = Rule()
        return rule.set_integer().set_message(message)

    # 必须为浮点型
    @staticmethod
    def float(message: str) -> "Rule":
        rule = Rule()
        return rule.set_float().set_message(message)

    # 必须为邮箱字段
    @staticmethod
    def email(message: str) -> "Rule":
        rule = Rule()
        return rule.set_email().set_message(message)

    # 必须为链接
    @staticmethod
    def url(message: str) -> "Rule":
        rule = Rule()
        return rule.set_url().set_message(message)

    # 必须为手机号
    @staticmethod
    def phone(message: str) -> "Rule":
        rule = Rule()
        return rule.set_phone().set_message(message)

    # 是否为必选字段
    @staticmethod
    def required(message: str) -> "Rule":
        rule = Rule()
        return rule.set_required().set_message(message)

    # 设置 unique 验证类型，插入数据时：Unique("admins", "username", "用户名已存在")，更新数据时：Unique("admins", "username", "{id}", "用户名已存在")
    @staticmethod
    def unique(*unique: str) -> "Rule":
        rule = Rule()
        if len(unique) == 3:
            unique_table, unique_table_field, message = unique
            rule.set_unique(unique_table, unique_table_field)
        elif len(unique) == 4:
            unique_table, unique_table_field, unique_ignore_value, message = unique
            rule.set_unique(unique_table, unique_table_field, unique_ignore_value)
        rule.set_message(message)
        return rule

    # 需要验证的字段名称
    def set_name(self, name: str) -> "Rule":
        self.name = name
        return self

    # 必须设置 type：string 类型；为字符串最大长度；number 类型时为最大值；array 类型时为数组最大长度
    def set_max(self, max_value: int) -> "Rule":
        self.max_value = max_value
        return self.set_rule_type("max")

    # 错误信息，不设置时会通过模板自动生成
    def set_message(self, message: str) -> "Rule":
        self.message = message
        return self

    # 必须设置 type：string 类型为字符串最小长度；number 类型时为最小值；array 类型时为数组最小长度
    def set_min(self, min_value: int) -> "Rule":
        self.min_value = min_value
        return self.set_rule_type("min")

    # 正则表达式匹配
    def set_regexp(self, pattern: str) -> "Rule":
        self.pattern = pattern
        return self.set_rule_type("regexp")

    # 是否为必选字段
    def set_required(self) -> "Rule":
        self.required_value = True
        return self.set_rule_type("required")

    # 必须为字符串
    def set_string(self) -> "Rule":
        self.rule_type_field = "string"
        return self.set_rule_type("string")

    # 必须为数字
    def set_number(self) -> "Rule":
        self.rule_type_field = "number"
        return self.set_rule_type("number")

    # 必须为布尔类型
    def set_boolean(self) -> "Rule":
        self.rule_type_field = "boolean"
        return self.set_rule_type("boolean")

    # 必须为整型
    def set_integer(self) -> "Rule":
        self.rule_type_field = "integer"
        return self.set_rule_type("integer")

    # 必须为浮点型
    def set_float(self) -> "Rule":
        self.rule_type_field = "float"
        return self.set_rule_type("float")

    # 必须为邮箱字段
    def set_email(self) -> "Rule":
        self.rule_type_field = "email"
        return self.set_rule_type("email")

    # 必须为链接
    def set_url(self) -> "Rule":
        self.rule_type_field = "url"
        return self.set_rule_type("url")

    # 必须为手机号
    def set_phone(self) -> "Rule":
        return self.set_regexp(r"^1[3-9]\d{9}$")

    # 设置 unique 验证类型，插入数据：SetUnique("admins","username")，更新数据：SetUnique("admins","username","{id}")
    def set_unique(self, *unique: str) -> "Rule":
        self.rule_type_field = "unique"
        if len(unique) == 2:
            self.unique_table, self.unique_table_field = unique
        elif len(unique) == 3:
            self.unique_table, self.unique_table_field, self.unique_ignore_value = (
                unique
            )
        return self.set_rule_type("unique")

    # type：unique时，指定验证的表名
    def set_unique_table(self, unique_table: str) -> "Rule":
        self.unique_table = unique_table
        return self

    # type：unique时，指定验证的表名
    def set_unique_table_field(self, unique_table_field: str) -> "Rule":
        self.unique_table_field = unique_table_field
        return self

    # type：unique时，忽略符合条件验证的列，例如：{id}
    def set_unique_ignore_value(self, unique_ignore_value: str) -> "Rule":
        self.unique_ignore_value = unique_ignore_value
        return self

    # 字段类型，string | number | boolean | url | email
    def set_type(self, rule_type_field: str) -> "Rule":
        self.rule_type_field = rule_type_field
        return self

    # 规则类型，max | min | unique | required
    def set_rule_type(self, rule_type: str) -> "Rule":
        self.rule_type = rule_type
        return self
