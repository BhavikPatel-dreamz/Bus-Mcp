from pydantic import BaseModel, Field, field_validator
from typing import List


# ---------- Stop Subdocument ----------
class Stop(BaseModel):
    
    name: str = Field(min_length=1)
    predistance: float = Field(ge=0)
    pretime: float = Field(ge=0)


# ---------- Route Creation Input ----------
class AddRouteInput(BaseModel):
    stops: List[Stop]
    token: str = Field(min_length=10)

    # must have at least 2 stops
    @field_validator("stops")
    @classmethod
    def validate_stops(cls, stops):
        if len(stops) < 2:
            raise ValueError("Route must contain at least 2 stops")

        # logical validation
        total_distance = sum(s.predistance for s in stops)
        if total_distance == 0:
            raise ValueError("Route distance cannot be zero")

        return stops


class EditRouteInput(BaseModel):
    routeId: str = Field(min_length=1)
    stops: List[Stop]
    token: str = Field(min_length=10)

    @field_validator("stops")
    @classmethod
    def validate_stops(cls, stops):
        if len(stops) < 2:
            raise ValueError("Route must contain at least 2 stops")

        total_distance = sum(s.predistance for s in stops)
        if total_distance == 0:
            raise ValueError("Route distance cannot be zero")

        return stops
