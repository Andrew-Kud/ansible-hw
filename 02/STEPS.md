### README:

Playbook устанавливает и настраивает ClickHouse и Vector.
Vector скачивается в виде архива, распаковывается в `/opt`, запускается как systemd-сервис и читает системные журналы Ubuntu.

## Требования:
- Ansible и ansible-lint на control node
- Ubuntu 24.04 на managed node
- Доступ по SSH
- Исходящий доступ VM в интернет

---
---

1.
```
sudo apt update
```
```
sudo apt install -y pipx python3-venv
```
```
pipx ensurepath
```
```
exec "$SHELL" -l
```
```
pipx install --include-deps ansible
```
```
ansible --version
```
```
sudo apt install ansible-lint
```

обновление:
```
pipx upgrade --include-injected ansible
```

удаление:
```
pipx uninstall ansible
```

---

2.
Проверка к управлению:
```
ansible all -i inventory/prod.yml -m ansible.builtin.ping -k
```
<img width="1395" height="194" alt="2-1" src="https://github.com/user-attachments/assets/e79914ee-2ac2-4a7b-bfec-dfd802ff6beb" />


---

3.
Создать `playbook/group_vars/vector/vars.ym`.
версию фиксировать, не `latest`.
- Vector рекомендует отдельный каталог данных.

---

4.
Сздать шаблон `playbook/templates/vector.yaml.j2`
- статичный шаблон, деплоится модулем `ansible.builtin.template`, а не `copy`.

---

5.
Создать `playbook/templates/vector.service.j2`
- Unit-файл systemd.

---

6.
Добавить `play` в `playbook/site.yml` для `vector`

---

7.
Проверить синтаксис:
```
ansible-playbook -i inventory/prod.yml site.yml --syntax-check
```
```
ansible-lint site.yml
```

---

8.
на чистой VM --check может не пройти распаковку, потому что get_url в check mode делает HEAD-проверку URL, но не скачивает архив. По этому сначала сделай реальный запуск, только потом chech.

Запуск:
```
ansible-playbook -i inventory/prod.yml site.yml \
  --tags vector \
  --diff \
  --ask-pass \
  --ask-become-pass
```
<img width="929" height="381" alt="8-1" src="https://github.com/user-attachments/assets/8e85ad68-e399-45cb-afb2-5a8ed9c63c37" />


Проверка diff:
```
ansible-playbook -i inventory/prod.yml site.yml \
  --tags vector \
  --check \
  --diff \
  --ask-pass \
  --ask-become-pass
```
<img width="956" height="380" alt="8-2" src="https://github.com/user-attachments/assets/2a3421a4-e395-4155-960e-0d381534c1ea" />


Проверка работы сервиса:
```
ansible vector -i inventory/prod.yml -b \
  -m ansible.builtin.command \
  -a "systemctl is-active vector" \
  --ask-pass
  --ask-become-pass
```
<img width="611" height="107" alt="8-3" src="https://github.com/user-attachments/assets/ae3f633d-9f31-40c0-bda4-f21b38e6a7a0" />


Проверка на идемпотентность:
```
ansible-playbook -i inventory/prod.yml site.yml \
  --tags vector \
  --diff \
  --ask-pass \
  --ask-become-pass
```
<img width="947" height="379" alt="8-4" src="https://github.com/user-attachments/assets/5eb7ef44-98b4-4d23-a5f2-e14ce7aef437" />


---

9.
```
git add .
```
```
git commit -m "complete tesk 02"
```
```
git tag -a 08-ansible-02-playbook -m "Ansible homework 02"
```
```
git push origin main
```
```
git push origin 08-ansible-02-playbook
```
```
git show --stat 08-ansible-02-playbook
```

---
---
