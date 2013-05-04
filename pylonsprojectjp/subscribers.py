# -*- coding: utf-8 -*-

from pyramid.events import BeforeRender

from js.modernizr import modernizr


def load_fanstatic(event):
    modernizr.need()


def includeme(config):
    config.add_subscriber(load_fanstatic, BeforeRender)
