from sqlalchemy import (
    Column, Integer, String, Boolean, ForeignKey, Text, DateTime, func
)
from sqlalchemy.orm import relationship
from core.database import Base

class TaskModel(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    description = Column(Text())
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    status_id = Column(Integer, ForeignKey("taskstatus.id"), nullable=False)
    is_completed = Column(Boolean, default=False)
    created_date = Column(DateTime, server_default=func.now(), nullable=False)
    updated_date = Column(DateTime, server_default=func.now(), server_onupdate=func.now(), onupdate=func.now())

    status = relationship("TaskStatusModel", back_populates="tasks")
    user = relationship("UserModel", back_populates="tasks", uselist=False)
