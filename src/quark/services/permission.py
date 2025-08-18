from typing import List

from quark.models.menu_has_permission import MenuHasPermission
from quark.models.role_has_permission import RoleHasPermission

from ..component.form.fields.transfer import DataSource
from ..models.permission import Permission


class PermissionService:
    def __init__(self):
        pass

    async def list(self):
        permissions = await Permission.all()
        list_options = [
            {"label": permission.name, "value": permission.id}
            for permission in permissions
        ]
        return list_options

    async def data_source(self):
        permissions = await Permission.all()
        data_source = [
            DataSource(
                key=permission.id,
                title=permission.name,
                description=permission.remark,
            )
            for permission in permissions
        ]
        return data_source

    async def get_list_by_ids(self, permission_ids):
        permissions = await Permission.filter(id__in=permission_ids).all()
        return permissions

    async def get_list_by_names(self, permission_names):
        permissions = await Permission.filter(name__in=permission_names).all()
        return permissions

    async def get_menu_permissions(self, menu_id: int):
        permissions = await MenuHasPermission.filter(menu_id=menu_id).all()
        return permissions

    async def get_permissions_by_role_ids(self, role_ids: List[int]):
        permissions = await RoleHasPermission.filter(role_id__in=role_ids).all()
        return permissions

    async def add_menu_permission(self, menu_id: int, permission_ids: List[int]):
        await MenuHasPermission.filter(menu_id=menu_id).delete()
        await MenuHasPermission.bulk_create(
            [
                MenuHasPermission(menu_id=menu_id, permission_id=permission_id)
                for permission_id in permission_ids
            ]
        )
