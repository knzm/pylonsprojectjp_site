# -*- coding: utf-8 -*-

import pyramid.urldispatch


def fix_quote_path_segment(orig_quote_path_segment):
    def quote_path_segment(segment, safe=''):
        if ';' not in safe:
            safe += ';'
        return orig_quote_path_segment(segment, safe)
    return quote_path_segment


def monkeypatch_quote_path_segment():
    pyramid.urldispatch.quote_path_segment = \
        fix_quote_path_segment(pyramid.urldispatch.quote_path_segment)
