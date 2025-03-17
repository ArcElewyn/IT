# Variables for the VM
variable "vm_name" {
  description = "Name of the virtual machine"
  type        = string
}

variable "node_name" {
  description = "Name of the Proxmox node where the VM will be deployed"
  type        = string
  default     = "pve"
}

variable "template_name" {
  description = "Name of the VM template to clone"
  type        = string
  default     = "debian-template"
}

variable "cpumode" {
  description = "CPU mode for the VM (e.g., host, kvm64, etc.)"
  type        = string
  default     = "host"
}

variable "storage_name" {
  description = "Name of the storage where the VM will be installed"
  type        = string
  default     = "vm"
}

variable "bridge_name" {
  description = "Name of the network bridge for the VM"
  type        = string
  default     = "vmbr0"
}

variable "username" {
  description = "Username for cloud-init configuration"
  type        = string
}

variable "password" {
  description = "Password for cloud-init configuration"
  type        = string
  sensitive   = true
}

# Variables for Proxmox provider configuration
variable "proxmox_endpoint" {
  description = "URL of the Proxmox API"
  type        = string
}

variable "proxmox_api_token_id" {
  description = "Proxmox API token ID"
  type        = string
}

variable "proxmox_api_token_secret" {
  description = "Proxmox API token secret"
  type        = string
  sensitive   = true
}
