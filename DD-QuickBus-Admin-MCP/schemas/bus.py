from pydantic import BaseModel, Field, field_validator
from typing import List, Literal, Optional


class AddBusInput(BaseModel):
    name: str = Field(min_length=1)

    busnumber: str = Field(min_length=1)

    totalseats: int = Field(ge=1)

    bus_type: Literal["seating", "sleeper"]

    baseprice: float = Field(ge=0)

    amenties: List[Literal["WiFi", "AC", "Charging"]]

    token: str = Field(min_length=10)

    # normalize case (optional but useful)
    @field_validator("amenties", mode="before")
    @classmethod
    def normalize_amenities(cls, v):
        if isinstance(v, list):
            return [item.strip() for item in v]
        raise ValueError("amenties must be a list")
    
class UpdateBusInput(BaseModel):
    id: str = Field(min_length=1)

    name: str = Field()
    baseprice: float = Field(ge=0)
    type: Literal["seating", "sleeper"]
    amenties: List[Literal["WiFi", "AC", "Charging"]]

    token: str = Field(min_length=10)

    @field_validator("amenties", mode="before")
    @classmethod
    def normalize_amenities(cls, v):
        if v is None:
            return v
        if isinstance(v, list):
            return [item.strip() for item in v]
        raise ValueError("amenties must be a list")