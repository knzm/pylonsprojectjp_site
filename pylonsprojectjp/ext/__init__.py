# -*- coding: utf-8 -*-

def fix_quote_path_segment(orig_quote_path_segment):
    def quote_path_segment(segment, safe=''):
        if ';' not in safe:
            safe += ';'
        return orig_quote_path_segment(segment, safe)
    return quote_path_segment


def includeme(config):
    config.scan('.subscribers')

    # don't quote ";" in generated urls
    import pyramid.urldispatch
    pyramid.urldispatch.quote_path_segment = \
        fix_quote_path_segment(pyramid.urldispatch.quote_path_segment)
