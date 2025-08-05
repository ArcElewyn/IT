# --- Proxmox Configuration (alimenté par GitHub Secrets) ---
# proxmox_url    = sera défini via TF_VAR_proxmox_url dans GitHub Actions
# proxmox_user   = sera défini via TF_VAR_proxmox_user dans GitHub Actions  
# proxmox_token  = sera défini via TF_VAR_proxmox_token dans GitHub Actions

# --- Proxmox target ---
proxmox_node         = "SRV-PROXMOX"

# --- VM configuration ---
vm_name              = "VM-DEDICATED"       # Nom de la VM
vm_id                = 110                  # ID de la VM (type number)
vm_memory            = 8000                 # Mémoire en Mo
vm_cores             = 4                    # Nombre de cœurs
vm_sockets           = 2                    # Nombre de sockets CPU

# --- Disque principal ---
disk_datastore_id    = "VMS"                # Datastore pour le disque
disk_size            = 60                   # Taille en Go
disk_iothread        = true                 # Activer iothread

# --- Image cloud-init ---
image_datastore_id   = "ISO"                # Datastore pour l'image
image_url            = "https://cloud.debian.org/images/cloud/bookworm/latest/debian-12-generic-amd64.qcow2"
image_file_name      = "debian12-cloud.img"

# --- Réseau ---
network_bridge       = "vmbr0"              # Bridge Proxmox

# --- SSH Key (alimenté par GitHub Secrets) ---
# cloudinit_sshkey = sera défini via TF_VAR_cloudinit_sshkey dans GitHub Actions
