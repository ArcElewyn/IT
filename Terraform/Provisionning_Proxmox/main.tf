resource "proxmox_vm_qemu" "debian_vm" {
  name = "var.vm_name"
  target_node = "var.node_name"
  clone = "var.template_name" #

  cpu = "var.cpumode"
  sockets = 1
  cores = 2
  memory = 2048
  balloon = 1024
  disk {
    size = "20G"
    type = "virtio"
    storage = var.storage_name 
    }

  network {
    model = "virtio"
    bridge = "var.bridge_name" 
  }

  os_type = "cloud-init"
  ciuser = "var.username"
  cipassword = "var.password"
}