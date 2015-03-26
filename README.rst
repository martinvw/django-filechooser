=============================
Welcome to django-filechooser
=============================

Supply a server-side file-chooser in your Django application.


Installation
------------

1. Install using pip:

   ``pip install django-filechooser``

   Alternatively, you can install download or clone this repo and call ``pip install -e .``.

2. Add to INSTALLED_APPS in your ``settings.py``:

   ``'filechooser',``

3. In your templates, load the ``filechooser`` library and use the ``filechooser_*`` tags:

Example template
----------------

   .. code:: Django

    {% load filechooser %}
    {% filechooser_css %}

    {# Display a file-list #}

    {% filechooser_js %}

Documentation
-------------

The full documentation is at http://django-filechooser.readthedocs.org/.


Requirements
------------

- Python 3.2 or 3.3
- Django >= 1.7

Contributions and pull requests for other Django and Python versions are welcome.

Bugs and requests
-----------------

If you have found a bug or if you have a request for additional functionality, please use the issue tracker on GitHub.

https://github.com/martinvw/django-filechooser/issues

License
-------

You can use this under MIT license. See `LICENSE
<LICENSE>`_ file for details.

Author
------

Developed and maintained by Martin van Wingerden