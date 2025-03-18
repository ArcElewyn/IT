terraform {
  required_providers {
    proxmox = {
      source  = "bpg/proxmox"
      version = ">= 0.50.0"
    }
  }
}

provider "proxmox" {
  endpoint  = var.proxmox_endpoint
  api_token = var.proxmox_api_token
  insecure  = true 
}

data "local_file" "ssh_public_key" {
  filename = var.ssh_public_key_file
}

resource "proxmox_virtual_environment_vm" "debian_vm" {
  name      = var.vm_name
  node_name = var.proxmox_node

  memory {
      dedicated = var.vm_memory
    }

  cpu {
    cores   = var.vm_cores
    sockets = var.vm_sockets
  }

  initialization {
    ip_config {
      ipv4 {
        address = var.vm_ipv4_address
        gateway = var.vm_gateway
      }
    }

    user_account {
      username = var.
      password = var.vm_password
      keys     = [trimspace(data.local_file.ssh_public_key.content)]
    }
  }

  disk {
    datastore_id = var.datastore_id
    file_id      = proxmox_virtual_environment_download_file.debian_cloud_image.id
    interface    = var.disk_interface
    iothread     = var.disk_iothread
    discard      = var.disk_discard
    size         = var.disk_size
  }

  network_device {
    bridge = var.network_bridge
  }
}

resource "proxmox_virtual_environment_download_file" "debian_cloud_image" {
  content_type = "iso"
  datastore_id = var.download_datastore_id
  node_name    = var.proxmox_node
  url          = var.cloud_image_url
}
