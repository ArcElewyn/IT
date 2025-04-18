# TERRAFORM/OPENTOFU

## Provisionning Proxmox with Terraform:
### Setting up your Proxmox server

First, on your Proxmox server create a role for Terraform, either with your web interface, or via SSH:

> pveum role add yourgroup -privs "Datastore.Allocate Datastore.AllocateSpace Datastore.Audit Datastore.AllocateTemplates Pool.Allocate Sys.Audit Sys.Console Sys.Modify VM.Allocate VM.Audit VM.Clone VM.Config.CDROM VM.Config.CPU VM.Config.Disk VM.Config.HWType VM.Config.Memory VM.Config.Network VM.Config.Options VM.Console VM.Migrate VM.Monitor VM.PowerMgmt SDN.Use"

Then create the dedicated user:

> pveum user add username@realm --password <password>

Next, add your new user to the group:

> pveum aclmod / -user youruser@realm -role yourgroup

Since the Terraform provider "Proxmox BPG" uses Proxmox's API, when your user is created and all set, generate your API token:

> pveum user token add youruser@realm tokenname -expire 0 -privsep 0 -comment "Terraform token"

---
### Setting up your Terraform Server
*We're going to install Terraform on a Debian 12 VM.* \
*https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli*

Ensure that your system is up to date and you have the necessary packages installed:
> sudo apt-get update && sudo apt-get install -y gnupg software-properties-common curl

Then, install HashiCorp's GPG key:
> wget -O- https://apt.releases.hashicorp.com/gpg | \
  gpg --dearmor | \
  sudo tee /usr/share/keyrings/hashicorp-archive-keyring.gpg > /dev/null

And verify the key's fingerprint:
> gpg --no-default-keyring \
  --keyring /usr/share/keyrings/hashicorp-archive-keyring.gpg \
  --fingerprint

Next, add HashiCorp's repository to your system:
> echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list

Finally, update your package list:
> sudo apt update

And install Terraform:
> sudo apt-get install terraform

To verify that the installation worked, try:
> terraform -help

---
### Installing the Proxmox provider
To provision Proxmox VMs, we need to set up a provider. We will use BPG's Proxmox provider *(https://registry.terraform.io/providers/bpg/proxmox/latest/docs)*.

First, create a project directory on your Terraform server:
> mkdir ~/terraform-proxmox-bpg && cd ~/terraform-proxmox-bpg

Inside this directory, create several files:
>
> /terraform-proxmox-bpg \
> ├── terraform.tfvars         # Actual Variables value \
> ├── variables.tf             # Declaration of Variables \
> ├── provider.tf              # (Optionnal) Provider configuration \
> ├── main.tf                  # Defining resources (VMs, containers...) \
> ├── outputs.tf               # Output file (VMs IPs...) \
> ├── modules/                 # (Optional) Terraform Modules \
> ├── .gitignore               # (Optional) To exclude terraform.tfvars & .terraform/ from versioning

### Example files:

#### variables.tf
```hcl
variable "proxmox_endpoint" {
  description = "The Proxmox API endpoint"
  type        = string
}

variable "proxmox_api_token_id" {
  description = "The Proxmox API token ID"
  type        = string
}

variable "proxmox_api_token_secret" {
  description = "The Proxmox API token secret"
  type        = string
  sensitive   = true
}
```

#### terraform.tfvars
```hcl
proxmox_endpoint = "https://<PROXMOX_IP>:8006/"
proxmox_api_token_id = "youruser@realm!tokenname"
proxmox_api_token_secret = "<SECRET_KEY>"
```

#### main.tf
```hcl
resource "proxmox_virtual_environment_vm" "debian_vm" {
  name      = var.vm_name
  node_name = var.proxmox_node

  memory {
    dedicated = var.vm_memory
  }

  cpu {
    cores   = var.vm_cores
    sockets = var.vm_sockets
  }

  initialization {
    ip_config {
      ipv4 {
        address = var.vm_ipv4_address
        gateway = var.vm_gateway
      }
    }
    user_account {
      username = var.vm_username
      password = var.vm_password
      keys     = [trimspace(data.local_file.ssh_public_key.content)]
    }
  }

  disk {
    datastore_id = var.datastore_id
    file_id      = proxmox_virtual_environment_download_file.debian_cloud_image.id
    interface    = var.disk_interface
    iothread     = var.disk_iothread
    discard      = var.disk_discard
    size         = var.disk_size
  }

  network_device {
    bridge = var.network_bridge
  }
}
```

#### outputs.tf
```hcl
output "vm_name" {
  description = "Name of the created VM"
  value       = proxmox_virtual_environment_vm.debian_vm.name
}

output "vm_ip" {
  value = proxmox_virtual_environment_vm.debian_vm.default_ipv4_address
}
```

After you populate your project's folder, ensure you are in your project directory, then to deploy your VMs, run:

> terraform init

This command will create the `.terraform` workspace, your tfstate file, and install the providers.

Then, to deploy your VMs:
> terraform apply # Use `-auto-approve` to skip confirmation

### Automate

I decided to automate the deployment with a github action worflow, using secrets and a dedicated runner (I won't detai everything here) 

```yml
name: Deploy Infrastructure

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  terraform:
    name: Terraform Apply on Proxmox
    runs-on: self-hosted

    defaults:
      run:
        working-directory: /home/terraform/Terraform/Provisioning/ 
    
    steps:
      - name: Git Pull latest changes
        run: |
          git pull

      - name: Terraform Init
        run: terraform init

      - name: Terraform Plan
        run: |
          terraform plan \
            -var="proxmox_url=${{ secrets.PROXMOX_URL }}" \
            -var="proxmox_token=${{ secrets.PROXMOX_TOKEN }}" \
            -var="proxmox_user=${{ secrets.PROXMOX_USER }}" \
            -var-file="terraform.tfvars"

      - name: Terraform Apply
        run: |
          terraform apply -auto-approve \
            -var="proxmox_url=${{ secrets.PROXMOX_URL }}" \
            -var="proxmox_token=${{ secrets.PROXMOX_TOKEN }}" \
            -var="proxmox_user=${{ secrets.PROXMOX_USER }}" \
            -var-file="terraform.tfvars"
```