# Django Ultratenant


[![PyPI](https://img.shields.io/pypi/v/django-ultratenant.svg)](https://pypi.python.org/pypi/django-ultratenant)

[![Coverage Status](https://coveralls.io/repos/github/HBN3tw0rk/django-ultratenant/badge.svg?branch=master)](https://coveralls.io/github/HBN3tw0rk/django-ultratenant?branch=master)

[![Documentation Status](https://readthedocs.org/projects/django-ultratenant/badge/?version=latest)](https://django-ultratenant.readthedocs.io/en/latest/?version=latest)

Ultimate Django app for multi-tenant.

-   Documentation: <https://django-ultratenant.readthedocs.io>.

# Installation

``` bash
pip install django-ultratenant
```

# How to Use

-   TODO

# Pitch (Portuguese)

-   Part 1:
    <https://www.loom.com/share/a90948958c184a0fb64868bbb0230a28>
-   Part 2:
    <https://www.loom.com/share/52fd66b6f5a047f88a9fed56c1cf70d1>

# What is

-   Django multi-tenant library that implements diferent approachs

-   simple API with minimal setup

-   transparent for the application

-   suported isolations approachs: multi-db, multi-schema and tenant-id

- supported URL approachs: subdomain and path
    * tenant.url.com
    * url.com/tenant/admin/

-   support to multiple database suporte

-   good documentation

# Alternatives

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
