import datetime
from uuid import UUID

import uuid
from click import DateTime
from pydantic import BaseModel
from pydantic_extra_types.epoch import Integer
from rich.table import Column


class TimeStampMixinModel(BaseModel):
    """
    Bu model abstrak model bo'lib, hammasiga shu fieldlarni yozib o'tmaslik uchun yaratilgan
    """
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class ModelPrimaryKeyModel(BaseModel):
    """
    Bu modelni vazifasi hamma modellarga id va uuid yaratib beradi, loyihada 2 lasi ham ishlatiladi
    id foreign key uchun uuid tashqi tomondan murojaat qilish uchun
    """
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)
