from schemas.pydantic_config import BaseConfig
from pydantic import Field


class CreateObjResponse(BaseConfig):
    id: int = Field(strict=True, gt=0)


class CreateObjErrorResponse(BaseConfig):
    error: str = Field(strict=True)
