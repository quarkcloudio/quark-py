from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import json
from functools import wraps

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

# 模拟 Resourcer 接口
class ResourceTemplate:
    def get_model(self):
        raise NotImplementedError()

    def validator_for_creation(self, ctx, data):
        return None

    def before_saving(self, ctx, data):
        return data, None

    def after_saved(self, ctx, id_value, data, model):
        pass

    def after_saved_redirect_to(self, ctx, id_value, data, err):
        if err:
            return jsonify({"error": str(err)}), 400
        return jsonify({"id": id_value, "data": data}), 201


# 示例模型
class ExampleModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    metadata_json = db.Column(db.Text)


# 将字段名转为 PascalCase
def to_pascal_case(name: str) -> str:
    return ''.join(word.capitalize() for word in name.split('_'))


# StoreRequest 类
class StoreRequest:
    def handle(self, template: ResourceTemplate, data: dict):
        # 验证数据合法性
        validator = template.validator_for_creation(None, data)
        if validator is not None:
            return jsonify({"error": validator.error()}), 400

        # 保存前回调
        modified_data, err = template.before_saving(None, data)
        if err:
            return jsonify({"error": err}), 400

        # 重组数据
        new_data = {}
        model_instance = template.get_model()
        for k, v in modified_data.items():
            nv = v
            if isinstance(v, (list, dict)):
                nv = json.dumps(v)

            camel_case_name = to_pascal_case(k)
            field_exists = hasattr(model_instance, camel_case_name)
            if field_exists:
                new_data[k] = nv

        # 创建实例并赋值
        data_instance = template.get_model()
        for key, value in new_data.items():
            setattr(data_instance, key, value)
        db.session.add(data_instance)
        db.session.commit()

        # 获取 ID
        try:
            id_value = getattr(data_instance, "id")
        except AttributeError:
            return jsonify({"error": "参数错误"}), 400

        # 更新零值字段
        update_kwargs = {k: v for k, v in new_data.items()}
        db.session.query(type(data_instance)).filter_by(id=id_value).update(update_kwargs)
        db.session.commit()

        # 保存后回调
        err = template.after_saved(None, id_value, data, data_instance)
        return template.after_saved_redirect_to(None, id_value, data, err)