# Django Ultratenant

Installation info of the django-ultratenant

PyPI name: ***django-ultratenant***
<https://pypi.org/project/django-ultratenant/>

**Pythons** >=3.7

**Operating systems**: Linux, Windows, OSX, Unix

**Requirements:** dj-database-url, django*

**Installers**: pip

**Code repository**: <https://github.com/HBNetwork/django-ultratenant>

## Pitch about the main idea of the project (Portuguese)
Context of the origin of the library proposal

- [Video Part 1](https://www.loom.com/share/a90948958c184a0fb64868bbb0230a28)
- [Video Part 2:](https://www.loom.com/share/52fd66b6f5a047f88a9fed56c1cf70d1)

## What is
This library makes it possible to use tenant strategies in a django project.

In a multi-tenant architecture, multiple instances of an application share the environment. This architecture is able to work because each tenant is physically integrated but logically separate; which means that a single instance of the software will run on a server and then service multiple tenants (clients).

The dango ultratenant library that implements diferent approaches.

### Type of the Strategies (Approaches)
- multi-db
- multi-schema
- tenant-id

#### What is multi-db?
- Support multiple databases. Suported sqllite and postgresdb.

#### What is multi-schema?

#### What is tenant-id?
- Supported URL approaches: subdomain and path
    - tenant.url.com
    - url.com/tenant/admin/

## Objectives
- In a django project implemented diferent approaches based of the bussiness core

- Simple API with minimal setup

- Transparent for the application

- Supported isolations approaches (multi-db, multi-schema, tenant-id)

## How to Use

### Installation

``` bash
pip install django-ultratenant
```

### Configuration

In the **settings.py** file, install the app that corresponds to the chosen strategy:
``` bash
...
    INSTALLED_APPS=["test_project.singledb", "test_project.multidb"],
...
```

Put the information the created databases:
``` bash
...
     DATABASES={
            "default": config("DATABASE_URL", default="sqlite://:memory:", cast=dburl),
            "t1": config("DATABASE_URL", default="sqlite://:memory:", cast=dburl),
            "t2": config("DATABASE_URL", default="sqlite://:memory:", cast=dburl),
        },
...
```

### API Multi-db

``` bash
...
    # settings.py
    from ultratenant.multidb import Databases
    ...
    MIDDLEWARE = [
        ...
        'ultratenant.path.Middleware',
    ]
    ...
    DATABASES = Databases(config('DATABASE_URL', cast=dburl))
    DATABASE_ROUTERS = ['ultratenant.multidb.Router']
...
```

set the urls depending on the chosen strategies
``` bash
...
    # urls.py
    ...
    from ultimate_tenants.urls import tenants_path

    urlpatterns = tenants_path([
        path('admin/', admin.site.urls),
        path('', index, name='index'),
    ])

    # url.com/tenant/admin
...
```

## Contributors
HBNetwork

HBNetwork is a community of python programmers from Brazil established within the Dev Senior Passport.

### Rules to contribute

- Your contribution is welcome.

- Setup your development environment and select issues.

## Contributing

### Clone the code

```bash
git clone https://github.com/HBNetwork/django-ultratenant
cd django-ultratenant
git checkout main
```

Or

```bash
git clone git@github.com:HBNetwork/django-ultratenant.git
cd django-ultratenant
git checkout main
```

### Setup the project

```bash
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install ".[test]"
pre-commit install
pre-commit autoupdate
pytest
```

### Create a new branch

```bash
git fetch origin
git checkout -b task/branch-name-you-work-issue
```

### Create a pull request to the branch *main*


[![PyPI](https://img.shields.io/pypi/v/django-ultratenant.svg)](https://pypi.python.org/pypi/django-ultratenant)

[![Coverage Status](https://coveralls.io/repos/github/HBNetwork/django-ultratenant/badge.svg?branch=master)](https://coveralls.io/github/HBNetwork/django-ultratenant?branch=master)


## Alternatives

-   <https://github.com/django-tenants/django-tenants/> - only Postgres
    with multi-schema
-   <https://github.com/citusdata/django-multitenant> - only Postgres
    (with Citus extension)

## Base projects

-   <https://github.com/henriquebastos/pds-multi-tenant/>
-   <https://github.com/eli-junior/djangoDefault/>

## MVP

-   setup and pip

-   SQLite3 support

-   multi-db

-   tenant on URL path

-   documetation about how customize manage.py

### Roadmap

-   other databases supported by Django:
    [PostgreSQL](https://docs.djangoproject.com/en/4.0/ref/databases/#postgresql-notes),
    [MariaDB](https://docs.djangoproject.com/en/4.0/ref/databases/#mariadb-notes),
    [MySQL](https://docs.djangoproject.com/en/4.0/ref/databases/#mysql-notes),
    [Oracle](https://docs.djangoproject.com/en/4.0/ref/databases/#oracle-notes)

-   multi-schema

-   tenant-id

-   custom [manage.py]{.title-ref} to access different tenants

-   cookiecutter to create a new project

### [Unreleased]


### [0.0.1] - 2022-07-31

#### Added
- First release on PyPI.
