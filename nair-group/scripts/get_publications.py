import requests
import yaml
import xml.etree.ElementTree as ET

def get_authors_and_institutions_by_doi(doi):
    url = f"https://api.crossref.org/works/{doi}"
    response = requests.get(url)
    if response.status_code == 200 and response.text.strip():
        data = response.json()
        if 'author' in data['message']:
            authors = data['message']['author']
            authors_and_institutions = []
            for author in authors:
                name = f"{author['given']} {author['family']}"
                affiliations = author.get('affiliation', [])
                institution = affiliations[0].get('name', None) if affiliations else None
                authors_and_institutions.append([name, institution])
            return authors_and_institutions
        else:
            print(f'No author data found for DOI {doi}')
            return None
    else:
        print(f'Error fetching data for DOI {doi}: {response.status_code}')
        return None

orcids = ['0000-0001-9154-0798']  # Reemplaza estos con los ORCIDs que quieras buscar
publications = []

for orcid in orcids:
    response = requests.get('https://pub.orcid.org/v3.0/' + orcid + '/works')
    if response.status_code == 200:
        try:
            root = ET.fromstring(response.content)
            for group in root.findall('{http://www.orcid.org/ns/activities}group'):
                for summary in group.findall('{http://www.orcid.org/ns/work}work-summary'):
                    title = summary.find('{http://www.orcid.org/ns/work}title/{http://www.orcid.org/ns/common}title').text
                    year = summary.find('{http://www.orcid.org/ns/common}publication-date/{http://www.orcid.org/ns/common}year').text
                    doi_element = summary.find('{http://www.orcid.org/ns/common}external-ids/{http://www.orcid.org/ns/common}external-id/{http://www.orcid.org/ns/common}external-id-value')
                    doi = doi_element.text if doi_element is not None else None
                    authors_and_institutions = get_authors_and_institutions_by_doi(doi) if doi else None
                    publications.append((title, year, doi, authors_and_institutions))  # Añade la publicación como una tupla
        except ET.ParseError:
            print(f'Error parsing XML for ORCID {orcid}')
    else:
        print(f'Error fetching data for ORCID {orcid}: {response.status_code}')

# Convertir el conjunto a una lista de diccionarios para la serialización a YAML
publications_list = [{'title': title, 'year': year, 'doi': doi, 'authors_and_institutions': authors_and_institutions} for title, year, doi, authors_and_institutions in publications]
# Ordenar la lista de publicaciones por año
publications_list = sorted(publications_list, key=lambda pub: pub['year'])

with open('_data/publications.yml', 'w+') as file:
    documents = yaml.dump(publications_list, file)