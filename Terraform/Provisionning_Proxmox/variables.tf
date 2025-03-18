variable "proxmox_endpoint" {
  description = "Proxmox API URL"
  type        = string
}

variable "proxmox_api_token" {
  description = " API Token"
  type        = string
  sensitive   = true
}

variable "ssh_public_key_file" {
  description = " Path to pub SSH key"
  type        = string
  default     = "./id_rsa.pub"
}

variable "vm_name" {
  description = "VM name"
  type        = string
}

variable "proxmox_node" {
  description = "Proxmox Node name"
  type        = string
}

variable "vm_ipv4_address" {
  description = "IPv4 address with mask"
  type        = string
}

variable "vm_gateway" {
  description = "Default gateway"
  type        = string
}

variable "vm_username" {
  description = "default username"
  type        = string
}

variable "vm_password" {
  description = "Password for the VM user"
  type        = string
  sensitive   = true
}

variable "datastore_id" {
  description = "Datastore name for VM Disks "
  type        = string
}

variable "disk_interface" {
  description = "Disk interface (ex: virtio0)"
  type        = string
  default     = "virtio0"
}

variable "disk_iothread" {
  description = "Toggle iothread for the disk"
  type        = bool
  default     = true
}

variable "disk_discard" {
  description = "Toggle discard option for the disk"
  type        = string
  default     = "on"
}

variable "disk_size" {
  description = "Disk size"
  type        = number
}

variable "vm_memory" {
  description = "Ram quantity"
  type        = number
}

variable "vm_cores" {
  description = "Number of CPU core"
  type        = number
}

variable "vm_sockets" {
  description = "Number of CPU"
  type        = number
}

variable "network_bridge" {
  description = "Network bridge name(ex: vmbr0)"
  type        = string
}

variable "download_datastore_id" {
  description = "Datastore name for the image"
  type        = string
}

variable "cloud_image_url" {
  description = "Image URL "
  type        = string
}
