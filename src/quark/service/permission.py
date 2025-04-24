from ..dal import db
from ..model.permission import Permission

# PermissionService类
class PermissionService:
    def __init__(self):
        pass

    def list(self):
        permissions = Permission.query.all()
        list_options = []

        for permission in permissions:
            option = {
                "label": permission.name,
                "value": permission.id
            }
            list_options.append(option)

        return list_options, None

    def data_source(self):
        permissions = Permission.query.all()
        data_source = []

        for permission in permissions:
            option = {
                "key": permission.id,
                "title": permission.name,
                "description": permission.remark
            }
            data_source.append(option)

        return data_source, None

    def get_list_by_ids(self, permission_ids):
        permissions = Permission.query.filter(Permission.id.in_(permission_ids)).all()
        return permissions, None

    def get_list_by_names(self, permission_names):
        permissions = Permission.query.filter(Permission.name.in_(permission_names)).all()
        return permissions, None
