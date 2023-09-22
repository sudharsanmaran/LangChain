
from pydantic import BaseModel, Field
from typing import List, Optional


class Event(BaseModel):
    start: dict = Field(description="Start date and time information")
    end: dict = Field(description="End date and time information")
    summary: str = Field(description="Event summary or title")
    attendees: List = Field(description="Event attendees", default=[])
    location: Optional[str] = Field(description="Event location", default="")
