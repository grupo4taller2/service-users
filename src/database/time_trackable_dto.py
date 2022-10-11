from typing import Union

from sqlalchemy import Column, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class TimeTrackableDTO(Base):
    created_at: Union[DateTime, Column] = Column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Union[DateTime, Column] = Column(
        DateTime(timezone=True), onupdate=func.now()
    )
