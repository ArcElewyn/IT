# Variables for the VM
vmname           = "homelab-debian-vm"
node_name        = "pve"  # Proxmox node name
template_name    = "debian-template"  # Template to clone
cpumode          = "host"  # CPU mode for the VM (e.g., "host")
storage_name     = "local-lvm"  # Storage where the VM will be created
bridge_name      = "vmbr0"  # Network bridge for the VM
username         = "admin"  # Username for Cloud-Init
password         = "securepassword"  # Password for Cloud-Init

# Variables for the Proxmox provider
proxmox_endpoint        = "https://<PROXMOX_IP>:8006/"  # URL of your Proxmox server
proxmox_api_token_id    = "terraform@pve!terraform-token"  # Proxmox API token ID
proxmox_api_token_secret = "your_api_token_secret"  # Secret associated with your Proxmox API token
