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


class PageModel(BaseModel):
    __tablename__ = 'pages'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, default=datetime.datetime.utcnow)
    modified = Column(DateTime, default=datetime.datetime.utcnow)

    url = Column(Unicode(255), nullable=False)
    title = Column(Unicode(255), unique=True, nullable=False)
    body = Column(UnicodeText, default=u'')
    template = Column(Text, nullable=False)
