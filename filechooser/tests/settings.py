import json

from django.test import TestCase


from filechooser.settings import (
    datatable_css_url, filechooser_css_url, jquery_js_url, datatable_js_url, filechooser_js_url
)

from django.http import HttpResponse, HttpResponseNotFound

class SettingsTestCase(TestCase):

    def test_overwritten_value(self):
        self.assertEquals(jquery_js_url(), 'some-cdn-url')
        self.assertEquals(datatable_css_url(), 'some-other-cdn-url')

    def test_non_overwritten_value(self):
        self.assertEquals(filechooser_css_url(), '/static/filechooser/css/filechooser.css')
        self.assertEquals(datatable_js_url(), '/static/js/jquery.dataTables.min.js')
        self.assertEquals(filechooser_js_url(), '/static/filechooser/js/filechooser.js')
