# -*- coding: utf-8 -*-

from .utils import admin_form_config, ListColumn

def includeme(config):
    config.add_directive('add_admin_form', '.utils.add_admin_form')
