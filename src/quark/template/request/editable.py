from flask import request, jsonify
from your_app import db, app  # 替换为实际的 Flask 应用和数据库实例
from your_app.models import YourModel  # 替换为实际模型


class EditableRequest:
    def handle(self):
        data = request.args.to_dict()

        if not data:
            return jsonify({"error": "参数错误"}), 400

        id_val = data.get("id")
        if not id_val:
            return jsonify({"error": "id不能为空"}), 400

        model_instance = YourModel.query.get(id_val)
        if not model_instance:
            return jsonify({"error": "记录不存在"}), 400

        field = None
        value = None

        for k, v in data.items():
            if v == "true":
                v = 1
            elif v == "false":
                v = 0

            if k not in ["id", "_t"]:
                field = k
                value = v

        if not field or value is None:
            return jsonify({"error": "参数错误"}), 400

        # 表格行内编辑执行前回调（模板方法）
        before_result = self.before_editable(id_val, field, value)
        if before_result is not None:
            return before_result

        # 构建查询并更新数据
        try:
            update_data = {field: value}
            YourModel.query.filter_by(id=id_val).update(update_data)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 500

        # 行内编辑执行后回调
        after_result = self.after_editable(id_val, field, value)
        if after_result is not None:
            return after_result

        return jsonify({"message": "操作成功"})

    def before_editable(self, id_val, field, value):
        """
        行内编辑前回调，可重写实现自定义逻辑。
        返回非None值表示中断处理并返回响应。
        """
        return None

    def after_editable(self, id_val, field, value):
        """
        行内编辑后回调，可重写实现自定义逻辑。
        返回非None值表示中断处理并返回响应。
        """
        return None