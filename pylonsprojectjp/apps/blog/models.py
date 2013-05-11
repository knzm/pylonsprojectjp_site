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

from webhelpers.text import urlify
from webhelpers.date import time_ago_in_words

from pylonsprojectjp.models import BaseModel


class BlogEntryModel(BaseModel):
    __tablename__ = 'entries'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, default=datetime.datetime.utcnow)
    modified = Column(DateTime, default=datetime.datetime.utcnow)

    title = Column(Unicode(255), unique=True, nullable=False)
    body = Column(UnicodeText, default=u'')

    @property
    def slug(self):
        return urlify(self.title)

    @property
    def created_in_words(self):
        return time_ago_in_words(self.created)
