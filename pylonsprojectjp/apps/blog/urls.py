# -*- coding: utf-8 -*-

from .security import EntryFactory

def includeme(config):
    config.add_route('blog_index', '/')
    config.add_route('blog_entry', '/blog/{id:\d+}/{slug}')
    config.add_route('blog_action', '/blog/{action}', factory=EntryFactory)
