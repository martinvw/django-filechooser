{% load static %}
{% for script in scripts %}
<script src="{% static script %}"></script>
{% endfor %}
<script type="text/javascript">
var nexturl = "{% url filechooser_url_id "http" "process" ""%}";
var baseurl = "{% url filechooser_url_id "ajax" "list" ""%}";
var filechooser_id = "#{{filechooser_id}}"
var table;
</script>
<script src="{% static js_url %}"></script>
