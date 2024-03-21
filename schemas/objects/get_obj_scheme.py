from typing import List
from schemas.pydantic_config import BaseConfig
from pydantic import Field, constr


class Price(BaseConfig):
    base: float = Field(strict=True, gt=0)
    discount: float = Field(strict=True, gt=0)


class Colors(BaseConfig):
    name: str = Field(strict=True)


class GetObjResponse(BaseConfig):
    id: int = Field(strict=True, gt=0)
    a: constr(max_length=64) | None

    #  и ЕСЛИ были бы другие поля объекта:
    field: str | None
    field2: Price  # к примеру, есть объекты
    field3: List[Colors]  # или есть массив объектов


class GetObjErrorResponse(BaseConfig):
    error: str = Field(strict=True)
