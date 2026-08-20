### Подготовка окружения:

1.
```
sudo apt update && sudo apt install -y python3-venv python3-full
```
```
pipx install molecule && pipx inject molecule "molecule-plugins[docker,podman]"
```
```
sudo apt install -y docker.io && sudo apt install -y podman
```
```
docker --version
python3 --version
pipx --version
molecule --version
molecule drivers
```


2.
```
docker pull aragast/netology:latest
```


3.
```
docker run --rm -it \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v "$PWD":/workspace \
  -w /workspace \
  aragast/netology:latest \
  bash
```

---

### Задание 1:

1.
```
docker run --rm -it \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v "$PWD":/workspace \
  -w /workspace \
  aragast/netology:latest \
  bash
```
```
python3 -m pip install \
  "molecule==3.6.1" \
  "molecule-docker==1.1.0" \
  "ansible==4.10.0" \
  "docker<6" \
  "ansible-lint<6" \
  "yamllint<1" \
  "flake8<4"
```
```
python3 -m pip uninstall -y urllib3 requests
```
```
python3 -m pip install --no-cache-dir \
  "urllib3==1.26.18" \
  "requests==2.27.1" \
  "six==1.16.0"
```
```
yum install -y docker
```
```
python3 -c "import urllib3, requests, six; print('urllib3:', urllib3.__version__); print('requests:', requests.__version__); print('six:', six.__version__)"
```
```
molecule --version
```
```
molecule drivers
```
```
docker --version
```
<img width="706" height="635" alt="1" src="https://github.com/user-attachments/assets/cc635a8c-2ac2-4379-aa3e-fdf2682e6949" />


2.
```
cd /workspace/roles/clickhouse
```
```
molecule test -s ubuntu_xenial
```

`Запуск test сформировал тестовую последовательность dependency - lint - cleaup - destroy - syntax - create - prepare - converge - idempotence - side_effect - verify - cleanup - destroy. Тст остановился на стадии dependency, потому что устаревшая версия Ansible в учебном контейнере не смогла получить коллекцию community.docker через изменившийся API.`
<img width="1518" height="1120" alt="1-2" src="https://github.com/user-attachments/assets/b73bca0c-d52c-4054-a40e-24b2525803a3" />


3.
в /roles/vector/meta/main.yml нужно добавить:
```
  namespace: adm1
  role_name: vector
```
после:
`  license: license (GPL-2.0-or-later, MIT, etc)`
`  min_ansible_version: 2.1`

4.
в /roles/vector/molecule/converge.yml заменить все:
```
  roles:
    - role: adm1
```
на
```
  roles:
    - role: adm1.vector
```


5.
в /roles/vector/molecule/molecule.yml закоментировать:
```
lint: |
  yamllint .
  ansible-lint
```


6.
В /roles/vector/handlers/main.yml заменить название сервиса `ansible.builtin.systemd_service:` на этот:
```
- name: Reload systemd daemon
  ansible.builtin.systemd:
    daemon_reload: true
```


7.
Вернуться в докер:
```
cd /workspace/roles/vector
```
```
molecule test -s default
```

`molecule test -s default успешно прошёл этапы dependency, lint, destroy, syntax и create. Бли собраны и запущены тестовые образы oracle linux:8 и ubuntu:latest. На этапе converge тест остановился при сборе фактов для ubuntu иззв устаревшего контейнера aragast/netology:latest: внутри него /usr/bin/docker является podman-обёрткой, а запуск вложенного Podmn в контейнере запрещён. Поэтому ansible не может подключиться к molecule-инстансу. Ошибка относится к тестовому окружению, а не к роли vector.`

<img width="1030" height="1219" alt="1-7-1" src="https://github.com/user-attachments/assets/fb4e4ec3-9a2f-46f9-ab58-ce4da23ad9b6" />

<img width="998" height="1229" alt="1-7-2" src="https://github.com/user-attachments/assets/cfe3ed8d-ddc8-420e-af3a-5a9644eca35d" />

<img width="1071" height="727" alt="1-7-3" src="https://github.com/user-attachments/assets/e425ceeb-55d9-432b-a9fd-bd75f673d576" />

