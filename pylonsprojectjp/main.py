# -*- coding: utf-8 -*-

from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)

    # initialize db
    config.include('.models')

    # define authn/authz policy
    config.include('.security')

    # define layouts
    config.include('.layout')
    config.scan('.layout')

    # enable per-app extensions
    config.include('.apps.admin')

    # setup project extensions
    config.include('.urls')
    config.include('.ext')

    # load models, look up views, etc...
    config.scan('.apps.page')
    config.scan('.apps.top')
    config.scan('.apps.admin')
    config.scan('.apps.auth')
    config.scan('.apps.blog')

    return config.make_wsgi_app()
