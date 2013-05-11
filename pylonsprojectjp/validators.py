# -*- coding: utf-8 -*-

from formencode.validators import *

class UnicodeString(UnicodeString):
    """The FormEncode UnicodeString validator encodes strings as utf-8 for display. However, this is not desired behaviour in tw.forms, as Genshi will fail when it receives such strings. Instead, this validator renders Python unicode objects where possible, strings otherwise."""
    def _from_python(self, value, state):
        if isinstance(value, basestring):
            return value
        elif hasattr(value, '__unicode__'):
            return unicode(value)
        else:
            return str(value)
