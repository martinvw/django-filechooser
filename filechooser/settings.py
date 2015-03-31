# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage as static


# Default settings
FILECHOOSER_DEFAULTS = {
    'jquery_js_url': static.url('js/jquery.min.js'),
    'datatable_js_url': static.url('js/jquery.dataTables.min.js'),
    'filechooser_js_url': static.url('filechooser/js/filechooser.js'),
    'datatable_css_url': static.url('css/jquery.dataTables.min.css'),
    'filechooser_css_url': static.url('filechooser/css/filechooser.css'),
}


# Start with a copy of default settings
FILECHOOSER = FILECHOOSER_DEFAULTS.copy()

# Override with user settings from settings.py
FILECHOOSER.update(getattr(settings, 'FILECHOOSER', {}))


def get_filechooser_setting(setting, default=None):
    """
    Read a setting
    """
    return FILECHOOSER.get(setting, default)


def jquery_js_url():
    """
    Return the url to jQuery file to use
    """
    return get_filechooser_setting('jquery_js_url')


def datatable_js_url():
    """
    Return the url to dataTable jQuery file to use
    """
    return get_filechooser_setting('datatable_js_url')


def filechooser_js_url():
    """
    Return the url to filechooser js file to use
    """
    return get_filechooser_setting('filechooser_js_url')

def datatable_css_url():
    """
    Return the url to dataTable css file to use
    """
    return get_filechooser_setting('datatable_css_url')


def filechooser_css_url():
    """
    Return the url to filechooser css file to use
    """
    return get_filechooser_setting('filechooser_css_url')
