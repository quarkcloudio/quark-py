from ..db import db
from ..model.role import Role
from typing import List, Optional

class RoleService:
    def __init__(self):
        pass

    def get_info_by_id(self, role_id: int) -> Optional[Role]:
        role = db.query(Role).filter(Role.id == role_id).first()
        return role

    def update_role_data_scope(self, role_id: int, data_scope: int, department_ids: List[int]) -> None:
        role = db.query(Role).filter(Role.id == role_id).first()
        if role:
            role.data_scope = data_scope
            db.commit()
            if data_scope == 2:
                self.add_department_to_role(role_id, department_ids)
            else:
                self.remove_role_departments(role_id)

    def list_roles(self) -> List[Role]:
        roles = db.query(Role).filter(Role.status == 1).all()
        return roles

    def get_list_by_ids(self, ids: List[int]) -> List[Role]:
        roles = db.query(Role).filter(Role.id.in_(ids)).all()
        return roles