import requests
import csv
from datetime import datetime

# Générer la date au format MM-YYYY
date = datetime.now().strftime("%m-%Y")
filename = f"users_gitlab_{date}.csv"

# Params
url = "https://gitlab/api/v4/"
headers = {
    "PRIVATE-TOKEN": ""
}

# List all groups and its members
get_groups = requests.get(f"{url}/groups?top_level_only=yes", headers=headers)

if get_groups.status_code == 200:
    groups = get_groups.json()

    with open(filename, mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        # Entêtes CSV
        writer.writerow(["group id", "groupname", "user id", "username", "name"])

        for group in groups:
            get_groups_members = requests.get(f"{url}/groups/{group['id']}/members?per_page=100", headers=headers)
            if get_groups_members.status_code == 200:
                groups_members = get_groups_members.json()
                for member in groups_members:
                    if member['state'] != 'blocked':
                        writer.writerow([
                            group["id"],
                            group["full_name"],
                            member["id"],
                            member["username"],
                            member["name"]
                        ])
