---
layout: page
title: Publications Table
permalink: /publications
---

Publications in which the NAIR group has been involved:

<style>
.scrollable-table {
    max-height: 500px;
    overflow-y: auto;
    display: block;
    margin-bottom: 50px;
    overflow-x: auto;
    border: 1px solid #ddd;
    border-radius: 5px;
}

.scrollable-table table {
    width: 100%;
    border-collapse: collapse;
}

.scrollable-table th, .scrollable-table td {
    padding: 12px 15px;
    text-align: left;
    border-bottom: 1px solid #ddd;
}

.scrollable-table th {
    position: sticky;
    top: 0;
    background: white;
    box-shadow: 0 2px 2px -1px rgba(0, 0, 0, 0.4);
    background-color: #f2f2f2;
    color: #333;
    font-weight: bold;
    cursor: pointer;
}

.scrollable-table tbody tr:hover {
    background-color: #f1f1f1;
}

#myInput {
    width: 100%;
    font-size: 16px;
    padding: 12px;
    margin-top: 12px;
    margin-bottom: 12px;
    border: 1px solid #ddd;
    border-radius: 5px;
}
</style>

<script>
function myFunction() {
  var input, filter, table, tr, tdTitle, tdAuthors, i, txtValueTitle, txtValueAuthors;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  table = document.querySelector(".scrollable-table table");
  tr = table.getElementsByTagName("tr");

  for (i = 0; i < tr.length; i++) {
    tdTitle = tr[i].getElementsByTagName("td")[0];
    tdAuthors = tr[i].getElementsByTagName("td")[3];
    if (tdTitle && tdAuthors) {
      txtValueTitle = tdTitle.textContent || tdTitle.innerText;
      txtValueAuthors = tdAuthors.textContent || tdAuthors.innerText;
      if (txtValueTitle.toUpperCase().indexOf(filter) > -1 || txtValueAuthors.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }       
  }
}

document.addEventListener('DOMContentLoaded', function() {
  const getCellValue = (tr, idx) => tr.children[idx].innerText || tr.children[idx].textContent;

  const comparer = (idx, asc) => (a, b) => ((v1, v2) =>
      v1 !== '' && v2 !== '' && !isNaN(v1) && !isNaN(v2) ? v1 - v2 : v1.toString().localeCompare(v2)
  )(getCellValue(asc ? a : b, idx), getCellValue(asc ? b : a, idx));

  document.querySelectorAll('.sortable th').forEach(th => th.addEventListener('click', function() {
      const table = th.closest('table');
      Array.from(table.querySelectorAll('tbody tr'))
          .sort(comparer(Array.from(th.parentNode.children).indexOf(th), this.asc = !this.asc))
          .forEach(tr => table.querySelector('tbody').appendChild(tr) );
  }));
});
</script>

<input type="text" id="myInput" onkeyup="myFunction()" placeholder="Search for authors, institutions or titles..">

<div class="scrollable-table">
    <table class="sortable">
      <thead>
        <tr>
          <th>Title</th>
          <th>Year</th>
          <th>DOI</th>
          <th>Authors and Institutions</th>
        </tr>
      </thead>
      <tbody>
        {% for publication in site.data.publications %}
        <tr>
          <td>{{ publication.title }}</td>
          <td>{{ publication.year }}</td>
          <td><a href="https://doi.org/{{ publication.doi }}">{{ publication.doi }}</a></td>
          <td>
            {% if publication.authors_and_institutions %}
            <ul>
              {% for author_and_institution in publication.authors_and_institutions %}
              <li>
              {{ author_and_institution[0] }}
              {% if author_and_institution[1] %}
              - {{ author_and_institution[1] }}
              {% endif %}
              </li>
              {% endfor %}
            </ul>
            {% else %}
            N/A
            {% endif %}
          </td>
        </tr>
        {% endfor %}
      </tbody>
    </table>
</div>
