from typing import Any, List, Optional

from tortoise.queryset import QuerySet

from quark import Message, Request

from ..performs_queries import PerformsQueries


class ActionRequest:
    """
    处理资源行为请求
    """

    # 请求对象
    request: Request = None

    # 资源对象
    resource: Any = None

    # 查询对象
    query: QuerySet = None

    # 行为
    actions: Optional[Any] = None

    # 字段
    fields: Optional[Any] = None

    def __init__(
        self,
        request: Request,
        resource: Any,
        query: QuerySet,
        actions: Optional[Any],
        fields: Optional[Any],
    ):
        self.request = request
        self.resource = resource
        self.query = query
        self.actions = actions
        self.fields = fields

    def get_actions(self) -> List[Any]:
        """
        获取当前资源上定义的所有行为（包括资源级行为和字段级行为）。

        Returns:
            list: 返回行为列表。
        """
        actions = []

        # 资源上的行为
        if self.actions:
            actions.extend(self.actions)

        # 字段上的行为
        for field in self.fields:
            component = getattr(field, "component", None)
            if component == "actionField" and hasattr(field, "items"):
                action_items = getattr(field, "items", [])
                if isinstance(action_items, list):
                    actions.extend(action_items)

        return actions

    async def handle(self):
        """
        执行指定的行为。

        Returns:
            JSON 响应：成功或错误信息。
        """
        uri_key = self.request.path_params.get("uriKey")

        # 构建查询
        query = PerformsQueries(self.request).build_action_query(self.query)

        actions = self.get_actions()
        for action in actions:
            action_instance = action
            current_uri_key = action_instance.get_uri_key(action)
            action_type = action_instance.get_action_type()

            if action_type == "dropdown":
                dropdown_actioner = action
                for dropdown_action in dropdown_actioner.get_actions():
                    current_uri_key = dropdown_actioner.get_uri_key(dropdown_action)
                    if uri_key == current_uri_key:
                        # 执行前回调
                        try:
                            await self.resource.before_action(
                                self.request, uri_key, query
                            )
                        except Exception as e:
                            return Message.error(str(e))

                        result = await dropdown_action.handle(self.request, query)

                        # 执行后回调
                        try:
                            await self.resource.after_action(
                                self.request, uri_key, query
                            )
                        except Exception as e:
                            return Message.error(str(e))

                        return result
            else:
                if uri_key == current_uri_key:
                    try:
                        await self.resource.before_action(self.request, uri_key, query)
                    except Exception as e:
                        return Message.error(str(e))

                    result = await action.handle(self.request, query)

                    try:
                        # 执行后回调
                        await self.resource.after_action(self.request, uri_key, query)
                    except Exception as e:
                        return Message.error(str(e))

                    return result

        return result

    async def values(self):
        """
        获取行为对应的表单数据。

        Returns:
            JSON 响应：返回行为相关的数据。
        """
        uri_key = self.request.path_params.get("uriKey")
        data = {}
        actions = self.get_actions()

        for action in actions:
            action_instance = action
            current_uri_key = action_instance.get_uri_key(action)
            action_type = action_instance.get_action_type()

            if action_type == "dropdown":
                dropdown_actioner = action
                for dropdown_action in dropdown_actioner.get_actions():
                    current_uri_key = dropdown_actioner.get_uri_key(dropdown_action)
                    if uri_key == current_uri_key:
                        data = await dropdown_action.data(self.request)

            else:
                if uri_key == current_uri_key:
                    data = await action.data(self.request)

        return Message.success("获取成功", data)
