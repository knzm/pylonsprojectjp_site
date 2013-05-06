# -*- coding: utf-8 -*-

from zope.interface import Interface, Attribute

__all__ = [
    'IAdminFormInfo',
]


class IAdminFormInfo(Interface):
    form_class = Attribute("form_class")
    model_class = Attribute("model_class")
    title = Attribute("title")
    list_columns = Attribute("columns")
