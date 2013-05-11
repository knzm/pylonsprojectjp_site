# -*- coding: utf-8 -*-

from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models import DBSession


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)

    secret = settings.get('pylonsprojectjp.auth.secret', 'somesecret')
    authentication_policy = AuthTktAuthenticationPolicy(secret)
    authorization_policy = ACLAuthorizationPolicy()

    config = Configurator(settings=settings,
                          authentication_policy=authentication_policy,
                          authorization_policy=authorization_policy)

    # define layouts
    config.add_layout('.layout.BasicLayout', template='layout.jinja2')
    config.add_layout('.layout.AdminLayout', name='admin',
                      template='pylonsprojectjp:templates/admin/base.mako')
    config.add_layout('.layout.AdminLayout', name='auth',
                      template='pylonsprojectjp:templates/auth/base.mako')

    # enable per-app extensions
    config.include('.apps.admin')

    # setup project extensions
    config.include('.urls')
    config.include('.subscribers')

    # load models, look up views, etc...
    config.scan('.apps.page')
    config.scan('.apps.top')
    config.scan('.apps.admin')
    config.scan('.apps.auth')
    config.scan('.apps.blog')

    # don't quote ";" in generated urls
    from .custom import monkeypatch_quote_path_segment
    monkeypatch_quote_path_segment()

    return config.make_wsgi_app()
