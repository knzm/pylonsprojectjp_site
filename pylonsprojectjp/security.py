# -*- coding: utf-8 -*-

from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy


def includeme(config):
    settings = config.registry.settings
    secret = settings.get('pylonsprojectjp.auth.secret', 'somesecret')
    authentication_policy = AuthTktAuthenticationPolicy(secret)
    authorization_policy = ACLAuthorizationPolicy()
    config.set_authentication_policy(authentication_policy)
    config.set_authorization_policy(authorization_policy)
