Ansible Role: LightHouse
========================

Роль устанавливает и настраивает LightHouse на Linux-системах:
устанавливает Nginx, создаёт каталог веб-приложения, скачивает статическую
страницу LightHouse, разворачивает конфигурацию Nginx, включает и запускает сервис.

Requirements
------------

- Ansible >= 2.14
- Целевая ОС: deb-like.
- Доступ в интернет к `raw.githubusercontent.com`
- Права sudo/become на управляемом узле.

Role Variables
--------------

| Variable | Default |
|---|---|
| `lighthouse_name` | `lighthouse` |
| `lighthouse_root` | `/var/www/lighthouse` |
| `lighthouse_index_url` | `https://raw.githubusercontent.com/VKCOM/lighthouse/master/index.html` |
| `lighthouse_index_path` | `"{{ lighthouse_root }}/index.html"` |
| `lighthouse_nginx_config_path` | `/etc/nginx/sites-available/default` |
| `lighthouse_listen_port` | `80` |
| `lighthouse_nginx_service_name` | `nginx` |

Example Playbook
----------------

```yaml
- name: Install LightHouse
  hosts: lighthouse
  become: true
  roles:
    - role: lighthouse
```

Tags
----

- `lighthouse_install`
- `lighthouse_config`
- `lighthouse_service`
- `lighthouse_nginx`

License
-------

MIT

Author Information
------------------

Andrey Kudryashov