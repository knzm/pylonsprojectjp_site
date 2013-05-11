# -*- coding: utf-8 -*-

from .utils import admin_config, ListColumn

__all__ = ['admin_config', 'ListColumn']


def includeme(config):
    config.add_directive('add_admin', '.utils.add_admin')
