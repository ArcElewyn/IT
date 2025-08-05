provider "proxmox" {
  endpoint   = "https://${var.proxmox_url}/api2/json"
  api_token  = "${var.proxmox_user}@pam!terraform=${var.proxmox_token}"
  insecure   = true

  ssh {
    agent       = false
    username    = "terraform"
    private_key = file("/home/terraform/.ssh/id_rsa")
  }
}

resource "proxmox_virtual_environment_download_file" "debian_cloud_image" {
  content_type = "iso"
  datastore_id = var.image_datastore_id
  node_name    = var.proxmox_node
  url          = var.image_url
  file_name    = var.image_file_name
}

resource "proxmox_virtual_environment_vm" "debian_vm" {
  name      = var.vm_name
  node_name = var.proxmox_node
  vm_id     = var.vm_id

  cpu {
    type    = "x86-64-v2-AES"
    cores   = var.vm_cores
    sockets = var.vm_sockets
  }

  memory {
    dedicated = var.vm_memory
  }

  network_device {
    model  = "virtio"
    bridge = var.network_bridge
  }

  disk {
    size          = var.disk_size
    datastore_id  = var.disk_datastore_id
    interface     = "virtio0"
    iothread      = var.disk_iothread
    file_id       = proxmox_virtual_environment_download_file.debian_cloud_image.id
  }

  boot_order = ["virtio0"]

  initialization {
    ip_config {
      ipv4 {
        address = "dhcp"
      }
    }
    user_account {
      username = "root"
      password = "Password"
      keys     = [var.cloudinit_sshkey]
    }
  }
  
  serial_device {
    device = "socket"
  }
}
