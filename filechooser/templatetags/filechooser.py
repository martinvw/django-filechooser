# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template
from django.template.loader import get_template
from django.forms.widgets import flatatt

try:
    from django.utils.encoding import force_text
except ImportError:
    from django.utils.encoding import force_unicode as force_text

from ..settings import (
    datatable_css_url, filechooser_css_url, jquery_js_url, datatable_js_url, filechooser_js_url, get_filechooser_setting
)

register = template.Library()

@register.simple_tag(takes_context=True)
def filechooser_filetable(context, id):
    """
    Return HTML for the datatabel which is used to display the files
    **Tag name**::
        filechooser_filetable
    **usage**::
        {% filechooser_filetable id="" %}
    **example**::
        {% filechooser_filetable id="filelist" %}
    """

    context['filechooser_id'] = id

    return get_template('filechooser/filetable.html').render(context)

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
    urls = [url for url in [datatable_css_url(), filechooser_css_url()] if url]
    return ''.join([render_css_tag(url) for url in urls])


@register.simple_tag(takes_context=True)
def filechooser_javascript(context, id, jquery = None, namespace = None):
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
        :jquery: True to include jQuery also
    **usage**::
        {% filechooser_javascript id=""%}
    **example**::
        {% filechooser_javascript id="filelist" jquery=1 %}
    """
    # See if we have to include jQuery
    if jquery is None:
        jquery = get_filechooser_setting('include_jquery', False)

    urls = [url for url in [datatable_js_url()] if url]

    if jquery:  urls.prepend(bootstrap_jquery_url())

    url = 'filechooser_' + id
    if namespace: url = namespace + ':' + url

    context['scripts'] = urls
    context['filechooser_id'] = id
    context['filechooser_url_id'] = url
    context['js_url'] = filechooser_js_url()

    return get_template('filechooser/filechooser.js').render(context)


def render_css_tag(url):
    """
    Render the css tag
    """
    return render_tag('link', attrs={'href': url, 'rel': 'stylesheet', 'media': 'all'}, self_close = True)


def render_tag(tag, attrs=None, content=None, self_close=False):
    """
    Render a given tag, based on tag-name, attrs, content and whether it should be closed or not.
    """
    builder = "<{tag}{attrs}{self_close}>{content}"
    if content or not self_close: builder += "</{tag}>"

    return builder.format(
        tag = tag,
        attrs=flatatt(attrs) if attrs else '',
        self_close='/' if self_close else '',
        content=force_text(content) if content else ''
        )
