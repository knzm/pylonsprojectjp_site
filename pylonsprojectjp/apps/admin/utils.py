# -*- coding: utf-8 -*-

import venusian
from zope.interface import classImplements
from pyramid.interfaces import IRequest

from .interfaces import IAdmin

__all__ = [
    'admin_config',
    'ListColumn',
]


class admin_config(object):
    def __init__(self, **settings):
        self.__dict__.update(settings)

    def __call__(self, wrapped):
        settings = self.__dict__.copy()

        def callback(context, name, ob):
            classImplements(ob, IAdmin)
            config = context.config.with_package(info.module)
            config.add_admin(admin=ob, **settings)

        info = venusian.attach(wrapped, callback, category='pylonsprojectjp')

        return wrapped


def add_admin(config, admin, name):
    config.registry.registerAdapter(admin, (IRequest,), IAdmin, name)


class ListColumn(object):
    def __init__(self, name, label=None, field=None):
        self.name = name
        self.label = label or name
        self.field = field
