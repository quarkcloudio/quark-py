from typing import List, Optional, Tuple
from ..models.department import Department
from tortoise.expressions import Q


class DepartmentService:
    def __init__(self):
        pass

    async def get_children_ids(self, pid: int) -> List[int]:
        departments = await Department.filter(pid=pid, status=1).all()
        if not departments:
            return []

        ids = []
        for department in departments:
            children_ids = await self.get_children_ids(department.id)
            if children_ids:
                ids.extend(children_ids)
            ids.append(department.id)
        return ids

    async def get_children_departments(self, pid: int) -> List[Department]:
        departments = await Department.filter(pid=pid, status=1).all()
        if not departments:
            return []

        children_departments = []
        for department in departments:
            children = await self.get_children_departments(department.id)
            if children:
                children_departments.extend(children)
            children_departments.append(department)
        return children_departments

    async def get_info_by_id(
        self, department_id: int
    ) -> Tuple[Optional[Department], Optional[Exception]]:
        department = await Department.filter(status=1, id=department_id).first()
        if department:
            return department
        return None

    async def get_list(self) -> List[Department]:
        departments = await Department.filter(status=1).all()
        return departments

    async def get_list_by_ids(self, ids: List[int]) -> List[Department]:
        departments = await Department.filter(Q(id__in=ids), status=1).all()
        return departments
