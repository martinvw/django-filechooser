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
