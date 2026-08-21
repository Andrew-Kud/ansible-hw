# Ansible Collection - my_own_namespace.yandex_cloud_elk

Documentation for the collection.

# my_own_namespace.yandex_cloud_elk

Ansible collection containing a custom module and role for creating text files.

## Requirements

- Ansible Core 2.16 or later
- Python 3.13 or later on managed hosts

## Included content

### Module

- `my_own_namespace.yandex_cloud_elk.my_own_module` — creates or updates a text file with the specified content.

Module parameters:

| Parameter | Type | Required | Description |
|---|---|---:|---|
| `path` | `path` | Yes | Path to the target text file |
| `content` | `str` | Yes | Text content to write to the file |

### Role

- `my_own_namespace.yandex_cloud_elk.create_text_file` — creates a text file using the custom module.

## Usage

Example playbook:

```yaml
***
- name: Create a text file
  hosts: localhost
  connection: local
  gather_facts: false

  roles:
    - role: my_own_namespace.yandex_cloud_elk.create_text_file
```

## Role variables

| Variable | Default value | Description |
|---|---|---|
| `my_own_module_path` | `/tmp/example.txt` | Path to the created file |
| `my_own_module_content` | `Hello, Netology!` | Content of the created file |

Override role defaults:

```yaml
***
- name: Create a custom text file
  hosts: localhost
  connection: local
  gather_facts: false

  roles:
    - role: my_own_namespace.yandex_cloud_elk.create_text_file
      vars:
        my_own_module_path: /tmp/custom.txt
        my_own_module_content: Custom file content
```

## License

MIT