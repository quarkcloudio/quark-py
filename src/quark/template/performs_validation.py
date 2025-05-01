import re
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'  # 示例数据库配置
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# 模拟规则类
class Rule:
    def __init__(self, name, rule_type, message="", **kwargs):
        self.name = name
        self.rule_type = rule_type
        self.message = message
        self.kwargs = kwargs

# 模拟 'when' 条件判断的类
class WhenItem:
    def __init__(self, condition_name, condition_operator, condition_option, body=None):
        self.condition_name = condition_name
        self.condition_operator = condition_operator
        self.condition_option = condition_option
        self.body = body

# 示例数据库模型
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

# 模拟模板类
class Template:

    def validator_for_creation(self, data):
        # 获取创建数据验证规则
        rules = self.rules_for_creation(data)

        # 验证数据是否合法
        validation_errors = self.validator(rules, data)

        # 创建请求验证完成后回调
        self.after_creation_validation(validation_errors)

        return validation_errors

    def validator(self, rules, data):
        validation_errors = []

        for rule in rules:
            field_value = data.get(rule.name)
            if rule.rule_type == "required" and not field_value:
                validation_errors.append(rule.message or f"{rule.name} is required.")
            elif rule.rule_type == "min" and len(field_value) < rule.kwargs['min']:
                validation_errors.append(rule.message or f"{rule.name} should be at least {rule.kwargs['min']} characters.")
            elif rule.rule_type == "max" and len(field_value) > rule.kwargs['max']:
                validation_errors.append(rule.message or f"{rule.name} should be at most {rule.kwargs['max']} characters.")
            elif rule.rule_type == "regexp" and not re.match(rule.kwargs['pattern'], field_value):
                validation_errors.append(rule.message or f"{rule.name} does not match the required pattern.")
            elif rule.rule_type == "unique":
                count = self.check_unique(rule.kwargs['model'], rule.kwargs['field'], field_value, rule.kwargs.get('ignore_value'))
                if count > 0:
                    validation_errors.append(rule.message or f"{rule.name} must be unique.")
        
        return validation_errors

    def rules_for_creation(self, data):
        # 假设获取字段和验证规则
        fields = self.creation_fields_without_when(data)
        rules = []

        for field in fields:
            rules.extend(self.get_rules_for_creation(field))

            # 检查 'when' 组件中的条件规则
            if hasattr(field, 'get_when'):
                when_component = field.get_when()
                if when_component:
                    for when_item in when_component:
                        if self.need_validate_when_rules(data, when_item):
                            rules.extend(self.get_rules_for_creation(when_item.body))

        return rules

    def need_validate_when_rules(self, data, when_item):
        # 根据条件判断是否需要验证规则
        value = data.get(when_item.condition_name)
        if value is None:
            return False

        if isinstance(value, str):
            if not value:
                return False

        result = False
        if when_item.condition_operator == "=":
            result = value == when_item.condition_option
        elif when_item.condition_operator == ">":
            result = value > when_item.condition_option
        elif when_item.condition_operator == "<":
            result = value < when_item.condition_option
        elif when_item.condition_operator == "<=":
            result = value <= when_item.condition_option
        elif when_item.condition_operator == ">=":
            result = value >= when_item.condition_option
        elif when_item.condition_operator == "has":
            if isinstance(value, list):
                result = any(option in value for option in when_item.condition_option)
            else:
                result = when_item.condition_option in value
        elif when_item.condition_operator == "in":
            result = value in when_item.condition_option
        return result

    def get_rules_for_creation(self, field):
        rules = []

        if hasattr(field, 'get_rules'):
            rules.extend(field.get_rules())
        
        if hasattr(field, 'get_creation_rules'):
            rules.extend(field.get_creation_rules())

        return rules

    def check_unique(self, model, field, value, ignore_value):
        # 使用 SQLAlchemy 检查唯一性
        count = 0
        try:
            if ignore_value:
                count = model.query.filter(model.id != ignore_value, getattr(model, field) == value).count()
            else:
                count = model.query.filter(getattr(model, field) == value).count()
        except NoResultFound:
            pass
        return count

    def after_creation_validation(self, validation_errors):
        # 这里可以添加验证后的回调逻辑
        pass

    # 模拟获取创建字段的方法
    def creation_fields_without_when(self, data):
        # 假设返回字段列表
        return []