from flask import request, jsonify
from typing import List, Dict, Any, Optional
from your_app.models import db  # 假设你已经配置好 Flask-SQLAlchemy 的 db 实例


class ActionRequest:
    """
    处理资源行为请求，兼容 Flask 框架与 SQLAlchemy。
    """

    def __init__(self, template):
        self.template = template  # 当前资源模板实例

    def get_actions(self) -> List[Any]:
        """
        获取当前资源上定义的所有行为（包括资源级行为和字段级行为）。

        Returns:
            list: 返回行为列表。
        """
        actions = []

        # 资源上的行为
        resource_actions = self.template.actions()
        if resource_actions:
            actions.extend(resource_actions)

        # 字段上的行为
        fields = self.template.fields()
        for field in fields:
            component = getattr(field, 'component', None)
            if component == "actionField" and hasattr(field, 'items'):
                action_items = getattr(field, 'items', [])
                if isinstance(action_items, list):
                    actions.extend(action_items)

        return actions

    def handle(self):
        """
        执行指定的行为。

        Returns:
            JSON 响应：成功或错误信息。
        """
        uri_key = request.args.get("uriKey")
        if not uri_key:
            return jsonify({"error": "缺少 uriKey"}), 400

        model_instance = self.template.get_model()  # 获取模型类
        query = db.session.query(model_instance)

        # 构建查询条件
        query = self.template.build_action_query(request, query)

        actions = self.get_actions()
        for action in actions:
            action_instance = action
            action_instance.new(request)
            action_instance.init()

            current_uri_key = action_instance.get_uri_key(action)
            action_type = action_instance.get_action_type()

            if action_type == "dropdown":
                dropdown_actioner = action
                for dropdown_action in dropdown_actioner.get_actions():
                    current_uri_key = dropdown_actioner.get_uri_key(dropdown_action)
                    if uri_key == current_uri_key:
                        # 执行前回调
                        before_err = self.template.before_action(request, uri_key, query)
                        if before_err:
                            return jsonify({"error": before_err}), 400

                        result = dropdown_action.handle(request, query)

                        # 执行后回调
                        self.template.after_action(request, uri_key, query)

                        return result or jsonify({"success": True})
            else:
                if uri_key == current_uri_key:
                    # 执行前回调
                    before_err = self.template.before_action(request, uri_key, query)
                    if before_err:
                        return jsonify({"error": before_err}), 400

                    result = action.handle(request, query)

                    # 执行后回调
                    self.template.after_action(request, uri_key, query)

                    return result or jsonify({"success": True})

        return jsonify({"error": "未找到匹配的行为"}), 404

    def values(self):
        """
        获取行为对应的表单数据。

        Returns:
            JSON 响应：返回行为相关的数据。
        """
        uri_key = request.args.get("uriKey")
        if not uri_key:
            return jsonify({"error": "缺少 uriKey"}), 400

        data = {}
        actions = self.get_actions()

        for action in actions:
            action_instance = action
            action_instance.new(request)
            action_instance.init()

            current_uri_key = action_instance.get_uri_key(action)
            action_type = action_instance.get_action_type()

            if action_type == "dropdown":
                dropdown_actioner = action
                for dropdown_action in dropdown_actioner.get_actions():
                    current_uri_key = dropdown_actioner.get_uri_key(dropdown_action)
                    if uri_key == current_uri_key:
                        data = dropdown_action.data(request)
            else:
                if uri_key == current_uri_key:
                    data = action.data(request)

        return jsonify({"message": "获取成功", "data": data})