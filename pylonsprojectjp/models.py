# -*- coding: utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.properties import ColumnProperty
from sqlalchemy import engine_from_config, create_engine

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

    # @classmethod
    # def all(cls):
    #     return cls.query().order_by(sa.desc(cls.created))

    @classmethod
    def get_or_create(cls, **args):
        instance = cls.query().filter_by(**args).first()
        if instance is None:
            instance = cls(**args)
            DBSession.add(instance)
        return instance

    @classmethod
    def get_by_id(cls, id):
        return cls.query().filter(cls.id == id).first()

    def from_dict(self, data):
        for key, value in data.iteritems():
            setattr(self, key, value)

    def to_dict(self, deep={}, exclude=[]):
        col_prop_names = [p.key for p in self.__mapper__.iterate_properties
                          if isinstance(p, ColumnProperty)]
        data = dict([(name, getattr(self, name)) for name in col_prop_names
                     if name not in exclude])
        for rname, rdeep in deep.iteritems():
            dbdata = getattr(self, rname)
            #FIXME: use attribute names (ie coltoprop) instead of column names
            fks = self.__mapper__.get_property(rname).remote_side
            exclude = [c.name for c in fks]
            if dbdata is None:
                data[rname] = None
            elif isinstance(dbdata, list):
                data[rname] = [o.to_dict(rdeep, exclude) for o in dbdata]
            else:
                data[rname] = dbdata.to_dict(rdeep, exclude)
        return data


DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
BaseModel = declarative_base(cls=BaseModelMixin)


def setup_db(dburi):
    engine = create_engine(dburi)
    DBSession.configure(bind=engine)
    BaseModel.metadata.create_all(engine)


def teardown_db():
    DBSession.remove()


def includeme(config):
    settings = config.registry.settings
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
