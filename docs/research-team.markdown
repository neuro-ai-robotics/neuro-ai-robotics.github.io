---
layout: page
title: Research Team
permalink: /research-team/
---

Here is the list of our talented researchers:

## Principal Researchers:
{% for researcher in site.data.research_team.principal_researchers %}
###  {{ researcher.name }}
<div style="display: flex;">
  <img src="{{ researcher.image }}" alt="{{ researcher.name }}" style="width:300px;height:300px;border-radius:15px;">
  <p style="margin-left: 20px;"> {{ researcher.description }}</p>
</div>
<div style="display: flex; margin-bottom: 20px;">
  {% for link in researcher.links %}
  <a href="{{ link.url }}" style="margin-right: 5px;"><img src="{{ link.icon }}" alt="Link" style="width:20px;height:20px;display:inline-block;"></a>
  {% endfor %}
</div>
{% endfor %}

## PhD Students:
{% for student in site.data.research_team.phd_students %}
###  {{ student.name }}
<div style="display: flex;">
  <img src="{{ student.image }}" alt="{{ student.name }}" style="width:300px;height:300px;border-radius:15px;">
  <p style="margin-left: 20px;"> {{ student.description }}</p>
</div>
<div style="display: flex; margin-bottom: 20px;">
  {% for link in student.links %}
  <a href="{{ link.url }}" style="margin-right: 5px;"><img src="{{ link.icon }}" alt="Link" style="width:20px;height:20px;display:inline-block;"></a>
  {% endfor %}
</div>
{% endfor %}

Feel free to reach out to any of them for more information about our research projects.
