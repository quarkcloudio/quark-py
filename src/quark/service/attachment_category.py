from ..db import db
from ..model.attachment_category import AttachmentCategory

# AttachmentCategoryService类
class AttachmentCategoryService:
    def __init__(self):
        pass

    def get_list(self, admin_id):
        categories = []
        db.session.query(AttachmentCategory).\
            filter_by(source="ADMIN").\
            filter_by(uid=admin_id).\
            all()

        return categories