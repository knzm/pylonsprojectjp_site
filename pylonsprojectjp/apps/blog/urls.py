# -*- coding: utf-8 -*-

def includeme(config):
    config.add_route('blog_index', '/')
    config.add_route('blog_entry', '/blog/{id:\d+}/{slug}')
