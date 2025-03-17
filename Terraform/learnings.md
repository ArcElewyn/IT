# TERRAFORM/OPENTOFU

## Provisionning Proxmox with Terraform:
### Setting up your Proxmox server

First, on your Proxmox server create a role for Terraform, either with your web interface, or via ssh:

> pveum role add yourgroup -privs "Datastore.Allocate Datastore.AllocateSpace Datastore.Audit Pool.Allocate Sys.Audit Sys.Console Sys.Modify VM.Allocate VM.Audit VM.Clone VM.Config.CDROM VM.Config.Cloudinit VM.Config.CPU VM.Config.Disk VM.Config.HWType VM.Config.Memory VM.Config.Network VM.Config.Options VM.Console VM.Migrate VM.Monitor VM.PowerMgmt SDN.Use"

Then create the dedidated user :

> pveum user add username@realm --password <password>

Next, add your new user to the group:

>pveum aclmod / -user youruer@realm -role yourgroup

Since the Terraform's provider "Proxmox BPG" use Proxmox's API, When your user is created and all set, generate your api token:

> pveum user token add youruser@realm tokenname -expire 0 -privsep 0 -comment "Terraform token"

In order to start provisionning vms, we need a template, in our case, we are gonna use a debian template, to do so, create the vm as you would usualy do, then install cloud_inint :
>apt install cloud-init

verify it works by doing:
> sudo cloud-init status --long

Then shutdown the vm then convert it to template

---
### Setting up your Terraform Server
*We're gonna install terraform on a Debian 12 VM.* \
*https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli*

Ensure that your system is up to date and you have the gnupg, software-properties-common, and curl packages installed:
>sudo apt-get update && sudo apt-get install -y gnupg software-properties-common

Then, install Hashicorp's GPG key:
> wget -O- https://apt.releases.hashicorp.com/gpg | \
gpg --dearmor | \
sudo tee /usr/share/keyrings/hashicorp-archive-keyring.gpg > /dev/null

And verify the key's fingerprint: 
>gpg --no-default-keyring \
--keyring /usr/share/keyrings/hashicorp-archive-keyring.gpg \
--fingerprint

Next, add the Hashicorp's repository to your system:
>echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] \
https://apt.releases.hashicorp.com $(lsb_release -cs) main" | \
sudo tee /etc/apt/sources.list.d/hashicorp.list

Finaly do a quick update:
>sudo apt update

And install Terraform:
>sudo apt-get install terraform

To verify that the installation worked, try:
>terraform -help
---

### Installing the proxmox's provider
In order to start provisionning proxmox VMs, we need to set up a provider, we are gonna use BPG's proxmox provider *(https://registry.terraform.io/providers/bpg/proxmox/latest/docs)*

The first step, is to create, on our terraform server, a project
>mkdir ~/terraform-proxmox-bpg && cd ~/terraform-proxmox-bpg

In this  directoty, we create severals files:
 >/terraform-proxmox-bpg \
│── terraform.tfvars         # Actual Variables value \
│── variables.tf             # Declaration of Variables \
│── providers.tf             # Provider configuration \
│── main.tf                  # Defining ressources (VMs, containers...) \
│── outputs.tf               # Output file (VMs IPs...) \
│── modules/                 # (Optionnal) Terraform Modules \
│── .gitignore               # (Optionnal) To exclude terraform.tfvars & .terraform/ from versionning

In the provider.tf file, add:
>terraform { \
&nbsp;&nbsp;required_providers { \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;proxmox = { \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source  = "bpg/proxmox" \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version = ">= 0.50.0" \
&nbsp;&nbsp;&nbsp;&nbsp;} \
&nbsp;&nbsp;} \
} \
provider "proxmox" { \
&nbsp;&nbsp;endpoint        = var.proxmox_endpoint \
&nbsp;&nbsp;api_token_id    = var.proxmox_api_token_id \
&nbsp;&nbsp;api_token_secret = var.proxmox_api_token_secret \
&nbsp;&nbsp;insecure        = true  # false if SSL is configured \
}

In the variable.fr file, declare the variable we are gonna use:

>variable "proxmox_endpoint" { \
  description = "The Proxmox API endpoint" \
} \
variable "proxmox_api_token_id" { \
  description = "The Proxmox API token ID" \
} \
variable "proxmox_api_token_secret" { \
  description = "The Proxmox API token secret" \
} 

In the terraform.tfvars set the values of our previously declared variables:
>proxmox_endpoint = "https://<PROXMOX_IP>:8006/" \
proxmox_api_token_id = "youruser@realm!tokenname" \
proxmox_api_token_secret = "<SECRET_KEY>" 

Then, in our main.tf file, we declare ressources, such as a vm or a container: \
*For a debian vm*
> resource "proxmox_vm_qemu" "debian_vm" { \
&nbsp;&nbsp;name        = "vmname" # Name of the vm you are gonna create \
&nbsp;&nbsp;target_node = "nodename" # Name of the proxmox node \
&nbsp;&nbsp;clone       = "templatename" # Name of the template \
\
&nbsp;&nbsp;cpu    = "host" \
&nbsp;&nbsp;sockets = 1 \
&nbsp;&nbsp;cores  = 2 \
&nbsp;&nbsp;memory = 2048 \
&nbsp;&nbsp;balloon = 1024 # The balloon is the amount of dynamic ram the vm can use \ 
\
&nbsp;&nbsp;disk { \
&nbsp;&nbsp;&nbsp;&nbsp;size  = "20G" \
&nbsp;&nbsp;&nbsp;&nbsp;type  = "virtio" \
&nbsp;&nbsp;&nbsp;&nbsp;storage = "nameofyourstorage" # Default is local-lvm \
&nbsp;&nbsp;&nbsp;&nbsp;} \
\
&nbsp;&nbsp;network { \
&nbsp;&nbsp;&nbsp;&nbsp;model  = "virtio" \
&nbsp;&nbsp;&nbsp;&nbsp;bridge = "nameofthebridge" # Default is vmbr0 \
&nbsp;&nbsp;} \
\
&nbsp;&nbsp;os_type    = "cloud-init" \
&nbsp;&nbsp;ciuser     = "username" \
&nbsp;&nbsp;cipassword = "password" \
}

For your outputs.tf file:
>output "vm_ip" { \
&nbsp;&nbsp;value = proxmox_vm_qemu.debian_vm.default_ipv4_address \
}

After you populate your project's folder, make sure you are in your project directory, then to deploy your vms,do:

> terraform init

This command will create the .terraform workspace, your tfstate file, install the providers.. 

Then to deploy your vms: 
>terraform apply # use -auto-approve to skip confirmation


