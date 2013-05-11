# -*- coding: utf-8 -*-

import unittest
import transaction

from pyramid import testing

from pylonsprojectjp.models import DBSession, setup_db, teardown_db
from .models import BlogEntryModel


class TestBlogIndexView(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        setup_db('sqlite://')

        with transaction.manager:
            model = BlogEntryModel(title=u"blog title", body=u"blog content")
            DBSession.add(model)

    def tearDown(self):
        teardown_db()
        testing.tearDown()

    def test_it(self):
        from .views import blog_index_view

        request = testing.DummyRequest()
        info = blog_index_view(request)
        self.assertEqual(info['paginator'].item_count, 1)
        self.assertEqual(info['paginator'].items[0].title, u"blog title")
        self.assertEqual(info['paginator'].items[0].body, u"blog content")
