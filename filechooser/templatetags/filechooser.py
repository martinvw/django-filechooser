# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template
from django.template.loader import get_template

register = template.Library()

@register.simple_tag
def filechooser_css():
    """
    Return HTML for the (inclusion of) the filechooser CSS.
    **Tag name**::
        filechooser_css
    **usage**::
        {% filechooser_css %}
    **example**::
        {% filechooser_css %}
    """
    urls = [url for url in [filechooser_css_url()] if url]
    return ''.join([render_link_tag(url) for url in urls])


@register.simple_tag
def filechooser_javascript():
    """
    Return HTML for filechooser JavaScript, which also means the js
	for the datatable and optionally the jquery.
    Adjust url in settings. If no url is returned, we don't want this
    statement to return any HTML.
    This is intended behavior.
    Default value: ``None``
    This value is configurable, see Settings section
    **Tag name**::
        filechooser_javascript
    **Parameters**:
        :jquery: True to include jQuery as well as the Datatable js
    **usage**::
        {% filechooser_javascript %}
    **example**::
        {% filechooser_javascript jquery=1 %}
    """

    javascript = ''
    # See if we have to include jQuery
    if jquery is None:
        jquery = get_filechooser_setting('include_jquery', False)
    # NOTE: No async on scripts, not mature enough. See issue #52 and #56
    if jquery:
        url = bootstrap_jquery_url()
        if url:
            javascript += '<script src="{url}"></script>'.format(url=url)
    url = bootstrap_javascript_url()
    if url:
        javascript += '<script src="{url}"></script>'.format(url=url)
    return javascript
