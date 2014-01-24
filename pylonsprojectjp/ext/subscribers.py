# -*- coding: utf-8 -*-

from pyramid.events import subscriber, ContextFound

from js.modernizr import modernizr
from js.bootstrap import bootstrap


@subscriber(ContextFound)
def load_fanstatic(event):
    modernizr.need()
    bootstrap.need()
