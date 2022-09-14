# Django Ultratenant

## Pitch (Portuguese)

- Part 1:
    <https://www.loom.com/share/a90948958c184a0fb64868bbb0230a28>
- Part 2:
    <https://www.loom.com/share/52fd66b6f5a047f88a9fed56c1cf70d1>

## What is

- Django multi-tenant library that implements diferent approaches

- Simple API with minimal setup

- Transparent for the application

- Supported isolations approaches:
    - multi-db
    - multi-schema
    - tenant-id

- Supported URL approaches: subdomain and path
    - tenant.url.com
    - url.com/tenant/admin/

- Support multiple databases

- Good documentation

## Contributing

### Rules to contribute

#### Clone the code

```bash
git clone https://github.com/HBN3tw0rk/django-ultratenant
cd django-ultratenant
git checkout main
```

Or

```bash
git clone git@github.com:HBN3tw0rk/django-ultratenant.git
cd django-ultratenant
git checkout main
```

#### Setup the project

```bash
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install ".[test]"
pre-commit install
pre-commit autoupdate
pytest
```

#### Create a new branch

```bash
git fetch origin
git checkout -b task/branch-name-you-work-issue
```




#### Create a pull request to the branch *main*


[![PyPI](https://img.shields.io/pypi/v/django-ultratenant.svg)](https://pypi.python.org/pypi/django-ultratenant)

[![Coverage Status](https://coveralls.io/repos/github/HBN3tw0rk/django-ultratenant/badge.svg?branch=master)](https://coveralls.io/github/HBN3tw0rk/django-ultratenant?branch=master)

[![Documentation Status](https://readthedocs.org/projects/django-ultratenant/badge/?version=latest)](https://django-ultratenant.readthedocs.io/en/latest/?version=latest)

Ultimate Django app for multi-tenant.

-   Documentation: <https://django-ultratenant.readthedocs.io>.

## Installation

``` bash
pip install django-ultratenant
```

## How to Use

-   TODO



## Alternatives

-   <https://github.com/django-tenants/django-tenants/> - only Postgres
    with multi-schema
-   <https://github.com/citusdata/django-multitenant> - only Postgres
    (with Citus extension)

# Base projects

-   <https://github.com/henriquebastos/pds-multi-tenant/>
-   <https://github.com/eli-junior/djangoDefault/>

# MVP

-   setup and pip

-   SQLite3 support

-   multi-db

-   tenant on URL path

-   documetation about how customize manage.py



# API

```python
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
```

(maybe it won\'t be necessary)

```python
# urls.py
...
from ultimate_tenants.urls import tenants_path

urlpatterns = tenants_path([
    path('admin/', admin.site.urls),
    path('', index, name='index'),
])

# url.com/tenant/admin
```

# Roadmap

-   other databases supported by Django:
    [PostgreSQL](https://docs.djangoproject.com/en/4.0/ref/databases/#postgresql-notes),
    [MariaDB](https://docs.djangoproject.com/en/4.0/ref/databases/#mariadb-notes),
    [MySQL](https://docs.djangoproject.com/en/4.0/ref/databases/#mysql-notes),
    [Oracle](https://docs.djangoproject.com/en/4.0/ref/databases/#oracle-notes)

-   multi-schema

-   tenant-id

-   custom [manage.py]{.title-ref} to access different tenants

-   cookiecutter to create a new project

## Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/pt-BR/0.3.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

### [Unreleased]

### [0.0.1] - 2022-07-31
#### Added
- First release on PyPI.
