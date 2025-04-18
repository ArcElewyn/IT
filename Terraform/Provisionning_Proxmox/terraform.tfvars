proxmox_node        = "" # Name of your proxmox node
vm_name             = "" # Name of the vm you want to create
vm_id               = "" # ID of the VM
vm_memory           = 2048
vm_cores            = 2
vm_sockets          = 1

disk_datastore_id   = "" # Name of the datastore where you want to store your disks
disk_size           = 20
disk_iothread       = true

image_datastore_id  = "" # Name of the datastore where you want to download the image too
image_url           = "" # Url of the cloudimage OS you want to install
image_file_name     = "" # Name of the file once downloaded ( You want a .img, the provider will convert .qcow2 to .img)
network_bridge      = "" # Name of the bridge you want the vmnic to be in
