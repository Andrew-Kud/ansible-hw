1.
Подготовка 3 ВМ в Yandex cloud:
```
for i in {0..2}; do
  yc compute instance create \
    --name vm-$i \
    --zone ru-central1-b \
    --platform standard-v3 \
    --network-interface subnet-name=def_homework,nat-ip-version=ipv4 \
    --preemptible \
    --create-boot-disk image-folder-id=standard-images,image-family=ubuntu-2404-lts-oslogin,type=network-hdd,size=10GB \
    --cores=2 --memory=4GB --core-fraction=20 \
    --ssh-key ~/.ssh/id_rsa.pub \
    --async
done
```

---

2.
За основу возьму то, что было в ansible-02.
Добавил в `prod.yml` ключ и новые ip, проверил:

Доступность ключа:
```
ssh -i ~/.ssh/id_rsa yc-user@158.160.26.221
```

Доступность ВМ:
```
ansible all -i inventory/prod.yml -m ansible.builtin.ping
```


---

3.
Создал `vars.yml` для `lighthouse` и заполнил.

---

4.
Создал шаблон для nginx в `templates/lighthouse-nginx.conf.j2`

---

5.
Добавил в конец третий play для `site.yml`
Обьединил в блоки 3 плея, что бы удобно было для `tag` и `when: not ansible_check_mode`

---

6.
Проверка синтаксиса:
```
ansible-playbook -i inventory/prod.yml site.yml --syntax-check
```

Запуск линтера:
```
ansible-lint site.yml
```

Автоисправление линтера ansible:
```
ansible-lint --fix site.yml
```
для старых версий:
```
ansible-lint --write site.yml
```

---

7.
Запуск:
```
ansible-playbook -i inventory/prod.yml site.yml
```

---

8.

dry-run запуск и проверка:
```
ansible-playbook -i inventory/prod.yml site.yml --check --diff
```

Проверка по тегу:
```
ansible-playbook -i inventory/prod.yml site.yml --check --diff --tags lighthouse_install
```

---

9.


---

10.
Идемпотентность:
```
ansible-playbook -i inventory/prod.yml site.yml --diff
```


---
