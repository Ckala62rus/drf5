# Django REST

#### install
1. install virtual env python -m venv project_name
2. install django => pip install django==4.2.7
3. in to container django => docker exec -ti django_shop /bin/bash
4. django admin django-admin
5. create new project => django-admin startproject project_name
6. run web server => python manage.py runserver 0.0.0.0:8000
7. create migration => python manage.py makemigrations
8. run migrations => python manage.py migrate
9. create Swagger docs => python.exe .\manage.py spectacular --color --file schema.yml
10. 