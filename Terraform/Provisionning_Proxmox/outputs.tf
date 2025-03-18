
output "vm_name" {
  description = "Name of the created VM"
  value       = proxmox_virtual_environment_vm.debian_vm.name
}

output "vm_ip" {
  value = proxmox_virtual_environment_vm.debian_vm.default_ipv4_address
}