После подготовки окружения и
```
cd /home/adm1/Рабочий\ стол/HW/ansible-hw/06/ansible/
```
```
/usr/local/bin/python3.14 -m venv .venv
```
```
source .venv/bin/activate
```
```
python -m pip install ansible
```
```
. venv/bin/activate && . hacking/env-setup
```

А ещё данный Ansible требует 3.13 > версию Python, но в Linux Mint apt его нет, по этому нужно собрать бинарь рядом и хитро передать его в `venv`:

1.
```
sudo apt update
```

2.
```
sudo apt install -y \
  build-essential \
  wget curl ca-certificates \
  zlib1g-dev \
  libncursesw5-dev \
  libgdbm-dev \
  libnss3-dev \
  libssl-dev \
  libreadline-dev \
  libffi-dev \
  libsqlite3-dev \
  libbz2-dev \
  liblzma-dev \
  tk-dev \
  uuid-dev
```

3.
```
cd /tmp
```
```
wget https://www.python.org/ftp/python/3.14.7/Python-3.14.7.tgz
```
```
tar -xzf Python-3.14.7.tgz
```
```
cd Python-3.14.7
```
```
./configure \
  --prefix=/usr/local \
  --enable-optimizations \
  --with-ensurepip=install
```
```
make -j"$(nproc)"
```
```
sudo make altinstall
```
- altinstall использую для того, что бы можно было версионировать бинарь, а не заменять системный и не ломать PPA или APT.
`он будет находиться в /usr/local/bin/python3.14`

4.
```
python3.14 --version
```

5.
```
cd /home/adm1/Рабочий\ стол/HW/ansible-hw/06/ansible/
```
```
/usr/local/bin/python3.14 -m venv .venv
```
```
source .venv/bin/activate
```
```
python --version
```
```
python -m pip install --upgrade pip
```
```
python -m pip install ansible
```
```
pip install -r requirements.txt
```


---
### Шаг 4:

```
chmod +x my_own_module.py
```

Два раза:
```
echo '{"ANSIBLE_MODULE_ARGS":{"path":"/tmp/test.txt","content":"Hello, Netology!"}}' | python my_own_module.py
```
```
cat /tmp/test.txt
```
<img width="1541" height="166" alt="4" src="https://github.com/user-attachments/assets/0e741099-e986-4b19-a15c-decaf8b75d92" />


---
### Шаг 5:

```
mkdir -p library
```
```
cp my_own_module.py library/
```

```
ansible-playbook -i 'localhost,' --syntax-check playbook.yml
```
или через переменную окружения, если модуль в нестандартном месте лежит:
```
ANSIBLE_LIBRARY=./library ansible-playbook -i 'localhost,' --syntax-check playbook.yml
```


---
### Шаг 6:

```
ansible-playbook -i 'localhost,' playbook.yml
```
или через переменную окружения, если модуль в нестандартном месте лежит:
```
ANSIBLE_LIBRARY=./library ansible-playbook playbook.yml
```

```
cat /tmp/example.txt
```
<img width="1081" height="474" alt="6" src="https://github.com/user-attachments/assets/58a5a3a1-b638-4908-9bb0-b2815f8ecd46" />



---
### Шаг 7-12

7.
```
deactivate
```

8.
```
ansible-galaxy collection init my_own_namespace.yandex_cloud_elk
```

9.
```
mkdir -p ./my_own_namespace/yandex_cloud_elk/plugins/modules
```
```
cp ./my_own_module.py ./my_own_namespace/yandex_cloud_elk/plugins/modules/
```
или лучше, если копия в `library` не нужна:
```
mv ./library/my_own_module.py ./my_own_namespace/yandex_cloud_elk/plugins/modules/
```

10.
```
mkdir -p ./my_own_namespace/yandex_cloud_elk/roles/create_text_file/{defaults,tasks}
```
```
nano ./my_own_namespace/yandex_cloud_elk/roles/create_text_file/defaults/main.yml
```
```
nano ./my_own_namespace/yandex_cloud_elk/roles/create_text_file/tasks/main.yml
```

Так просто это не заработало, Ansible ожидает ansible_collection, а значит:
```
mkdir -p collections/ansible_collections/my_own_namespace
```
```
mv ./my_own_namespace/yandex_cloud_elk ./collections/ansible_collections/my_own_namespace/
```
```
rmdir my_own_namespace
```

Так же нужно переназначить путь до коллеций:
```
nano ansible.cfg
```
- тут до меня дошло, что через этот же `ansible.cfg` можно было оставить дефолтный `./my_own_namespace`как путь по умолчанию.

11.
```
ansible-playbook -i 'localhost,' playbook.yml
```
```
cat /tmp/example.txt
```
<img width="1418" height="1351" alt="11" src="https://github.com/user-attachments/assets/5282e09e-ca37-4ee6-88a8-351dc07c5c9c" />


12.
```
rm -rf 06/ansible/.git
```
```
git commit -m "homework-ansible 6-12"
```
```
git push -u origin main
```
```
git tag -a 1.0.0 -m "homework-ansible 6-12"
```
```
git push origin 1.0.0
```
```
git tag --list
```
```
git show 1.0.0
```

Так, столкнулся с ошибко 160000 - из за `Ansible` репозитория.
Проблема скорее всего в разныз владельцах и правах. Если так, то в Гит отправится Симлинк, а не репозиторий.

```
cd /home/adm1/Рабочий\ стол/HW/ansible-hw/
```
```
rm -rf 06/ansible/.git
```

если закомитил но не отправил:
```
git reset --mixed HEAD~1
```
```
git rm --cached -f 06/ansible
```

если уже отправил:
```
git rm --cached -f 06/ansible
```

```
ls -ld .git .git/objects
```
```
ls -la .git/objects | head
```
```
sudo chown -R "$(id -un)":"$(id -gn)" .git
```
```
git add 06
```
```
git commit -m ....
```
```
git push ...
```


---
### Шаг 13-14:

13.
```
cd collections/ansible_collections/my_own_namespace/yandex_cloud_elk
```
```
ansible-galaxy collection build
```
```
ls
```
<img width="1804" height="144" alt="13" src="https://github.com/user-attachments/assets/041f3812-44d3-417d-bda7-aa808336a764" />


14.
```
cd /home/adm1/Рабочий\ стол/HW/ansible-hw/06/ansible/
```
```
mkdir ./test_collection
```
```
cp ./playbook.yml ./test_collection/
```
```
mv ./collections/ansible_collections/my_own_namespace/yandex_cloud_elk/my_own_namespace-yandex_cloud_elk-1.0.0.tar.gz ./test_collection/
```


---
### Шаг 15-16:

15.
```
cd ./test_collection
```
```
ansible-galaxy collection install my_own_namespace-yandex_cloud_elk-1.0.0.tar.gz
```
```
ansible-galaxy collection list | grep yandex_cloud_elk
```
<img width="1255" height="214" alt="15" src="https://github.com/user-attachments/assets/5c4fbe0d-ef28-4bc5-b2ab-a64383f44b5e" />


16.
```
cd ./test_collection
```
```
rm /tmp/example.txt
```
```
ansible-playbook -i 'localhost,' playbook.yml
```
```
cat /tmp/example.txt
```
<img width="1069" height="495" alt="16" src="https://github.com/user-attachments/assets/273b21ef-4e71-4ac0-a7d7-82c61ada10c7" />
