import pydantic
from typing import Optional, Type


class CreateAdvertisement(pydantic.BaseModel):
    title: str
    description: str
    user_name: str

class PatchAdvertisement(pydantic.BaseModel):
    title: Optional[str]
    description: Optional[str]
    user_name: Optional[str]

VALIDATION_CLASS = Type[CreateAdvertisement] | Type[PatchAdvertisement]