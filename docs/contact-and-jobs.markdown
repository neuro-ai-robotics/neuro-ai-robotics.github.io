---
layout: page
title: Contact and Jobs
permalink: /contact-and-jobs/
---

<style>
    .map-container {
        position: relative;
        overflow: hidden;
        width: 100%;
        padding-top: 56.25%; 
    }

    .map-container iframe {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        border: 0;
    }

    form {
        width: 100%;
        max-width: 600px; 
        margin: 0 auto; 
    }

    form input, form textarea {
        width: 100%;
        box-sizing: border-box; 
    }

    .job-posting {
        border: 1px solid #ccc;
        padding: 15px;
        margin-bottom: 20px;
        border-radius: 8px;
    }

    .job-posting h3 {
        margin-top: 0;
    }

    .job-posting a {
        color: #007bff;
        text-decoration: none;
    }

    .job-posting a:hover {
        text-decoration: underline;
    }

    .job-posting .date {
        color: #666;
        font-size: 0.9em;
    }
</style>

## Contact us
Feel free to reach us at the following email (use "VcqRXuweBUyvcMP" code as subject, please): p [dot] lanillos [at] csic [dot] es

## Looking for a host?
- Information for foreing staff: <a href="https://www.csic.es/en/international/landing-at-csic" target="_blank">Landing at CSIC</a>

Contact us if your research idea fits the group and you would like to apply for a predoc or postdoc call, such as: 
* <a href="https://marie-sklodowska-curie-actions.ec.europa.eu/actions/postdoctoral-fellowships" target="_blank">Marie Skłodowska-Curie Actions</a>
* <a href="https://www.aei.gob.es/convocatorias/buscador-convocatorias/ayudas-contratos-ramon-cajal-ryc-2023" target="_blank">Spanish Ramón y Cajal</a>
* <a href="https://gestiona3.madrid.org/quadrivium/convocatorias/home/talento" target="_blank">Atracción de Talento Comunidad de Madrid</a>
* <a href="https://www.fundacionareces.es/fundacionareces/es/programa-de-retonorno-del-talento/edicion-2024/" target="_blank">Retorno del Talento de la Fundación Ramón Areces</a>

We will help you in the process.


## Job Opportunities

{% for job in site.data.job_postings %}
<div class="job-posting">
    <h3>{{ job.title }}</h3>
    <p>{{ job.description }}</p>
    <p class="date">Posted on: {{ job.date }}</p>
    {% if job.link %}
    <p><a href="{{ job.link }}" target="_blank">Learn more and apply</a></p>
    {% endif %}
</div>
{% endfor %}


## Where to find us:

Instituto Cajal CSIC<br>
Avda. Doctor Arce, 37<br>
28002 Madrid<br>
Spain
<div class="map-container">
    <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d97159.1188015647!2d-3.762632967115804!3d40.44821294662484!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0xd4228dc3425106b%3A0xb35f154ebd25a71!2sInstituto%20Cajal%20-%20CSIC!5e0!3m2!1ses!2ses!4v1710016762149!5m2!1ses!2ses" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
</div>



