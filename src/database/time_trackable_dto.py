from typing import Union
from pydantic import BaseModel


from sqlalchemy import Column, DateTime
from sqlalchemy.sql import func


class TimeTrackableDTO(BaseModel):
    created_at: Union[DateTime, Column] = Column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Union[DateTime, Column] = Column(
        DateTime(timezone=True), onupdate=func.now()
    )

    class Config:
        arbitrary_types_allowed = True
