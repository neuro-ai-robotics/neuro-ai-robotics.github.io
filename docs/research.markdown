---
layout: page
title: Research
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
        margin-right: 8px;
        cursor: pointer;
        font-size: 14px;
    }

    .filter-btn:hover {
        background-color: #e0e0e0; /* Slightly darker background on hover */
    }

    .filter-btn:active {
        background-color: #cacaca; /* Even darker for the active state */
    }

    .research-entry {
        margin-bottom: 20px;
        overflow: auto;  /* Ensures the container wraps around floated images */
        clear: both; /* Clears the float, necessary if the previous element is floated */
    }

    .research-entry img {
        max-width: 150px;  /* Adjust size as necessary */
        height: auto;
        float: left;
        margin-right: 20px;
    }
    .authors, .year {
        font-size: 12px; /* Smaller font size */
        font-weight: lighter; /* Less bold than the default */
    }

    .year {
        font-weight: lighter; /* Even lighter font weight for the year */
    }
</style>

<div id="filter-bar">
  <button class="filter-btn" onclick="filterResearch('all')">Show all</button>
  <button class="filter-btn" onclick="filterResearch('Human Brain Computing')">Human Brain Computing</button>
  <button class="filter-btn" onclick="filterResearch('Brain-inspired Intelligence')">Brain-inspired Intelligence</button>
  <!-- add other buttons for more topics -->
</div>

<div class="research-container">
  {% for research in site.data.research %}
    <div class="research-entry" data-topics="{{ research.topics | join: ', ' }}">
        <img src="{{ research.image }}" alt="Image for {{ research.title }}" style="float: left; margin-right: 20px; width: 150px; height: auto;">
        <h2>{{ research.title }}</h2>
        <p class="authors">{{ research.authors }} - <span class="year">{{ research.year }}</span></p>
        <p><strong>Abstract:</strong> {{ research.abstract }}</p>
        <a href="{{ research.link }}">Read the paper</a>
        <p><strong>Topics:</strong> {{ research.topics | join: ", " }}</p>
    </div>
    <div style="clear: both;"></div>
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

<!--[Go to all publications](/publications/table/)-->