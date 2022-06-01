# E-commerce Website

A website with multiple shops (Plumbing, Heating, Bathrooms).  Contained in docker, deployed with Github Actions, this Django app uses a Postgres database with full text search to retrieve search queries.

[Website Link](http://167.99.219.161:8000/)

Items currently only in "Bathroom" shop

---
## Features

- Postgres database with
    - Full text search
    - Partial word match
    - Search weighting
    - Search ranking

- Filters
    - Search by shop
    - Search by category
    - Search by name
    - Or any combination of the above

- Categories are searchable and automatically generated on the website via the database

- Search Example
    - Item = **"Slate Anthracite 1200x900mm LH Offset Quadrant Shower Tray & Waste"**
        - Searches that will include this item in results
            - Slate Anthracite 1200x900 lh quadrant shower tray
            - Slate Anthracite 1200 900 lh quad tray
            - slat anth 1200 900 lh qua tr
    - NOTE: This item will be ranked very high, with items not including some of the search terms appearing much lower down in the results.
---
## To-Do

- Automated testing
- Add items in heating and plumbing shops
- Format account pages & rig up emails to confirm accounts
- Create a quote app (shopping basket) for products
- Update placeholder images with final content on carousel
- Back buttons for pages
- Buttons to remove shop-filter / category / query

---
## Technologies

- [Postgres](https://www.postgresql.org/)
- [Django](https://www.djangoproject.com/)
- [Bootstrap4](https://getbootstrap.com/)
- [Docker](https://www.docker.com/)
- [Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)
- [Github Actions](https://github.com/features/actions/)
- Javascript / Python / YML

---
## Deployment

* Prerequisites
    * Machine with docker installed

1. Clone repo to local machine and choose how to run the app from the three options below

This project can run in three separate ways to increase development speed.  See below the environment files and commands needed to get them up and running.

---
### **1. Local - No Docker**

Runs without container using postgres.  Needs postgres installed and running

Create the postgres database, from postgres cli as below
```
CREATE USER mydbuser WITH PASSWORD 'mydbpass';
CREATE DATABASE mydb;
```

 create an ```.env``` file containing
```
DEBUG=TRUE
SECRET_KEY=secret-key-here
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
SUPERUSER_USERNAME=admin-username-here
SUPERUSER_PASSWORD=admin-pass-here
SUPERUSER_EMAIL=admin-email-here
SQL_ENGINE=django.db.backends.postgresql_psycopg2
SQL_USER=mydbuser
SQL_DATABASE=mydb
SQL_PASSWORD=mydbpass
SQL_HOST=localhost
SQL_PORT=5432
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

- Start postgres ``` sudo service postgresql start ```
- To run ``` python manage.py runserver ```

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

---
## Helpers

#### Production
* Connect to docker logs ``` docker-compose -f docker-compose.prod.yml logs -f ```
* Builds / deploys detached ``` docker-compose -f docker-compose.prod.yml up -d --build ```
