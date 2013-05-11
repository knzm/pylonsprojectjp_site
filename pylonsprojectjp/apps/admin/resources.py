# -*- coding: utf-8 -*-

from pyramid.security import Allow, Authenticated, ALL_PERMISSIONS


class AdminRootContext(object):
    __acl__ = [
        (Allow, Authenticated, 'view'),
        (Allow, 'admin', ALL_PERMISSIONS),
        # (Allow, 'editor', ('view', 'new', 'edit', 'delete')),
        ]

    def __init__(self, request):
        self.request = request
