from ..db import db
from ..model.menu import Menu
import uuid

# 假设的CasbinService类
class CasbinService:
    def get_user_menus(self, user_id):
        # 这里添加实际的逻辑来获取用户菜单
        if user_id == 1:
            return [
                Menu(id=1, name="Dashboard", pid=0, guard_name="admin", status=1, sort=1, type=1, path="/dashboard"),
                Menu(id=2, name="Users", pid=0, guard_name="admin", status=1, sort=2, type=1, path="/users")
            ]
        return []

# MenuService类
class MenuService:
    def __init__(self, guard_name="admin"):
        self.guard_name = guard_name

    def set_guard_name(self, guard_name):
        self.guard_name = guard_name
        return self

    def get_list(self):
        menus = Menu.query.filter_by(guard_name=self.guard_name, status=1).order_by(Menu.sort.asc(), Menu.id.asc()).all()
        return menus, None

    def get_list_with_root(self):
        menus, err = self.get_list()
        if err:
            return menus, err

        menus.append(Menu(id=0, pid=-1, name="根节点"))
        return menus, None

    def find_parent_tree_node(self, child_pid):
        menus = Menu.query.filter_by(guard_name=self.guard_name, id=child_pid, status=1, type=db.or_(1, 2, 3)).all()

        if not menus:
            return menus

        for menu in menus:
            if menu.pid != 0:
                children = self.find_parent_tree_node(menu.pid)
                if children:
                    menus.extend(children)

        return menus

    def get_list_by_user_id(self, user_id):
        menus = []

        if user_id == 1:
            menus = Menu.query.filter_by(guard_name=self.guard_name, status=1, type=db.or_(1, 2, 3)).order_by(Menu.sort.asc()).all()
            return self.menu_parser(menus)

        role_has_menus = CasbinService().get_user_menus(user_id)
        if not role_has_menus:
            return [], None

        menu_ids = [menu.id for menu in role_has_menus]

        # 最底层列表
        menus = Menu.query.filter_by(guard_name=self.guard_name, status=1, id=db.or_(*menu_ids), type=db.or_(1, 2, 3), pid=db.not_(0)).all()

        for menu in menus:
            parent_menus = self.find_parent_tree_node(menu.pid)
            for parent_menu in parent_menus:
                menu_ids.append(parent_menu.id)

        # 所有列表
        menus = Menu.query.filter_by(guard_name=self.guard_name, status=1, id=db.or_(*menu_ids)).order_by(Menu.sort.asc()).all()

        return self.menu_parser(menus)

    def menu_parser(self, menus):
        new_menus = []
        for menu in menus:
            menu.key = str(uuid.uuid4())
            menu.locale = "menu" + menu.path.replace("/", ".")

            if menu.show == 1:
                menu.hide_in_menu = False
            else:
                menu.hide_in_menu = True

            if menu.type == 2 and menu.is_engine == 1:
                menu.path = "/layout/index?api=" + menu.path

            if not self.has_menu(new_menus, menu.id) and menu.type != 3:
                new_menus.append(menu)

        return self.list_to_tree(new_menus, "id", "pid", "routes", 0)

    def has_menu(self, menus, menu_id):
        for menu in menus:
            if menu.id == menu_id:
                return True
        return False

    def get_info_by_id(self, menu_id):
        menu = Menu.query.filter_by(status=1, id=menu_id).first()
        return menu, None if menu else ValueError("Menu not found")

    def get_info_by_name(self, name):
        menu = Menu.query.filter_by(status=1, name=name).first()
        return menu, None if menu else ValueError("Menu not found")

    def is_exist(self, menu_id):
        menu = Menu.query.filter_by(id=menu_id).first()
        if menu:
            return True
        return False

    def get_list_by_ids(self, menu_ids):
        menus = Menu.query.filter(Menu.id.in_(menu_ids)).all()
        return menus, None

    def list_to_tree(self, items, id_key, parent_key, children_key, root_id):
        tree = []
        lookup = {}

        for item in items:
            item_dict = item.__dict__.copy()
            item_dict.pop('_sa_instance_state', None)
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
