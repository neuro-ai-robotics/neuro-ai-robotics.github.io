---
layout: page
title: Research Team
permalink: /research-team/
---

<style>
  .researcher-container {
      display: flex;
      flex-wrap: wrap;
      margin-bottom: 20px;
      justify-content: center; /* Centra el contenido horizontalmente */
      align-items: center; /* Centra el contenido verticalmente */
  }

  .researcher-container img {
      width: 100%;
      max-width: 300px;
      height: auto;
      border-radius: 15px;
  }

  .researcher-container p {
      flex-grow: 1;
      margin-left: 20px;
      text-align: center; /* Centra el texto */
  }

  .researcher-links {
      display: flex;
      margin-bottom: 20px;
      justify-content: center; /* Centra los enlaces horizontalmente */
  }

  .researcher-links a {
      margin-right: 5px;
  }
</style>

Here is the list of our talented researchers:

## Principal Investigators:
{% for researcher in site.data.research_team.principal_researchers %}
<div class="researcher-container">
  <img src="{{ researcher.image }}" alt="{{ researcher.name }}">
  <p> <b>{{ researcher.name }}</b>. {{ researcher.description }}</p>
</div>
<div class="researcher-links">
  {% for link in researcher.links %}
  <a href="{{ link.url }}"><img src="{{ link.icon }}" alt="Link" style="width:20px;height:20px;display:inline-block;"></a>
  {% endfor %}
</div>
{% endfor %}

## Postdocs, PhD students and researchers:
{% for student in site.data.research_team.postdocs %}
###  {{ student.name }}
<div class="researcher-container">
  <img src="{{ student.image }}" alt="{{ student.name }}">
  <p> {{ student.description }}</p>
</div>
<div class="researcher-links">
  {% for link in student.links %}
  <a href="{{ link.url }}"><img src="{{ link.icon }}" alt="Link" style="width:20px;height:20px;display:inline-block;"></a>
  {% endfor %}
</div>
{% endfor %}
{% for student in site.data.research_team.phd_students %}
###  {{ student.name }}
<div class="researcher-container">
  <img src="{{ student.image }}" alt="{{ student.name }}">
  <p> {{ student.description }}</p>
</div>
<div class="researcher-links">
  {% for link in student.links %}
  <a href="{{ link.url }}"><img src="{{ link.icon }}" alt="Link" style="width:20px;height:20px;display:inline-block;"></a>
  {% endfor %}
</div>
{% endfor %}

## Former researchers
{% for student in site.data.research_team.former %}
###  {{ student.name }}
<div class="researcher-container">
  <img src="{{ student.image }}" alt="{{ student.name }}">
  <p> {{ student.description }}</p>
</div>
<div class="researcher-links">
  {% for link in student.links %}
  <a href="{{ link.url }}"><img src="{{ link.icon }}" alt="Link" style="width:20px;height:20px;display:inline-block;"></a>
  {% endfor %}
</div>
{% endfor %}

Feel free to reach out to any of them for more information about our research projects.
