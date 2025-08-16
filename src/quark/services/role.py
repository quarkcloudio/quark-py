from typing import List, Optional

from tortoise.transactions import in_transaction

from quark.component.form.fields.checkbox import Option
from quark.models.menu_has_permission import MenuHasPermission
from quark.models.role_has_menu import RoleHasMenu
from quark.models.role_has_permission import RoleHasPermission

from ..models import Role, UserHasRole


class RoleService:
    def __init__(self):
        pass

    async def get_info_by_id(self, role_id: int) -> Optional[Role]:
        role = await Role.get(id=role_id)
        return role

    async def update_role_data_scope(
        self, role_id: int, data_scope: int, department_ids: List[int]
    ) -> None:
        async with in_transaction() as connection:
            role = await Role.get(id=role_id)
            role.data_scope = data_scope
            await role.save(using_db=connection)

            if data_scope == 2:
                await self.add_department_to_role(role_id, department_ids, connection)
            else:
                await self.remove_role_departments(role_id)

    async def get_list(self) -> List[Option]:
        roles = await Role.filter(status=1).all()
        options = [Option(label=role.name, value=role.id) for role in roles]
        return options

    async def get_list_by_ids(self, ids: List[int]) -> List[Role]:
        roles = await Role.filter(id__in=ids).all()
        return roles

    async def save_roles_by_user_id(self, user_id: int, role_ids: List[int]):
        async with in_transaction() as connection:
            # 删除用户原有的角色
            await UserHasRole.filter(uid=user_id).delete()  # 移除 using_db 参数

            # 保存新的角色
            for role_id in role_ids:
                user_role = UserHasRole(uid=user_id, role_id=role_id)
                await user_role.save(using_db=connection)

    async def get_role_ids_by_user_id(self, user_id: int) -> List[int]:
        user_roles = await UserHasRole.filter(uid=user_id).all()
        return [user_role.role_id for user_role in user_roles]

    async def get_menu_ids_by_role_id(self, role_id: int) -> List[int]:
        role_menus = await RoleHasMenu.filter(role_id=role_id).all()
        return [role_menu.menu_id for role_menu in role_menus]

    async def save_menus_by_role_id(
        self, role_id: int, menu_ids: List[int]
    ) -> List[int]:
        await RoleHasMenu.filter(role_id=role_id).delete()
        await RoleHasPermission.filter(role_id=role_id).delete()
        for menu_id in menu_ids:
            role_menu = RoleHasMenu(role_id=role_id, menu_id=menu_id)
            await role_menu.save()
            menu_permissions = await MenuHasPermission.filter(menu_id=menu_id).all()
            for menu_permission in menu_permissions:
                role_permission = RoleHasPermission(
                    role_id=role_id, permission_id=menu_permission.permission_id
                )
                await role_permission.save()

    async def add_department_to_role(
        self, role_id: int, department_ids: List[int], connection=None
    ):
        # 这里你需要实现具体逻辑，比如插入 RoleDepartment 关联表
        pass

    async def remove_role_departments(self, role_id: int, connection=None):
        # 这里你需要实现具体逻辑，比如删除 RoleDepartment 关联表里对应数据
        pass
