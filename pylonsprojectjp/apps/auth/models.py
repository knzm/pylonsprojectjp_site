# -*- coding: utf-8 -*-

import datetime

from sqlalchemy import (
    Table,
    Column,
    ForeignKey,
    Integer,
    Unicode,
    String,
    DateTime,
    )
from sqlalchemy.orm import relationship

from pylonsprojectjp.models import BaseModel


user_group = Table(
    "user_group", BaseModel.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('group_id', Integer, ForeignKey('groups.id')),
    )


class UserModel(BaseModel):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)
    modified = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)

    username = Column(Unicode(255), unique=True)
    _password = Column("password", String(255))
    last_logged = Column(DateTime, default=datetime.datetime.utcnow)

    def set_password(self, password):
        from .security import hash_password
        self._password = hash_password(password, salt=self.salt)

    password = property(fset=set_password)

    def verify_password(self, password):
        from .security import hash_password
        return self._password == hash_password(password, salt=self.salt)

    @property
    def salt(self):
        self.ensure_created()
        return self.created.strftime("%Y-%m-%d %H:%M:%S")

    def ensure_created(self):
        if self.created is None:
            self.created = datetime.datetime.now()


class GroupModel(BaseModel):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)
    modified = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)

    group_name = Column(Unicode(255), unique=True)

    users = relationship('UserModel', backref="groups",
                         secondary=user_group)
