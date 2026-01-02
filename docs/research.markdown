---
layout: page
title: Projects
permalink: /research/
---

<style>
    #filter-bar {
        background-color: #f5f5f5; /* Light gray background */
        padding: 10px;
        text-align: left;
        margin-bottom: 20px; /* Adds space below the filter bar */
    }

    .filter-btn {
        background-color: #ffffff; /* White background for buttons */
        border: 2px solid #d0d0d0; /* Light gray border */
        color: #333; /* Dark gray text */
        padding: 8px 16px;
        margin: 8px 4px; /* Adds spacing around buttons */
        cursor: pointer;
        font-size: 14px;
        display: inline-block;
    }

    .filter-btn:hover {
        background-color: #e0e0e0; /* Slightly darker background on hover */
    }

    .filter-btn:active {
        background-color: #cacaca; /* Even darker for the active state */
    }

    .research-entry {
        border: 1px solid #ccc; /* Light gray border */
        padding: 15px;
        margin-bottom: 20px;
        border-radius: 8px;
        display: flex;
        flex-direction: row; /* Arrange rows horizontally */
    }

    .research-entry img {
        width: 33%;  /* Image takes up 33% of the width */
        height: auto;
        margin-right: 20px;
        border-radius: 8px;
        flex-shrink: 0; /* Prevent image from shrinking */
    }

    .content-container {
        width: 66%; /* Content takes up 66% of the width */
        display: flex;
        flex-direction: column; /* Stack items vertically */
    }

    .content-container .title {
        display: flex;
        align-items: center; /* Center align title vertically */
        margin-bottom: 10px;
    }

    .content h3 {
        margin-top: 0;
    }

    .content p, .content a {
        margin: 10px 0; /* Add margin for better spacing */
    }

    .authors, .year {
        font-size: 12px; /* Smaller font size */
        font-weight: lighter; /* Less bold than the default */
    }

    .year {
        font-weight: lighter; /* Even lighter font weight for the year */
    }
</style>

<!--<div id="filter-bar">
  <button class="filter-btn" onclick="filterResearch('all')">Show all</button>
  {% assign all_topics = "" %}
  {% for research in site.data.research %}
    {% assign topics = research.topics | join: "," | remove: "[" | remove: "]" | remove: '"' %}
    {% assign all_topics = all_topics | append: topics | append: "," %}
  {% endfor %}
  {% assign all_topics = all_topics | split: "," | uniq | sort %}
  {% for topic in all_topics %}
    {% assign topic = topic | strip %}
    {% if topic != "" %}
      <button class="filter-btn" onclick="filterResearch('{{ topic | escape }}')">{{ topic }}</button>
    {% endif %}
  {% endfor %}
</div>-->

<div class="research-container">
  {% for research in site.data.research %}
    <div class="research-entry" data-topics="{{ research.topics | join: ', ' }}">
        <img src="{{ research.image }}" alt="Image for {{ research.title }}">
        <div class="content-container">
            <div class="title">
                <h3>{{ research.title }}</h3>
            </div>
            <div class="content">
                <p class="authors">{{ research.authors }} - <span class="year">{{ research.year }}</span></p>
                <p><strong>Abstract:</strong> {{ research.abstract }}</p>
                <a href="{{ research.link }}">Link</a>
                <p><strong>Topics:</strong> {{ research.topics | join: ", " }}</p>
            </div>
        </div>
    </div>
  {% endfor %}
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
    function filterResearch(topic) {
      document.querySelectorAll('.research-entry').forEach(entry => {
        const topics = entry.dataset.topics.split(', ');
        entry.style.display = (topic === 'all' || topics.includes(topic)) ? 'block' : 'none';
      });
    }
    window.filterResearch = filterResearch;  // Expose to global scope for inline onclick handlers
});
</script>

[Go to all publications](/publications)
