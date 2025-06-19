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
        return list_options, None

    async def data_source(self):
        permissions = await Permission.all()
        data_source = [
            {
                "key": permission.id,
                "title": permission.name,
                "description": permission.remark,
            }
            for permission in permissions
        ]
        return data_source, None

    async def get_list_by_ids(self, permission_ids):
        permissions = await Permission.filter(id__in=permission_ids).all()
        return permissions, None

    async def get_list_by_names(self, permission_names):
        permissions = await Permission.filter(name__in=permission_names).all()
        return permissions, None
