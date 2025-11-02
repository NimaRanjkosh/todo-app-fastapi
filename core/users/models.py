import hashlib
from passlib.context import CryptContext
from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from sqlalchemy.orm import relationship
from core.database import Base

pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_date = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_date = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        server_onupdate=func.now(),
        onupdate=func.now(),
    )

    tasks = relationship("TaskModel", back_populates="user")

    def hash_password(self, raw_password: str) -> str:
        if len(raw_password.encode("utf-8")) > 72:
            raw_password = hashlib.sha256(raw_password.encode()).hexdigest()
        return pwd_context.hash(raw_password)

    def verify_password(self, raw_password: str) -> bool:
        if len(raw_password.encode("utf-8")) > 72:
            raw_password = hashlib.sha256(raw_password.encode()).hexdigest()
        return pwd_context.verify(raw_password, self.password)

    def set_password(self, raw_password: str) -> None:
        self.password = self.hash_password(raw_password)
