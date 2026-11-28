
output "vps_ip" {
  value     = vultr_instance.sole_host.main_ip
  sensitive = true
}

output "vps_fqdn" {
  value     = cloudflare_dns_record.internal_subdomain_A.name
  sensitive = true
}

output "vps_ipv6" {
  value     = vultr_instance.sole_host.v6_main_ip
  sensitive = true
}

output "vps_id" {
  value     = vultr_instance.sole_host.id
  sensitive = true
}

output "ssh_command" {
  value     = "ssh deploy@${cloudflare_dns_record.internal_subdomain_A.name}"
  sensitive = true
}

output "app_dir" {
  value = "/opt/${var.github_repo}"
}

output "deploy_private_key" {
  value     = tls_private_key.deploy_key.private_key_openssh
  sensitive = true
}

output "deploy_public_key" {
  value = tls_private_key.deploy_key.public_key_openssh
}

output "flyio_private_key" {
  value     = tls_private_key.flyio_key.private_key_openssh
  sensitive = true
}

output "flyio_public_key" {
  value = tls_private_key.flyio_key.public_key_openssh
}