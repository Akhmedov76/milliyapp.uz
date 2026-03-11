from datetime import datetime
import uuid
from pydantic import BaseModel
from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.dialects.postgresql import UUID


class TimeStampMixinModel(BaseModel):
    """
    Bu model abstrak model bo'lib, hammasiga shu fieldlarni yozib o'tmaslik uchun yaratilgan
    """
    created_at = Column(DateTime(), default=datetime.now())
    updated_at = Column(DateTime(), default=datetime.now(), onupdate=datetime.utcnow)


class PrimaryKeyModel(BaseModel):
    """
    Bu modelni vazifasi hamma modellarga id va uuid yaratib beradi, loyihada 2 lasi ham ishlatiladi
    id foreign key uchun uuid tashqi tomondan murojaat qilish uchun
    """
    __abstract__ = True

    id = Column(Integer(), primary_key=True, index=True)
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)
