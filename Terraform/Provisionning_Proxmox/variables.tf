variable "proxmox_url" {
  description = "The Proxmox API endpoint URL"
  type        = string
}

variable "proxmox_user" {
  description = "Proxmox username"
  type        = string
}

variable "proxmox_token" {
  description = "Proxmox API token"
  type        = string
  sensitive   = true
}

variable "proxmox_node" {
  description = "Target Proxmox node"
  type        = string
}

variable "vm_name" {
  type        = string
  description = "Name of the virtual machine"
}

variable "vm_id" {
  type        = string
  description = "Virtual machine ID"
}

variable "vm_memory" {
  type        = number
  description = "Memory in MB"
}

variable "vm_cores" {
  type        = number
  description = "Number of vCPUs"
}

variable "vm_sockets" {
  type        = number
  description = "Number of sockets"
}

variable "disk_size" {
  type        = number
  description = "Disk size in GB"
}

variable "disk_iothread" {
  type        = bool
  description = "Enable iothread on disk"
}

variable "disk_datastore_id" {
  type        = string
  description = "Datastore for the disk"
}

variable "image_datastore_id" {
  type        = string
  description = "Datastore where the image will be downloaded"
}

variable "image_url" {
  type        = string
  description = "URL of the image to download"
}

variable "image_file_name" {
  type        = string
  description = "Name of the file to store the image as"
}

variable "network_bridge" {
  type        = string
  description = "Network bridge to attach the VM to"
}
