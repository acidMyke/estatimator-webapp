variable "project_name" {
  type    = string
  default = "hdbeeprice"
}

variable "project_name_human" {
  type    = string
  default = "HDBee Price"
}

variable "github_owner" {
  type    = string
  default = "acidmyke"
}

variable "github_repo" {
  type    = string
  default = "hdbeeprice"
}

variable "repo_branch" {
  type    = string
  default = "main"
}

variable "repo_compose_dir" {
  type    = string
  default = "infra"
}

variable "repo_compose_path" {
  type    = string
  default = "compose.yml"
}

variable "private_key_algorithm" {
  type    = string
  default = "ED25519"
}

variable "personal_ssh_public_key" {
  type = string
}

# From iac-acidmyke/module/vultr

variable "vultr_personal_ssh_key_uuid" {
  type    = string
  default = "24f7b2de-1f1f-480c-ab52-547179873f4e"
}

variable "vultr_instance_plan" {
  type    = string
  default = "vc2-1c-1gb"
}

variable "vultr_instance_region" {
  type    = string
  default = "sgp"
}

variable "vultr_instance_os_name" {
  type    = string
  default = "Ubuntu 26.04 LTS x64"
}


# From iac-acidmyke/module/cloudflare

variable "cloudflare_account_id" {
  type      = string
  sensitive = true
}

variable "cloudflare_zone_id" {
  type      = string
  sensitive = true
}

variable "internal_subdomain" {
  type = string
}

variable "wildcard_internal_subdomain" {
  type    = bool
  default = true
}