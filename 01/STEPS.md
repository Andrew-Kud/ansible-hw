1.
```
ansible-playbook -i inventory/test.yml site.yml
```
<img width="2209" height="558" alt="1" src="https://github.com/user-attachments/assets/2bd7de68-1591-4583-8292-3557d69be78f" />



2.
```
ansible-playbook -i inventory/test.yml site.yml
```
<img width="2208" height="608" alt="2" src="https://github.com/user-attachments/assets/2313d236-aae2-4141-aa84-474b5831a876" />



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
<img width="2207" height="798" alt="3" src="https://github.com/user-attachments/assets/400e918e-451b-4b0b-a3ae-62b2019c02dc" />
<img width="2212" height="807" alt="4" src="https://github.com/user-attachments/assets/5202b8d5-3ee6-44ce-8892-3a8755ae00b7" />


5-6.
<img width="2202" height="798" alt="5" src="https://github.com/user-attachments/assets/f3b9eedd-6fe8-49c2-afe4-545272fd4d87" />




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
<img width="2560" height="1437" alt="10" src="https://github.com/user-attachments/assets/5cecc06c-b1e8-44cb-9b81-b01807185580" />

