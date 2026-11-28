terraform {
  required_providers {
    cloudflare = {
      source  = "cloudflare/cloudflare"
      version = "~> 5"
    }

    vultr = {
      source  = "vultr/vultr"
      version = "2.33.2"
    }

    github = {
      source  = "integrations/github"
      version = "~> 6.0"
    }

    tls = {
      source  = "opentofu/tls"
      version = "4.4.2"
    }
  }

  backend "s3" {
    bucket = "opentofu-state-shared"
    key    = "hdbee-price/terraform.tfstate"
    region = "auto"

    use_lockfile                = true
    skip_credentials_validation = true
    skip_metadata_api_check     = true
    skip_region_validation      = true
    skip_requesting_account_id  = true
    skip_s3_checksum            = true
    use_path_style              = true
  }
}

provider "github" {
  owner = var.github_owner
}

resource "tls_private_key" "deploy_key" {
  algorithm = var.private_key_algorithm
}

resource "tls_private_key" "flyio_key" {
  algorithm = var.private_key_algorithm
}

locals {
  app_ports = [
    { port = "22", protocol = "tcp" },
    { port = "80", protocol = "tcp" },
    { port = "443", protocol = "tcp" },
  ]
}

resource "vultr_firewall_group" "webapp" {
  description = "IAC: ${var.project_name_human}"
}

resource "vultr_firewall_rule" "webapp_v4" {
  for_each          = { for item in local.app_ports : "${item.port}-${item.protocol}" => item }
  firewall_group_id = vultr_firewall_group.webapp.id
  protocol          = each.value.protocol
  ip_type           = "v4"
  subnet            = "0.0.0.0"
  subnet_size       = 0
  port              = each.value.port
}


resource "vultr_firewall_rule" "webapp_v6" {
  for_each          = { for item in local.app_ports : "${item.port}-${item.protocol}" => item }
  firewall_group_id = vultr_firewall_group.webapp.id
  protocol          = each.value.protocol
  ip_type           = "v6"
  subnet            = "::"
  subnet_size       = 0
  port              = each.value.port
}

data "vultr_os" "selected_os" {
  filter {
    name   = "name"
    values = [var.vultr_instance_os_name]
  }
}

resource "vultr_instance" "sole_host" {
  region            = var.vultr_instance_region
  plan              = var.vultr_instance_plan
  os_id             = data.vultr_os.selected_os.id
  enable_ipv6       = true
  firewall_group_id = vultr_firewall_group.webapp.id
  ssh_key_ids       = [var.vultr_personal_ssh_key_uuid]

  user_data = templatefile("${path.module}/cloud-init.yml", {
    owner_ssh_public_key  = var.personal_ssh_public_key
    deploy_ssh_public_key = tls_private_key.deploy_key.public_key_openssh
    flyio_ssh_public_key  = tls_private_key.flyio_key.public_key_openssh
    github_owner          = var.github_owner
    github_repo           = var.github_repo
    repo_branch           = var.repo_branch
    repo_compose_dir      = var.repo_compose_dir
    repo_compose_path     = var.repo_compose_path
  })

  lifecycle {
    prevent_destroy = true
  }
}

data "cloudflare_zone" "selected" {
  zone_id = var.cloudflare_zone_id
}

locals {
  zone_domain            = data.cloudflare_zone.selected.name
  internal_fqdn          = sensitive("${trimsuffix(var.internal_subdomain, ".${local.zone_domain}")}.${local.zone_domain}")
  wildcard_internal_fqdn = sensitive("*.${local.internal_fqdn}")
}

resource "cloudflare_dns_record" "internal_subdomain_A" {
  zone_id = var.cloudflare_zone_id
  name    = local.internal_fqdn
  content = vultr_instance.sole_host.main_ip
  type    = "A"
  ttl     = 1
  proxied = false
  comment = "IAC: ${var.project_name_human}"
}

resource "cloudflare_dns_record" "internal_subdomain_AAAA" {
  zone_id = var.cloudflare_zone_id
  name    = local.internal_fqdn
  content = vultr_instance.sole_host.v6_main_ip
  type    = "AAAA"
  ttl     = 1
  proxied = false
  comment = "IAC: ${var.project_name_human}"
}

resource "cloudflare_dns_record" "wildcard_internal_subdomain_A" {
  count   = var.wildcard_internal_subdomain ? 1 : 0
  zone_id = var.cloudflare_zone_id
  name    = local.wildcard_internal_fqdn
  content = vultr_instance.sole_host.main_ip
  type    = "A"
  ttl     = 1
  proxied = false
  comment = "IAC: ${var.project_name_human}"
}


resource "cloudflare_dns_record" "wildcard_internal_subdomain_AAAA" {
  count   = var.wildcard_internal_subdomain ? 1 : 0
  zone_id = var.cloudflare_zone_id
  name    = local.wildcard_internal_fqdn
  content = vultr_instance.sole_host.v6_main_ip
  type    = "AAAA"
  ttl     = 1
  proxied = false
  comment = "IAC: ${var.project_name_human}"
}

resource "github_actions_secret" "vps_host" {
  repository  = var.github_repo
  secret_name = "VPS_HOST"
  value       = cloudflare_dns_record.internal_subdomain_A.name
}

resource "github_actions_secret" "vps_user" {
  repository  = var.github_repo
  secret_name = "VPS_USER"
  value       = "deploy"
}

resource "github_actions_secret" "vps_ssh_key" {
  repository  = var.github_repo
  secret_name = "VPS_SSH_KEY"
  value       = tls_private_key.deploy_key.private_key_openssh
}