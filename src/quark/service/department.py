from ..db import db
from ..model.department import Department

# DepartmentService类
class DepartmentService:
    def __init__(self):
        pass

    def get_children_ids(self, pid):
        departments = Department.query.filter_by(pid=pid, status=1).all()
        if not departments:
            return []

        ids = []
        for department in departments:
            children_ids = self.get_children_ids(department.id)
            if children_ids:
                ids.extend(children_ids)
            ids.append(department.id)
        return ids

    def get_children_departments(self, pid):
        departments = Department.query.filter_by(pid=pid, status=1).all()
        if not departments:
            return []

        children_departments = []
        for department in departments:
            children = self.get_children_departments(department.id)
            if children:
                children_departments.extend(children)
            children_departments.append(department)
        return children_departments

    def get_info_by_id(self, department_id):
        department = Department.query.filter_by(status=1, id=department_id).first()
        return department, None if department else ValueError("Department not found")

    def get_list(self):
        departments = Department.query.filter_by(status=1).all()
        return departments, None

    def get_list_by_ids(self, ids):
        departments = Department.query.filter(Department.id.in_(ids), Department.status == 1).all()
        return departments, None
