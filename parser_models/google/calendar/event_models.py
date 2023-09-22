import datetime
from pydantic import BaseModel, Field
from typing import List, Optional


class DateTimeInfo(BaseModel):
    """give either dateTime or date"""
    dateTime: str = Field(description="Date and time in RFC3339 format")
    timeZone: str = Field(description="Timezone in IANA Time Zone Database format")
    # date: str | None = Field(description="Date in RFC3339 format, its only for all day events")


class Event(BaseModel):
    start: DateTimeInfo = Field(description="Start date and time information")
    end: DateTimeInfo = Field(description="End date and time information, for single event don't consider recurring events")
    summary: str = Field(description="Optional, Event summary or title")
    attendees: List = Field(
        description="Optional, Event attendees", default=[])
    location: Optional[str] = Field(
        description="Optional, Event location", default="")
    recurrence: Optional[List[str]] = Field(
        description="Optional, Recurrence rules for the event. it's in RFC5545 format", default=[])
