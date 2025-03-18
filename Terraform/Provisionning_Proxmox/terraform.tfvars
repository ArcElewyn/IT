# VM configuration
proxmox_endpoint = ""
proxmox_api_token = ""
ssh_public_key_file = ""
vm_name = ""
proxmox_node = ""
vm_username = ""
vm_password = ""
# Hardware configuration
vm_memory = 2048
vm_cores   = 2  
vm_sockets = 1  
datastore_id = "local-lvm"
disk_interface = ""
disk_iothread = true
disk_discard = "on"
disk_size = 20

# Network configuration
vm_ipv4_address = ""
vm_gateway = ""
network_bridge = "vmbr0"

# Image configuration
download_datastore_id = "local"
cloud_image_url = "https://cdimage.debian.org/cdimage/cloud/bookworm/latest/debian-12-genericcloud-amd64.qcow2"
