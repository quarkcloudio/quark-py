from pydantic import model_validator
from .base import Base


class Fieldset(Base):

    component: str = "fieldsetField"

    @model_validator(mode="after")
    def init(self):
        self.only_on_forms()
        self.set_key()
        return self
