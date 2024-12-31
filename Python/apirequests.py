import requests
import datetime
import getpass

# Définition des identifiants pour jira
password = getpass.getpass("tapez mot de passe jira du compte svcauto: ")
identifiants_jira = ("user", password)
# Formatage date actuelle
date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

# Fonction pour lister les projets du portefolio Dependency_Track
def lister_projets():
    url_projets = "http://serveurdependency-track/api/v1/project?pageNumber=1&pageSize=100"
    entetes = {
        "accept": "application/json",
        "X-Api-Key": "cleapi"
    }
    reponse = requests.get(url_projets, headers=entetes)
    if reponse.status_code == 200:
        return reponse.json()  # Retourne la liste des projets
    else:
        print(f"Erreur lors de la récupération des projets. Code: {reponse.status_code}")
        return []

# Fonction pour récupérer les vulnérabilités d'un projet
def recuperer_vulnerabilites(uuid_projet):
    url_vuln = f"http://serveurdependency-track/api/v1/vulnerability/project/{uuid_projet}"
    reponse_vuln = requests.get(url_vuln, headers={"accept": "application/json"})
    if reponse_vuln.status_code == 200:
        return reponse_vuln.json()  # Retourne la liste des vulnérabilités
    else:
        print(f"Erreur lors de la récupération des vulnérabilités pour le projet {uuid_projet}.")
        return []

# Fonction pour vérifier l'existence d'un ticket Jira
def verifier_ticket_jira(uuid_projet):
    url_jira_recherche = "http://serveurjira/rest/api/2/search"
    requete_jql = {
        "jql": f"project = SID AND issuetype = \"dependencytrack\" AND summary ~ \"{uuid_projet}\" ORDER BY created DESC",
        "maxResults": 1
    }
    reponse_jira = requests.get(url_jira_recherche, auth=identifiants_jira, headers={"Content-Type": "application/json"}, params=requete_jql)
    if reponse_jira.status_code == 200:
        resultat_recherche = reponse_jira.json()
        return resultat_recherche['issues']
    else:
        print(f"Erreur lors de la recherche du ticket Jira pour le projet {uuid_projet}.")
        return []

# Fonction pour ajouter un commentaire à un ticket Jira existant
def ajouter_commentaire_ticket_jira(ticket_id, details_vulnerabilites):
    url_jira_commentaire = f"http://serveurjira/rest/api/2/issue/{ticket_id}/comment"
    commentaire = {
        "body": f"{date}, vulnérabilités :\n{details_vulnerabilites}"
    }
    reponse_commentaire = requests.post(url_jira_commentaire, auth=identifiants_jira, headers={"Content-Type": "application/json"}, json=commentaire)
    if reponse_commentaire.status_code == 201:
        print(f"Commentaire ajouté au ticket Jira {ticket_id}.")
    else:
        print(f"Erreur lors de l'ajout du commentaire au ticket Jira {ticket_id}. Code: {reponse_commentaire.status_code}")

# Fonction pour créer un ticket Jira
def creer_ticket_jira(uuid_projet, nom_du_projet, details_vulnerabilites):
    ticket = {
        "fields": {
            "project": {"key": "SID"},
            "issuetype": {"name": "dependencytrack"},
            "summary": f"{date} Vulnérabilités du projet {nom_du_projet}, uuid: {uuid_projet}",
            "description": f"Liste des vulnérabilités pour le projet {nom_du_projet}: {details_vulnerabilites}"
        }
    }
    url_jira_ticket = "http://serveurjira/rest/api/2/issue"
    reponse_ticket = requests.post(url_jira_ticket, auth=identifiants_jira, headers={"Content-Type": "application/json"}, json=ticket)
    if reponse_ticket.status_code == 201:
        print(f"Ticket Jira créé avec succès pour le projet {nom_du_projet}.")
    else:
        print(f"Échec de la création du ticket Jira pour le projet {nom_du_projet}. Code: {reponse_ticket.status_code}")

# Fonction pour formater les détails des vulnérabilités
def formater_details_vulnerabilites(vulnerabilites):
    details = ""
    for vuln in vulnerabilites:
        vulnid = vuln.get("vulnId", "Inconnu")
        description = vuln.get("description", "Pas de description")
        severity = vuln.get("severity", "Inconnue")
        composants = vuln.get("components", [])
        details += f"\n- **Vuln ID**: {vulnid}\n  **Description**: {description}\n  **Sévérité**: {severity}\n  **Composants**:\n"
        for comp in composants:
            details += f"    - Nom: {comp.get('name', 'Inconnu')}, Version: {comp.get('version', 'Inconnue')}, Type: {comp.get('classifier', 'Inconnu')}\n"
    return details

#Script
lister_projets = lister_projets()
for projet in lister_projets:
    uuid_projet = projet['uuid']
    nom_du_projet = projet['name']
    
    # Récupérer les vulnérabilités pour chaque projet
    vulnerabilites = recuperer_vulnerabilites(uuid_projet)
    details_vulnerabilites = formater_details_vulnerabilites(vulnerabilites)

    # Vérifier si un ticket Jira existe déjà pour ce projet
    tickets_existants = verifier_ticket_jira(uuid_projet)
    if tickets_existants:
        # Si un ticket existe, on ajoute un commentaire
        ticket_id = tickets_existants[0]['key']
        ajouter_commentaire_ticket_jira(ticket_id, details_vulnerabilites)
    else:
        # Sinon, on crée un nouveau ticket Jira
        creer_ticket_jira(uuid_projet, nom_du_projet, details_vulnerabilites)

