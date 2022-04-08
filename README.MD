# Website

## Deployment

* Prerequisites
    * Machine with docker installed

1. Clone repo to local machine and choose how to run the app from the three options below

This project can run in three separate ways to increase development speed.  See below the environment files and commands needed to get them up and running.

---
### **1. Local - No Docker**

Runs without container using Sqlite database

 create an ```.env``` file containing
```
DEBUG=TRUE
SECRET_KEY=secret-key-here
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
SUPERUSER_USERNAME=admin-username-here
SUPERUSER_PASSWORD=admin-pass-here
SUPERUSER_EMAIL=admin-email-here
```

First time setup
```
python manage.py makemigrations --no-input
python manage.py migrate --no-input
python manage.py ensure_initial_users
python manage.py loaddata brands.json
python manage.py loaddata shops.json
python manage.py loaddata categories.json
python manage.py loaddata productssample.json
```

To run ``` python manage.py runserver ```

---
### **2. Development - Dockerized**

Runs in container with Postgresql database

create an ```.env.dev``` file containing
```
DEBUG=TRUE
SECRET_KEY=secret-key-here
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
SQL_ENGINE=django.db.backends.postgresql
SQL_USER=postgres-db-name
SQL_DATABASE=postgres
SQL_PASSWORD=postgres-pass
SQL_HOST=db
SQL_PORT=5432
DATABASE=postgres
SUPERUSER_USERNAME=admin-username-here
SUPERUSER_PASSWORD=admin-pass-here
SUPERUSER_EMAIL=admin-email-here
POSTGRES_USER=postgres-db-name
POSTGRES_PASSWORD=postgres-pass
POSTGRES_DB=postgres
```

To run 
``` 
docker-compose build
docker-compose up
```
---
### **3. Production - Dockerized**

Runs in container with Postgresql database

create an ```.env.prod``` file containing
```
DEBUG=FALSE
SECRET_KEY=secret-key-here
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
SQL_ENGINE=django.db.backends.postgresql
SQL_USER=postgres-db-name
SQL_DATABASE=postgres
SQL_PASSWORD=postgres-pass
SQL_HOST=db
SQL_PORT=5432
DATABASE=postgres
SUPERUSER_USERNAME=admin-username-here
SUPERUSER_PASSWORD=admin-pass-here
SUPERUSER_EMAIL=admin-email-here
```

create an ```.env.prod.db``` file containing
```
POSTGRES_USER=postgres-db-name
POSTGRES_PASSWORD=postgres-pass
POSTGRES_DB=postgres
```

Build and run detached
```
docker-compose -f docker-compose.prod.yml up -d --build
```

Logs
```
docker-compose -f docker-compose.prod.yml logs -f
```