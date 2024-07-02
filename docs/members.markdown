---
layout: page
title: Members
permalink: /members/
---

<style>
  .researcher-container {
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      margin: 20px;
  }

  .columns-container {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
  }

  .column {
      flex: 1 1 calc(33.333% - 40px);
      box-sizing: border-box;
      margin: 20px;
      display: flex;
      flex-direction: column;
      align-items: center;
      min-width: 250px;
  }

  .researcher-container img {
      width: 100%;
      max-width: 300px;
      height: 300px;
      object-fit: cover;
      border-radius: 15px;
      margin-bottom: 10px;
  }

  .researcher-links {
      display: flex;
      justify-content: center;
      margin-top: 10px;
  }

  .researcher-links a {
      margin-right: 5px;
  }

  @media (max-width: 768px) {
    .column {
        flex: 1 1 calc(50% - 40px);
    }
  }

  @media (max-width: 480px) {
    .column {
        flex: 1 1 100%;
    }
  }
</style>

Here is the list of our talented researchers:

## Principal Investigators:
<div class="columns-container">
{% for researcher in site.data.research_team.principal_researchers %}
<div class="column">
  <div class="researcher-container">
    <img src="{{ researcher.image }}" alt="{{ researcher.name }}">
    <p><b>{{ researcher.name }}</b>. {{ researcher.description }} [{{ researcher.institution }}]</p>
  </div>
  <div class="researcher-links">
  {% for link in researcher.links %}
    {% if link.url and link.url != "" %}
      <a href="{{ link.url }}">
        <img src="{{ link.icon }}" alt="Link" style="width:20px;height:20px;display:inline-block;">
      </a>
    {% endif %}
  {% endfor %}
  </div>
</div>
{% endfor %}
</div>

## Postdocs, PhD students and researchers:
<div class="columns-container">
{% for student in site.data.research_team.postdocs %}
<div class="column">
  <div class="researcher-container">
    <img src="{{ student.image }}" alt="{{ student.name }}">
    <p><b>{{ student.name }}</b>. {{ student.description }} [{{ student.institution }}]</p>
  </div>
  <div class="researcher-links">
    {% for link in student.links %}
      {% if link.url and link.url != "" %}
        <a href="{{ link.url }}">
          <img src="{{ link.icon }}" alt="Link" style="width:20px;height:20px;display:inline-block;">
        </a>
      {% endif %}
    {% endfor %}
  </div>
</div>
{% endfor %}

{% for student in site.data.research_team.phd_students %}
<div class="column">
  <div class="researcher-container">
    <img src="{{ student.image }}" alt="{{ student.name }}">
    <p><b>{{ student.name }}</b>. {{ student.description }} [{{ student.institution }}]</p>
  </div>
  <div class="researcher-links">
    {% for link in student.links %}
      {% if link.url and link.url != "" %}
        <a href="{{ link.url }}">
          <img src="{{ link.icon }}" alt="Link" style="width:20px;height:20px;display:inline-block;">
        </a>
      {% endif %}
    {% endfor %}
  </div>
</div>
{% endfor %}
</div>

## Master students:
<div class="columns-container">
{% for student in site.data.research_team.master %}
<div class="column">
  <div class="researcher-container">
    <img src="{{ student.image }}" alt="{{ student.name }}">
    <p><b>{{ student.name }}</b>. {{ student.description }} [{{ student.institution }}]</p>
  </div>
  <div class="researcher-links">
    {% for link in student.links %}
      {% if link.url and link.url != "" %}
        <a href="{{ link.url }}">
          <img src="{{ link.icon }}" alt="Link" style="width:20px;height:20px;display:inline-block;">
        </a>
      {% endif %}
    {% endfor %}
  </div>
</div>
{% endfor %}
</div>



## Former researchers:
<div class="columns-container">
{% for student in site.data.research_team.former %}
<div class="column">
  <div class="researcher-container">
    <img src="{{ student.image }}" alt="{{ student.name }}">
    <p><b>{{ student.name }}</b>. {{ student.description }} [{{ student.institution }}]</p>
  </div>
  <div class="researcher-links">
    {% for link in student.links %}
      {% if link.url and link.url != "" %}
        <a href="{{ link.url }}">
          <img src="{{ link.icon }}" alt="Link" style="width:20px;height:20px;display:inline-block;">
        </a>
      {% endif %}
    {% endfor %}
  </div>
</div>
{% endfor %}
</div>

Feel free to reach out to any of them for more information about our research projects.
