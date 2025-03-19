### Configurating Proxmox VMs with Ansible  
*After Terraform create our vm, we can push things a bit further by integrating ansible to configure our vms post provisionning*  
*https://docs.ansible.com/ansible/latest/*

## Installing Ansible  
*We are gonna install our ansible server on a debian 12 VM*  

Firstly, we need to have our ansible server up and running. To do so:

Verify if whether python is installed (nowadays, it is installed by default on Debian):  
> python3 --version  

If not:  
> apt install python3  

Next, we are gonna need Ansible GPG keys and repos:  

Install the prerequisite:  
> apt install -y software-properties-common  

Then add the Ansible repository:  
> add-apt-repository ppa:ansible/ansible  

Do a quick update of the packages:  
> apt update  

Lastly, install Ansible then verify if the installation has worked:  
> apt install -y ansible  
> ansible --version  

# Setting up ansible for proxmox integration  

Install the proxmox plugin by installing the collection "community.general":  
> ansible-galaxy collection install community.general  

We want a clean ansible project, so we need a nice tree with several folders:

> ansible/ \  
> ├── ansible.cfg                   # Main Ansible config file \
> ├── README.md                     \
> ├── inventories/ \
> │   ├── dynamic/ \
> │   │   └── proxmox.inventory.yaml  # Dynamic inventory file (Proxmox plugin) \
> │   └── static/ \
> │       └── hosts.ini             # Static inventory file \
> ├── group_vars/ \
> │   └── all.yml                   # Global variables \
> ├── playbooks/ \
> │   ├── site.yml                  # Main playbook \
> │   └── roles/ \
> │       └── common/               # Exemple role \
> │           ├── tasks/ \
> │           │   └── main.yml \
> │           └── vars/             # Variables for specific roles \
> │               └── main.yml \
> ├── files/                        # Folder for the files that are required on an host \
> ├── templates/                    # Jinja2 Templates \
> ├── vault/ \
> │   └── secrets.yml               # Encrypted files (Ansible Vault)

After we create our tree, make sure you have an API token from your proxmox (otherwise, go check my "guide" [Provisionning Proxmox](https://github.com/ArcElewyn/IT/tree/main/Terraform)).

Good practices recommend not leaving the key in plain text in our files, so we are gonna use ansible-vault to encrypt our secrets/key:  
> ansible-vault create vault/secrets.yml  

Inside the vault file, add:  
> proxmox_url: "https://proxmox.exemple.com:8006" \
 proxmox_user: "terraform-prov@pve" \
 proxmox_token_id: "terraform" \
 proxmox_token_secret: "api-key"

Next, we need to fill our "proxmox.inventory.yaml":
> plugin: community.general.proxmox \
 url: https://proxmox.exemple.com:8006 \
 user: 'terraform-prov@pve' \
 token_id: 'terraform' \
 token_secret: 'your_secret_token' \
 validate_certs: false \
 \
 want_facts: true \
 hostnames: \
 &nbsp;&nbsp;\- name \
 compose: \
 &nbsp;&nbsp;ansible_host: proxmox_ipconfig0_ip

To test if our inventory works, try:  
> ansible-inventory -i ansible/inventories/dynamic/proxmox.inventory.yaml --graph

When it's done, we can create whatever playbook we need and run it with our new inventory:  
> ansible-playbook -i inventories/dynamic/inventory.proxmox.yaml playbook/ourplaybook.yml
