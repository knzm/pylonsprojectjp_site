# -*- coding: utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base

import sqlalchemy as sa
from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

__all__ = ['DBSession', 'BaseModel', 'setup_db', 'teardown_db']


class BaseModelMixin(object):
    @classmethod
    def query(cls):
        return DBSession.query(cls)

    @classmethod
    def all(cls):
        return cls.query().order_by(sa.desc(cls.created))

    @classmethod
    def by_id(cls, id):
        return cls.query().filter(cls.id == id).first()


DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
BaseModel = declarative_base(cls=BaseModelMixin)


def setup_db(dburi):
    from sqlalchemy import create_engine
    engine = create_engine(dburi)
    DBSession.configure(bind=engine)
    BaseModel.metadata.create_all(engine)


def teardown_db():
    DBSession.remove()
