# Variables pour la VM
variable "vm_name" {
  description = "Nom de la machine virtuelle"
  type        = string
}

variable "node_name" {
  description = "Nom du nœud Proxmox où la VM sera déployée"
  type        = string
  default     = "pve"
}

variable "template_name" {
  description = "Nom du modèle de la VM à cloner"
  type        = string
  default     = "debian-template"
}

variable "cpumode" {
  description = "Mode CPU pour la VM (ex. host, kvm64, etc.)"
  type        = string
  default     = "host"
}

variable "storage_name" {
  description = "Nom du stockage où la VM sera installée"
  type        = string
  default     = "vm"
}

variable "bridge_name" {
  description = "Nom du bridge réseau pour la VM"
  type        = string
  default     = "vmbr0"
}

variable "username" {
  description = "Nom d'utilisateur pour la configuration cloud-init"
  type        = string
}

variable "password" {
  description = "Mot de passe pour la configuration cloud-init"
  type        = string
  sensitive   = true
}

# Variables pour la configuration du provider Proxmox
variable "proxmox_endpoint" {
  description = "URL de l'API Proxmox"
  type        = string
}

variable "proxmox_api_token_id" {
  description = "ID du token API Proxmox"
  type        = string
}

variable "proxmox_api_token_secret" {
  description = "Secret du token API Proxmox"
  type        = string
  sensitive   = true
}
