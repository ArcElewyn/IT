# Prometheus Ansible Role

## Project Overview

This project provides an **Ansible role** to install and configure **Prometheus** as an agent on your servers. It automates the setup, download, and configuration of Prometheus, making it easy to deploy across multiple hosts.

The role installs Prometheus, sets up its service, and configures it to scrape metrics from the local machine. It also handles the configuration of the Prometheus service through **systemd** and provides a custom configuration file for Prometheus.

## Project Structure

```
C:.
│   README.md
├── inventories/hosts.ini
├── playbooks/
│       install-prometheus.yml
└── roles/
    └── prometheus/
        ├── files/
        │       prometheus-agent.service
        ├── tasks/
        │       main.yml
        ├── templates/
        │       prometheus.yml.j2
        └── vars/
                main.yml
```

### Description of Each File

- **README.md**  
  This file (the one you're reading). It explains the purpose of the project, its structure, and how to use it.

- **inventories/hosts.ini**  
  Contains the list of target hosts for installing Prometheus. You can define groups and specific host variables here.

- **playbooks/install-prometheus.yml**  
  The main Ansible playbook that calls the Prometheus role on hosts defined in the `[prometheus]` group of your inventory.

- **roles/prometheus/files/prometheus-agent.service**  
  The systemd service file for Prometheus. It is copied to `/etc/systemd/system/prometheus.service` on the target host.

- **roles/prometheus/tasks/main.yml**  
  The core tasks that download Prometheus from GitHub, extract it, place the binaries in the correct location, and set up the directories and config files.

- **roles/prometheus/templates/prometheus.yml.j2**  
  A Jinja2 template for the Prometheus configuration file (`prometheus.yml`). By default, it scrapes metrics from `localhost:9090`.

- **roles/prometheus/vars/main.yml**  
  Defines variables such as the Prometheus version, the download URL, and file paths used in the tasks.

## Usage

1. **Configure Inventory**  
   Edit `inventories/hosts.ini` and add your target servers under the `[prometheus]` group.

2. **Run the Playbook**  
   From your Ansible control node, run:
   ```bash
   ansible-playbook -i inventories/hosts.ini playbooks/install-prometheus.yml
   ```

3. **Verify**  
   Once complete, Prometheus should be running as a systemd service on your target machine(s). Access it (by default) at `http://<your_host>:9090`.
