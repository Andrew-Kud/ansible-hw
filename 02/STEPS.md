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

Проверка diff:
```
ansible-playbook -i inventory/prod.yml site.yml \
  --tags vector \
  --check \
  --diff \
  --ask-pass \
  --ask-become-pass
```

Проверка работы сервиса:
```
ansible vector -i inventory/prod.yml -b \
  -m ansible.builtin.command \
  -a "systemctl is-active vector" \
  --ask-pass
  --ask-become-pass
```

Проверка на идемпотентность:
```
ansible-playbook -i inventory/prod.yml site.yml \
  --tags vector \
  --diff \
  --ask-pass \
  --ask-become-pass
```

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
