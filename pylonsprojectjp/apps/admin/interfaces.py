# -*- coding: utf-8 -*-

from zope.interface import Interface, Attribute

__all__ = ['IAdmin']


class IAdmin(Interface):
    title = Attribute("title")
    list_columns = Attribute("columns")
    model_class = Attribute("model_class")

    def get_form(self, entity):
        """Return a form"""
        pass
