from typing import List, Optional
from ..models.role import Role
from tortoise.transactions import in_transaction
from quark.component.form.fields.checkbox import Option


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
                await self.remove_role_departments(role_id, connection)

    async def get_list(self) -> List[Option]:
        roles = await Role.filter(status=1).all()
        options = [Option(label=role.name, value=role.id) for role in roles]
        return options

    async def get_list_by_ids(self, ids: List[int]) -> List[Role]:
        roles = await Role.filter(id__in=ids).all()
        return roles

    # 以下两个方法需要你补充实现（假设你有 RoleDepartment 关联表）
    async def add_department_to_role(
        self, role_id: int, department_ids: List[int], connection=None
    ):
        # 这里你需要实现具体逻辑，比如插入 RoleDepartment 关联表
        pass

    async def remove_role_departments(self, role_id: int, connection=None):
        # 这里你需要实现具体逻辑，比如删除 RoleDepartment 关联表里对应数据
        pass
