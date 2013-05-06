# -*- coding: utf-8 -*-

import venusian
from zope.interface import implementer
from pyramid.exceptions import ConfigurationError

from .interfaces import IAdminFormInfo

__all__ = [
    'admin_form_config',
    'ListColumn',
]


@implementer(IAdminFormInfo)
class AdminFormInfo(object):
    def __init__(self, form_class, model_class, title, list_columns):
        self.form_class = form_class
        self.model_class = model_class
        self.title = title
        self.list_columns = list_columns


class admin_form_config(object):
    def __init__(self, **settings):
        self.__dict__.update(settings)

    def __call__(self, wrapped):
        settings = self.__dict__.copy()

        def callback(context, name, ob):
            config = context.config.with_package(info.module)
            config.add_admin_form(form_class=ob, **settings)

        info = venusian.attach(wrapped, callback, category='pylonsprojectjp')

        return wrapped


def add_admin_form(config, name=None, form_class=None, model_class=None,
                   title=None, list_columns=None):
    if not form_class:
        raise ConfigurationError('"form_class" was not specified.')
    if not model_class:
        raise ConfigurationError('"model_class" was not specified.')
    form_class = config.maybe_dotted(form_class)
    model_class = config.maybe_dotted(model_class)

    if name is None:
        name = model_class.__name__
        if name.endswith('Model'):
            name = name[:-5]
        name = name.lower()

    if title is None:
        title = name

    if not list_columns:
        raise ConfigurationError('"list_columns" was not specified.')

    info = AdminFormInfo(form_class=form_class, model_class=model_class,
                         title=title, list_columns=list_columns)
    config.registry.registerUtility(info, IAdminFormInfo, name)


class ListColumn(object):
    def __init__(self, name, label=None, field=None):
        self.name = name
        self.label = label or name
        self.field = field
