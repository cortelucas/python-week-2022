from datetime import datetime
from typing import Optional

from fastapi import HTTPException, status
from pydantic import BaseModel, validator


class BeerOut(BaseModel):
    id: Optional[int]
    name: str
    style: str
    flavor: int
    image: int
    cost: int
    rate: int
    date: datetime


class BeerIn(BaseModel):
    name: str
    style: str
    flavor: int
    image: int
    cost: int

    @validator("flavor", "image", "cost")
    def validate_ratings(cls, value, field) -> int:
        if value < 1 or value > 10:
            raise HTTPException(
                detail=f"{field.name} must be between 1 and 10",
                status_code=status.HTTP_400_BAD_REQUEST,
            )
        return value
