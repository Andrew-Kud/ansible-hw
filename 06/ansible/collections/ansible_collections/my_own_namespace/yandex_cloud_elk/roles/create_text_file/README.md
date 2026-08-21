# create_text_file

The `create_text_file` role creates or updates a text file using the
`my_own_namespace.yandex_cloud_elk.my_own_module` module.

## Requirements

- The `my_own_namespace.yandex_cloud_elk` collection must be available.
- Python 3.13 must be available on the managed host.

## Role variables

| Variable | Default value | Description |
|---|---|---|
| `my_own_module_path` | `/tmp/example.txt` | Path to the target text file |
| `my_own_module_content` | `Hello, Netology!` | Content to write into the file |

## Example playbook

```yaml
***
- name: Use the create_text_file role
  hosts: localhost
  connection: local
  gather_facts: false

  roles:
    - role: my_own_namespace.yandex_cloud_elk.create_text_file
      vars:
        my_own_module_path: /tmp/example.txt
        my_own_module_content: Hello, Netology!
```

## License

MIT