.. code:: django

  {# Load the tag library #}
  {% load filechooser %}

  {# Load CSS #}
  {% filechooser_css %}

  {# Display a filetabel #}
  {% filechooser_filetable  %}

  {# Load CSS and JavaScript #}
  {% filechooser_javascript id="identifier" browse_url="ajax_browse_url" next_url="next_page_url"%}

  {# Read the documentation for more information #}

