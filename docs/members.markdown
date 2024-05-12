---
layout: page
title: Members
permalink: /members/
---

<style>
  .researcher-container {
      display: flex;
      flex-wrap: wrap;
      margin-bottom: 20px;
      justify-content: center;
      align-items: center;
  }

  .columns-container {
      display: flex; /* This ensures the child elements are laid out in a row */
      justify-content: space-between; /* This spreads the columns to occupy the left and right sides */
  }

  .column {
      flex: 1; /* This allows each column to grow and fill up the container equally */
      max-width: 50%; /* Maximum width to ensure they stay side by side */
      padding: 10px; /* Padding around each column */
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
      text-align: center;
  }

  .researcher-links {
      display: flex;
      margin-bottom: 20px;
      justify-content: center;
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
  {% if link.url and link.url != "" %}
    <a href="{{ link.url }}">
      <img src="{{ link.icon }}" alt="Link" style="width:20px;height:20px;display:inline-block;">
    </a>
  {% endif %}
{% endfor %}
</div>
{% endfor %}

## Postdocs, PhD students and researchers:
<div class="columns-container">
  <!-- Column for CSIC -->
  <div class="column">
    <img src="/icons/csic.png" alt="Donders Institute Logo" style="display: block; margin: 0 auto 20px auto; width: 100px; height: auto;">
    {% assign csic_postdocs = site.data.research_team.postdocs | where: "institution", "csic" %}
    {% if csic_postdocs.size > 0 %}
    <h4 style="text-align: center;"> Postdoctoral students </h4>
    {% for student in site.data.research_team.postdocs %}
    {% if student.institution == 'csic' %}
    <div class="researcher-container">
      <img src="{{ student.image }}" alt="{{ student.name }}">
      <p><b>{{ student.name }}</b>. {{ student.description }}</p>
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
    {% endif %}
    {% endfor %}
    {% endif %}
    {% assign csic_phd_students = site.data.research_team.phd_students | where: "institution", "csic" %}
    {% if csic_phd_students.size > 0 %}
    <h4 style="text-align: center;"> PhD students </h4>
    {% for student in site.data.research_team.phd_students %}
    {% if student.institution == 'csic' %}
    <div class="researcher-container">
      <img src="{{ student.image }}" alt="{{ student.name }}">
      <p><b>{{ student.name }}</b>. {{ student.description }}</p>
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
    {% endif %}
    {% endfor %}
    {% endif %}
  </div>

  <!-- Column for Donders Institute -->
  <div class="column">
    <img src="/icons/donders_logo.png" alt="Donders Institute Logo" style="display: block; margin: 0 auto 20px auto; width: 100px; height: auto;">
    {% assign donders_postdocs = site.data.research_team.postdocs | where: "institution", "donders" %}
    {% if donders_postdocs.size > 0 %}
    <h4 style="text-align: center;"> Postdoctoral students </h4>

    {% for student in site.data.research_team.postdocs %}
    {% if student.institution == 'donders' %}
    <div class="researcher-container">
      <img src="{{ student.image }}" alt="{{ student.name }}">
      <p><b>{{ student.name }}</b>. {{ student.description }}</p>
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
    {% endif %}
    {% endfor %}
    {% endif %}

    {% assign donders_phd_students = site.data.research_team.phd_students | where: "institution", "donders" %}
    {% if donders_phd_students.size > 0 %}

    <h4 style="text-align: center;"> PhD students </h4>

    {% for student in site.data.research_team.phd_students %}
    {% if student.institution == 'donders' %}
    <div class="researcher-container">
      <img src="{{ student.image }}" alt="{{ student.name }}">
      <p><b>{{ student.name }} </b>. {{ student.description }}</p>
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
    {% endif %}
    {% endfor %}
    {% endif %}
  </div>
</div>


## Former researchers

<div class="columns-container">
  <!-- Column for CSIC -->
  <div class="column">
    <img src="/icons/csic.png" alt="Donders Institute Logo" style="display: block; margin: 0 auto 20px auto; width: 100px; height: auto;">

    {% for student in site.data.research_team.former %}
    {% if student.institution == 'csic' %}
    <div class="researcher-container">
      <img src="{{ student.image }}" alt="{{ student.name }}">
      <p><b>{{ student.name }}</b>. {{ student.description }}</p>
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
    {% endif %}
    {% endfor %}
  </div>
  <div class="column">
    <img src="/icons/donders_logo.png" alt="Donders Institute Logo" style="display: block; margin: 0 auto 20px auto; width: 100px; height: auto;">

    {% for student in site.data.research_team.former %}
    {% if student.institution == 'donders' %}
    <div class="researcher-container">
      <img src="{{ student.image }}" alt="{{ student.name }}">
      <p><b>{{ student.name }}</b>. {{ student.description }}</p>
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
    {% endif %}
    {% endfor %}
  </div>
</div>

Feel free to reach out to any of them for more information about our research projects.
