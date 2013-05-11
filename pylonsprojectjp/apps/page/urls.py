# -*- coding: utf-8 -*-

from .utils import page_predicate


def includeme(config):
    config.add_route("page", "/*subpath", custom_predicates=[page_predicate])
