Ansible Role: Vector
=========

Роль устанавливает и настраивает Vector на Linux-системах:
создаёт системного пользователя, скачивает архив, разворачивает бинарный файл,
устанавливает systemd unit и конфигурацию, включает и запускает сервис.

Requirements
------------

- Ansible >= 2.14
- Целевая ОС: deb-like.
- Доступ в интернет к packages.timber.io
- Права sudo/become на управляемом узле.

Role Variables
--------------

| Variable | Default |
|---|---|
| `vector_version` | `0.56.0` |
| `vector_arch` | `"x86_64-unknown-linux-musl"` |
| `vector_user` | `vector` |
| `vector_group` | `vector` |

Example Playbook
----------------


```yaml
- name: Install Vector
  hosts: vector
  become: true
  roles:
    - role: vector
```

## Tags

- `vector_install`
- `vector_config`
- `vector_service`

License
-------

MIT

Author Information
------------------

Andrey Kudryashov
