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
    config.add_layout('.layout.BasicLayout', 'layout.jinja2')
    config.add_layout('.layout.AdminLayout', 'pylonsprojectjp:templates/admin/base.mako', name='admin')
    config.include('.apps.admin')
    config.include('.apps.blog')
    config.include('.urls')
    config.include('.subscribers')

    config.scan('.apps.top')
    config.scan('.apps.admin')
    config.scan('.apps.account')
    config.scan('.apps.blog')

    return config.make_wsgi_app()
