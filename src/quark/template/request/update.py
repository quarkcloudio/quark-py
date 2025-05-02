from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

# 模拟 Resourcer 接口
class ResourceTemplate:
    def get_model(self):
        raise NotImplementedError()

    def validator_for_update(self, ctx, data):
        return None

    def before_saving(self, ctx, data):
        return data, None

    def after_saved(self, ctx, id_value, data, model):
        pass

    def after_saved_redirect_to(self, ctx, id_value, data, err):
        if err:
            return jsonify({"error": str(err)}), 400
        return jsonify({"id": id_value, "data": data}), 200

    def build_update_query(self, ctx, query):
        return query


# 示例模型
class ExampleModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    metadata_json = db.Column(db.Text)


# 将字段名转为 PascalCase
def to_pascal_case(name: str) -> str:
    return ''.join(word.capitalize() for word in name.split('_'))


# UpdateRequest 类
class UpdateRequest:
    def handle(self, template: ResourceTemplate):
        # 解析数据
        try:
            data = request.get_json()
        except Exception as err:
            return jsonify({"error": str(err)}), 400

        # 验证参数合法性
        if not data.get("id"):
            return jsonify({"error": "参数错误"}), 400

        # 验证数据合法性
        validator = template.validator_for_update(request, data)
        if validator is not None:
            return jsonify({"error": validator.error()}), 400

        # 保存前回调
        modified_data, err = template.before_saving(request, data)
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

        # 获取对象并更新
        model_class = type(template.get_model())
        id_value = int(data["id"])
        model = model_class.query.get(id_value)
        if not model:
            return jsonify({"error": "记录不存在"}), 404

        # 构建查询
        query = template.build_update_query(request, model_class.query)

        # 更新数据
        for key, value in new_data.items():
            setattr(model, key, value)
        db.session.commit()

        # 保存后回调
        err = template.after_saved(request, id_value, data, model)
        return template.after_saved_redirect_to(request, id_value, data, err)