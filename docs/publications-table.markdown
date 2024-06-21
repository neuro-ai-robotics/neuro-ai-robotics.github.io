---
layout: page
title: Publications Table
permalink: /publications/table
---

Publications in which the NAIR group has been involved:

<style>
.scrollable-table {
    max-height: 500px;
    overflow-y: auto;
    display: block;
    margin-bottom: 50px;
    overflow-x: auto;
}

.scrollable-table table {
    width: 100%;
    border-collapse: collapse;
}

.scrollable-table th{
    position: sticky;
    top: 0;
    background: white;
    box-shadow: 0 2px 2px -1px rgba(0, 0, 0, 0.4);
    background-color: #f2f2f2; /* Cambia esto al color que prefieras */
    color: black; /* Cambia esto al color que prefieras para el texto */
}

#myInput {
  width: 50%;
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
    tdTitle = tr[i].getElementsByTagName("td")[0]; // Get the first column (Title)
    tdAuthors = tr[i].getElementsByTagName("td")[3]; // Get the fourth column (Authors and Institutions)
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
</script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/sorttable/2.0.0/sorttable.min.js"></script>


<input type="text" id="myInput" onkeyup="myFunction()" placeholder="Search for authors, institutions or titles..">

<div class="scrollable-table">
    <table class="sortable">
      <tr>
        <th>Title</th>
        <th>Year</th>
        <th>DOI</th>
        <th>Authors and Institutions</th>
      </tr>
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
    </table>
</div>