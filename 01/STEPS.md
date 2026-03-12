1.
```
ansible-playbook -i inventory/test.yml site.yml
```



2.
```
ansible-playbook -i inventory/test.yml site.yml
```


3-4.
```
docker run -d --name ubuntu ubuntu:24.04 sleep infinity
```
```
docker exec -it ubuntu apt update
docker exec -it ubuntu apt install -y python3
```
```
docker run -d --name centos7 rockylinux:8 sleep infinity
```
```
docker exec -it centos7 dnf install -y python39
```
```
docker ps
```
```
ansible-playbook -i inventory/prod.yml site.yml
```


5-6.




7-8.
```
ansible-vault encrypt ./group_vars/deb/examp.yml
```
```
ansible-vault encrypt ./group_vars/el/examp.yml
```
```
ansible-playbook -i inventory/prod.yml site.yml --ask-vault-pass
```



9.
```
ansible-doc -t connection -l
```
ansible.builtin.local



10-11.
```
ansible-playbook -i inventory/prod.yml site.yml --ask-vault-pass
```