from sqlalchemy import Column, String

from core.models import PrimaryKeyModel, TimeStampMixinModel


class UserModel(PrimaryKeyModel, TimeStampMixinModel):
    __tablename__ = 'users'

    first_name = Column(String(100))
    last_name = Column()
