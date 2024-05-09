for create a project after build the image:
 docker compose run --rm app sh -c "django-admin startproject app ."

for create an app after build the image:
 docker compose run --rm app sh -c "python manage.py startapp core"
