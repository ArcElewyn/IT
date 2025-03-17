import requests
import csv
import getpass
import sys
import datetime
from requests.auth import HTTPBasicAuth

# Directly define variables
requettejql = 'project = HL ORDER BY createdDate ASC'
username = '' 
password = ""
urljira = ''
step = 1000
start = 0

# Fields to keep
champs_a_garder = [
    "Résumé", "Clé de ticket", "Type de ticket", "Etat", "Clé de projet", 
    "Nom du projet", "Priorité", "Résolution", "Responsable", "Rapporteur", 
    "Créateur", "Création", "Mise à jour", "Résolue", "Niveau de sécurité",
    "Champs personnalisés (Domaine Métier)", "Champs personnalisés (HL - Gravité)", 
    "Champs personnalisés (Organisme - Niveau de gravité)", "Champs personnalisés (Filière)", 
    "Champs personnalisés (SLA)"
]

# Output file name
csvfinal = f"TicketsHL_{datetime.datetime.now().strftime('%Y%m%d')}.csv"

# URL to retrieve issues in CSV format
url = f"{urljira}/sr/jira.issueviews:searchrequest-csv-all-fields/temp/SearchRequest.csv?jqlQuery={requettejql}"

# Override the character limit in the CSV
csv.field_size_limit(1000000)

# Export Jira to CSV (in batches of 'step' issues)
with open('TicketsHL.csv', 'w', encoding='utf-8-sig', newline='') as csvfile:
    writer = None
    tickets_exportes = 0
    
    while True:
        print(f"{start} issues exported")
        theurl = f"{url}&tempMax={step}&pager/start={start}"
        resp = requests.get(theurl, auth=(username, password), verify=False)

        # Read the CSV
        reader = csv.DictReader(resp.text.splitlines(), delimiter=',')

        # Initialize the writer with detected fields
        if writer is None:
            all_fieldnames = reader.fieldnames
            writer = csv.DictWriter(csvfile, fieldnames=all_fieldnames, delimiter=',')
            writer.writeheader()

        rows = list(reader)

        # Update fieldnames if new fields are found
        for row in rows:
            for key in row.keys():
                if key not in all_fieldnames:
                    all_fieldnames.append(key)
        
        # Rewrite the CSV with new fields
        writer = csv.DictWriter(csvfile, fieldnames=all_fieldnames, delimiter=',')
        writer.writerows(rows)

        # Stop if fewer tickets are returned than the batch size
        if len(rows) < step:
            break

        start += step

# For each ticket, make an API request to retrieve only the customfield_10106 field
with open('TicketsHL.csv', 'r', encoding='utf-8-sig') as infile:
    reader = csv.DictReader(infile)
    # Ensure the fields defined in champs_a_garder are retained
    champs_existants = [col for col in champs_a_garder if col in reader.fieldnames]
    if "Champs personnalisés (Organisme - Niveau de gravité)" not in champs_existants:
        champs_existants.append("Champs personnalisés (Organisme - Niveau de gravité)")

    lignes_mises_a_jour = []

    for row in reader:
        issue_key = row["Clé de ticket"]
        # Dynamic request: only request the customfield_10106 field for the current issue
        requette_individuelle = f"{urljira}rest/api/2/issue/{issue_key}?fields=customfield_10106"

        response = requests.get(
            requette_individuelle,
            auth=HTTPBasicAuth(username, password),
            headers={"Accept": "application/json"},
            verify=False
        )

        if response.status_code == 200:
            issue_data = response.json()
            champ_perso = issue_data["fields"].get("customfield_10106", "Non renseigné")

            # If the field is a list, convert it to a string
            if isinstance(champ_perso, list):
                champ_perso = ", ".join(map(str, champ_perso))

            row["Champs personnalisés (Organisme - Niveau de gravité)"] = champ_perso
        else:
            print(f"Error {response.status_code} for issue {issue_key}")
            row["Champs personnalisés (Organisme - Niveau de gravité)"] = "API Error"

        lignes_mises_a_jour.append(row)

# Filter and write only the fields to keep in the final CSV file
lignes_filtrees = []
for row in lignes_mises_a_jour:
    # Keep only the keys defined in champs_a_garder
    row_filtre = { key: row.get(key, "") for key in champs_a_garder }
    lignes_filtrees.append(row_filtre)

with open(csvfinal, 'w', encoding='utf-8-sig', newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=champs_a_garder)
    writer.writeheader()
    writer.writerows(lignes_filtrees)

print(f"Export completed and saved in: {csvfinal}")
