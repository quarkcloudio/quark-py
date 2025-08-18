import uuid
from typing import List

from ..models.menu import Menu


class MenuService:
    def __init__(self, guard_name: str = "admin"):
        self.guard_name = guard_name

    def set_guard_name(self, guard_name: str):
        self.guard_name = guard_name
        return self

    async def get_list(self) -> List[Menu]:
        menus = (
            await Menu.filter(guard_name=self.guard_name, status=1)
            .order_by("sort", "id")
            .all()
        )
        return menus

    async def get_list_with_root(self):
        menus = await self.get_list()
        menus.append(Menu(id=0, pid=-1, name="根节点"))
        return menus

    async def find_parent_tree_node(self, child_pid: int):
        menus = await Menu.filter(
            guard_name=self.guard_name, id=child_pid, status=1, type__in=[1, 2, 3]
        ).all()
        if not menus:
            return menus

        result = []
        for menu in menus:
            if menu.pid != 0:
                children = await self.find_parent_tree_node(menu.pid)
                result.extend(children)
            result.append(menu)

        return result

    async def get_list_by_user_id(self, user_id: int):
        if user_id == 1:
            menus = (
                await Menu.filter(
                    guard_name=self.guard_name, status=1, type__in=[1, 2, 3]
                )
                .order_by("sort")
                .all()
            )
            return await self.menu_parser(menus)

        # role_has_menus = await CasbinService().get_user_menus(user_id)
        # TODO: 这里需要替换为实际的获取用户菜单的方法
        role_has_menus = []
        if not role_has_menus:
            return []

        menu_ids = [menu.id for menu in role_has_menus]

        menus = (
            await Menu.filter(
                guard_name=self.guard_name,
                status=1,
                id__in=menu_ids,
                type__in=[1, 2, 3],
            )
            .exclude(pid=0)
            .all()
        )

        for menu in menus:
            parent_menus = await self.find_parent_tree_node(menu.pid)
            for parent in parent_menus:
                if parent.id not in menu_ids:
                    menu_ids.append(parent.id)

        all_menus = (
            await Menu.filter(guard_name=self.guard_name, status=1, id__in=menu_ids)
            .order_by("sort")
            .all()
        )

        return await self.menu_parser(all_menus)

    async def menu_parser(self, menus):
        new_menus = []
        for menu in menus:
            menu.key = str(uuid.uuid4())
            menu.locale = "menu" + menu.path.replace("/", ".") if menu.path else ""

            menu.hide_in_menu = False if menu.show == 1 else True

            if menu.type == 2 and menu.is_engine == 1:
                menu.path = "/layout/index?api=" + menu.path

            if not self.has_menu(new_menus, menu.id) and menu.type != 3:
                new_menus.append(menu)

        return self.list_to_tree(new_menus, "id", "pid", "routes", 0)

    def has_menu(self, menus, menu_id):
        return any(menu.id == menu_id for menu in menus)

    async def get_info_by_id(self, menu_id: int):
        menu = await Menu.filter(status=1, id=menu_id).first()
        return menu

    async def get_info_by_name(self, name: str):
        menu = await Menu.filter(status=1, name=name).first()
        return menu

    async def is_exist(self, menu_id: int):
        menu = await Menu.filter(id=menu_id).first()
        return bool(menu)

    async def get_list_by_ids(self, menu_ids):
        menus = await Menu.filter(id__in=menu_ids).all()
        return menus

    def list_to_tree(self, items, id_key, parent_key, children_key, root_id):
        tree = []
        lookup = {}

        for item in items:
            item_dict = item.__dict__.copy()
            item_dict.pop("_state", None)
            lookup[item_dict[id_key]] = item_dict
            item_dict[children_key] = []

        for item in items:
            item_dict = lookup[item.id]
            parent_id = item_dict[parent_key]
            if parent_id == root_id:
                tree.append(item_dict)
            else:
                if parent_id in lookup:
                    lookup[parent_id][children_key].append(item_dict)

        return tree
