from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    func,
)
from sqlalchemy.orm import relationship
from core.database import Base


class TaskStatusModel(Base):
    __tablename__ = "taskstatus"

    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String(20), nullable=False)

    created_date = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_date = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    tasks = relationship("TaskModel", back_populates="status")
