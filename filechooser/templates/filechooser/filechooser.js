{% load static %}
{% for script in scripts %}
<script src="{% static script %}"></script>
{% endfor %}
<script type="text/javascript">
var nexturl = "/mapper/filechooser/{{filechooser_id}}/http/process/";
var baseurl = "/mapper/filechooser/{{filechooser_id}}/ajax/list/";
var filechooser_id = "#{{filechooser_id}}"
var table;
</script>
<script src="{% static 'filechooser/js/filechooser.js' %}"></script>
