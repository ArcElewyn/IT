terraform {
  required_providers {
      proxmox = {
      source = "bpg/proxmox"
      version = ">= 0.50.0"
    }
  }
}
provider "proxmox" {
  endpoint = var.proxmox_endpoint
  api_token_id = var.proxmox_api_token_id
  api_token_secret = var.proxmox_api_token_secret
  insecure = true # false if SSL is configured
}