
output "vm_name" {
  description = "Name of the created VM"
  value       = proxmox_vm_qemu.debian_vm.name
}

output "vm_ip" {
  value = proxmox_vm_qemu.debian_vm.default_ipv4_address
}