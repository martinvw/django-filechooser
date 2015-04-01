=============================
Welcome to django-filechooser
=============================

.. image:: https://travis-ci.org/martinvw/django-filechooser.png?branch=master
    :target: https://travis-ci.org/martinvw/django-filechooser

.. image:: https://coveralls.io/repos/martinvw/django-filechooser/badge.png?branch=master
  :target: https://coveralls.io/r/martinvw/django-filechooser?branch=master

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

   .. code:: django

     {# Load the tag library #}
     {% load filechooser %}

     {# Load CSS #}
     {% filechooser_css %}

     {# Display a filetabel #}
     {% filechooser_filetable  id="identifier" %}

     {# Load CSS and JavaScript #}
     {% filechooser_javascript id="identifier" %}

     {# Read the documentation for more information #}

Documentation
-------------

The full documentation is at http://django-filechooser.readthedocs.org/.


Requirements
------------

- Python 3.2, 3.3 or 3.4
- Django >= 1.6

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
