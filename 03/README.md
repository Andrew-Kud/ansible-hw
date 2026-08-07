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
<img width="829" height="212" alt="1-1" src="https://github.com/user-attachments/assets/72828745-4dd0-46b4-9fc8-88acbf321fda" />


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
<img width="903" height="397" alt="2-1" src="https://github.com/user-attachments/assets/9554908b-1477-4f44-bba1-5ec932bd9fa4" />


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
<img width="954" height="132" alt="6-1" src="https://github.com/user-attachments/assets/b16704ca-2e53-46d5-a37c-4c19e25a9a8b" />


---

7.
Запуск:
```
ansible-playbook -i inventory/prod.yml site.yml
```
<img width="981" height="400" alt="7-1" src="https://github.com/user-attachments/assets/2ace4216-a1c0-4519-aae5-40e34829cedf" />


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
<img width="986" height="407" alt="8-1" src="https://github.com/user-attachments/assets/546fde16-af86-493f-9a17-2687be734cd9" />


---

9.

<img width="1430" height="648" alt="9-1" src="https://github.com/user-attachments/assets/5b79da4c-ee37-4b76-aeb1-9246beba0818" />

<img width="1106" height="517" alt="9-2" src="https://github.com/user-attachments/assets/eaa2e647-3c79-46bd-b5f7-0c8afb9198f3" />


---

10.
Идемпотентность:
```
ansible-playbook -i inventory/prod.yml site.yml --diff
```

<img width="1003" height="541" alt="10-1" src="https://github.com/user-attachments/assets/72facf7d-fc5d-4e59-8632-d23337f90571" />


---

11.
Git:
```
git add .
```
```
git commit -m "complete task 03"
```
```
git tag -a 08-ansible-03-yandex -m "complete task-03"
```
```
git tag --list
```

Чекнуть содержимое тега:
```
git show 08-ansible-03-yandex
```

```
git push origin main
```
```
git push origin 08-ansible-03-yandex
```
<img width="500" height="56" alt="11-1" src="https://github.com/user-attachments/assets/de40a4cc-6786-4aa6-9939-b494211767a9" />

---
---