# # Requete API pour lister projets du portefolio
# url = "http://serveurdependency-track/api/v1/project?pageNumber=1&pageSize=100"
# headers = {
#     "accept": "application/json",
#     "X-Api-Key": "cleapi"
# }
# apiDT_listerprojets = requests.get(url, headers=headers)
# print(apiDT_listerprojets.status_code)

# # Conversion données en json pour parser
# liste_projets = apiDT_listerprojets.json()

# # Parser résultats pour récupérer nom du projet + uuid
# liste_projets_resultats = [{'name': entry['name'], 'uuid': entry['uuid']} for entry in liste_projets]

# # Pour chaque projet, lister les vulnérabilités
# for projet in liste_projets_resultats:
#     uuid_projet = projet['uuid']
#     nomduprojet = projet['name']
    
#     # Réinitialisation des détails de vulnérabilité pour ce projet
#     vuln_detail = ""  

#     # Requête API pour récupérer les vulnérabilités du projet
#     url_vuln = f"http://serveurdependency-track/api/v1/vulnerability/project/{uuid_projet}"
#     api_getvulvnerability = requests.get(url_vuln, headers=headers)
    
#     # Interprétation des résultats de la requête API
#     liste_vulnerabilites = api_getvulvnerability.json()

#     for vuln in liste_vulnerabilites:
#         vulnid = vuln.get("vulnId")
#         description = vuln.get("description")
#         severity = vuln.get("severity")
        
#         components = [
#             {
#                 "name": comp.get("name"),
#                 "version": comp.get("version"),
#                 "classifier": comp.get("classifier")
#             } for comp in vuln.get("components", [])
#         ]
        
#         vuln_detail += f"\n- **Vuln ID**: {vulnid}\n  **Description**: {description}\n  **Severity**: {severity}\n  **Composants**:\n"
#         for comp in components:
#             vuln_detail += f"    - Nom: {comp['name']}, Version: {comp['version']}, Type: {comp['classifier']}\n"
    
#     # Verifier si ticket jira existant en fonction de l'uuid du projet
#     url_jira_checkifexist = f"http://serveurjira/rest/api/2/search"
#     requete_checkifexist = {
#         "jql": f"project = SID AND issuetype = \"dependencytrack\" AND summary ~ \"{uuid_projet}\" ORDER BY created DESC",
#         "maxResults": 1
#     }
#     api_jira_search =  requests.get(url_jira_checkifexist, auth=identifiants_jira, headers={"Content-Type": "application/json"}, params=requete_checkifexist)
#     if api_jira_search.status_code == 200:
#         resultat_recherche_jira = api_jira_search.json()
#         # Si ticket avec uuid projet identique existe deja, ajout commentaire
#         if resultat_recherche_jira['total'] > 0:
#             id_ticket_existant = resultat_recherche_jira['issues'][0]['key']
#             comment = {
#                 "body": f"{date}, vulnérabilités :\n{vuln_detail}"
#             }
#             url_jira_comment = f"http://jserveurjira/rest/api/2/issue/{id_ticket_existant}/comment"
#             api_jira_add_comment = requests.post(url_jira_comment, auth=identifiants_jira, headers={"Content-Type": "application/json"}, json=comment)
#             if api_jira_add_comment.status_code == 201:
#                 print(f"Commentaire ajouté au ticket Jira {id_ticket_existant} pour le projet {nomduprojet}.")
#             else:
#                 print(f"Erreur lors de l'ajout du commentaire au ticket Jira {id_ticket_existant}. Code: {api_jira_add_comment.status_code}")
#         # Sinon création ticket jira pour le projet
#         else:
#             # Template ticket Jira
#             issue = {
#                 "fields": {
#                     "project": {
#                         "key": "SID"
#                     },
#                     "issuetype": {
#                         "name": "dependencytrack"
#                     },
#                     "summary": f"{date} Vulnérabilités du projet {nomduprojet}, uuid: {uuid_projet}",
#                     "description": f"Liste des vulnérabilités pour le projet {nomduprojet}: {vuln_detail}"
#                 }
#             }
#             # Requête API pour création ticket Jira
#             url_jira_ticket = "http://serveurjira/rest/api/2/issue"
#             jira_headers = {
#                 "Content-Type": "application/json",
#             }
#             retour_api_ticket_jira = requests.post(url_jira_ticket, auth=identifiants_jira, headers=jira_headers, json=issue)
#             # Vérification de la réponse API
#             if retour_api_ticket_jira.status_code == 201:
#                 print(f"Ticket Jira créé avec succès pour le projet {nomduprojet}.")
#             else:
#                 print(f"Échec de création du ticket Jira pour le projet {nomduprojet}. "
#                     f"Code: {retour_api_ticket_jira.status_code}, Message: {retour_api_ticket_jira.text}")
#     else:
#         print(f"Erreur lors de la recherche du ticket Jira pour le projet {nomduprojet}. Code: {api_jira_search.status_code}, Message: {api_jira_search.text}")
