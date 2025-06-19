from ..models.attachment_category import AttachmentCategory


class AttachmentCategoryService:
    def __init__(self):
        pass

    async def get_list(self, admin_id):
        categories = await AttachmentCategory.filter(source="ADMIN", uid=admin_id).all()
        return categories
