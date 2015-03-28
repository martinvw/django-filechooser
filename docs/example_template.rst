.. code:: django

  {# Load the tag library #}
  {% load filechooser %}

  {# Load CSS #}
  {% filechooser_css %}

  {# Display a filetabel #}
  {% filechooser_list  %}

  {# Load CSS and JavaScript #}
  {% filechooser_javascript "identifier" "ajax_browse_url" "next_page_url"%}

  {# Read the documentation for more information #}

