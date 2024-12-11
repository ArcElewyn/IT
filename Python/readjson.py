# Import module
import json
import os
import csv
import sys

jsonPath = sys.argv[1]

# Clear the content of hosts_paths.csv
with open("path_of_.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["App", "Env", "Host", "Path"])

# Open json file
with open(jsonPath, 'r') as f:
    data = json.load(f)

# For each app, list app name, env, hostname, and the path of the app on the host and write it on .csv
for app_name, app_data in data.items():
    for env_data in app_data:
        try:
            for env_name, env_info in env_data.items():
                hosts = env_info.get("host", [])
                if isinstance(hosts, list):
                    for host in hosts:
                        host_name = host.get("host", "Unknown Host")
                ssh_app_dir = env_info.get("sshAppDir", "Unknown sshAppDir")
                deploy_dir = env_info.get("deployDir", "Unknown deployDir")
                with open("path_of_.csv", "a", newline='') as f:
                    writer = csv.writer(f)
                    if deploy_dir.startswith("/"):
                        writer.writerow([app_name, env_name, host_name, f"{ssh_app_dir.rstrip('/')}{deploy_dir}"])
                    elif deploy_dir == "":
                        writer.writerow([app_name, env_name, host_name, ssh_app_dir])
                    elif not deploy_dir.startswith("/"):
                        writer.writerow([app_name, env_name, host_name, f"{ssh_app_dir.rstrip('/')}/{deploy_dir}"])               
        except Exception as app_error:
            print("Error processing application " + app_name + " : " + str(app_error))
