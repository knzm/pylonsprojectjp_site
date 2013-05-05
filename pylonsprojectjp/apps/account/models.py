# -*- coding: utf-8 -*-

import datetime

import sqlalchemy as sa
from sqlalchemy import (
    Column,
    Integer,
    Text,
    Unicode,
    UnicodeText,
    DateTime
    )

from pylonsprojectjp.models import BaseModel


class UserModel(BaseModel):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, default=datetime.datetime.utcnow)
    modified = Column(DateTime, default=datetime.datetime.utcnow)

    name = Column(Unicode(255), unique=True, nullable=False)
    password = Column(Unicode(255), nullable=False)
    last_logged = Column(DateTime, default=datetime.datetime.utcnow)
