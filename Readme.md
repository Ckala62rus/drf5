# Django REST

####

### Create new secret key

#### importing the function from utils
* from django.core.management.utils import get_random_secret_key
#### generating and printing the SECRET_KEY
* print(get_random_secret_key())

### Install
1. install virtual env python -m venv project_name
2. install django => pip install django==4.2.7
3. in to container django => docker exec -ti django_shop /bin/bash
4. django admin django-admin
5. create new project => django-admin startproject project_name
6. run web server => python manage.py runserver 0.0.0.0:8000
7. create migration => python manage.py makemigrations
8. run migrations => python manage.py migrate
9. create Swagger docs => python.exe .\manage.py spectacular --color --file schema.yml


#### Linux
1. add user => adduser call_helper
2. install if not exist => apt install sudo
3. add permissions => usermod -aG sudo call_helper
4. switch on user call_helper => su call_helper
5. go to user directory => cd /home/call_helper
6. install certbot => sudo api install certbot python3-certbot-nginx
7. sudo certbot --nginx

#### Make and Load fixtures
1. make from concrete application => python .\manage.py dumpdata blog.categories > categories.json
2. 