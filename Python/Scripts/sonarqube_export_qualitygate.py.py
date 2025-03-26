import requests

# Authentication configuration
SONAR_URL = ""
TOKEN = ""
HEADER = {'Authorization': 'Bearer {TOKEN}'}
PARAMS = {"p": 1, "ps": 500}  # Max limit of 500 projects per page

# Function to retrieve all projects
def get_all_projects():
    response_get_all_projects = requests.get(f"{SONAR_URL}api/components/search_projects", headers=HEADER, params=PARAMS)
    if response_get_all_projects.status_code == 200:
        data = response_get_all_projects.json()
        return data.get("components", [])
    else:
        print(f"Error retrieving projects: {response_get_all_projects.status_code}")
        return []

# Function to retrieve the quality gate of a project
def get_quality_gate_for_project(project_key):
    params = {"project": project_key}  # Use "project" as key
    response_get_quality_gate_for_project = requests.get(f"{SONAR_URL}api/qualitygates/get_by_project", headers=HEADER, params=params)
    if response_get_quality_gate_for_project.status_code == 200:
        data = response_get_quality_gate_for_project.json()
        # The response contains the key "qualityGate" if a quality gate is assigned
        return data.get("qualityGate", None)
    else:
        print(f"Error for project {project_key}: {response_get_quality_gate_for_project.status_code}")
        return None

# Main function to sort and display projects by Quality Gate
def main():
    # Retrieve all projects
    projects = get_all_projects()

    # Dictionary to organize projects by Quality Gate
    quality_gate_dict = {}

    # Retrieve the quality gate for each project and sort them in the dictionary
    for project in projects:
        project_key = project.get("key")
        project_name = project.get("name")
        quality_gate = get_quality_gate_for_project(project_key)
        
        if quality_gate:
            quality_gate_name = quality_gate.get("name", "Not Defined")
        else:
            quality_gate_name = "Not Defined"  # Projects without a Quality Gate will be classified under "Not Defined"
        
        # If the Quality Gate does not exist in the dictionary, add it
        if quality_gate_name not in quality_gate_dict:
            quality_gate_dict[quality_gate_name] = []

        # Add the project to the corresponding Quality Gate list
        quality_gate_dict[quality_gate_name].append(f"{project_name} (Project Key: {project_key})")

    # Open a file to write the results
    with open("quality_gate_results.txt", "w") as file:
        # Write sorted projects by Quality Gate into the file
        for quality_gate, projects in quality_gate_dict.items():
            file.write(f"\n[{quality_gate}]\n")
            for project in projects:
                file.write(f"- {project}\n")

    print("The results have been saved in 'quality_gate_results.txt'.")

# Auto-execution if imported
if __name__ == "__main__":
    main()
