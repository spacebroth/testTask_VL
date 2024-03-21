from schemas.pydantic_config import BaseConfig
from pydantic import Field


class VersionValue(BaseConfig):
    major: int = Field(strict=True, gt=0)
    minor: int = Field(strict=True, gt=0)


class GetVersionResponse(BaseConfig):
    version: VersionValue
