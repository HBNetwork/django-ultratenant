# django-ultratenant


## Pitch
- Parte 1: https://www.loom.com/share/a90948958c184a0fb64868bbb0230a28
- Parte 2: https://www.loom.com/share/52fd66b6f5a047f88a9fed56c1cf70d1 


## O que é?

- biblioteca multi-tenant do Django que implementa as principais abordagens
- API simples e concisa - mínimo de configuração possivel
- transparente para a aplicação
- isolamentos suportados: multi-db, multi-schema e tenant-id
- URL suportadas: subdomínio e path
    - tenant.url.com
    - url.com/tenant/admin/
- suporte a múltiplos bancos de dados
- bem documentado


## Alternativas

- https://github.com/django-tenants/django-tenants/ - só postgres e multi-schema
- https://github.com/citusdata/django-multitenant - só postgres - usa um tal de Citus


## Projetos base

- https://github.com/henriquebastos/pds-multi-tenant/
- https://github.com/eli-junior/djangoDefault/


## MVP

- setup e pip
- suporte somente ao sqlite3
- multi-db
- tenant no path da URL
- documentação como customizar o `manage.py`
- custom [urls.py](http://urls.py/)


## API

```python
# settings.py
from ultratenants.multidb import Databases
...
MIDDLEWARE = [
    ...
    'ultratenants.path.Middleware',
]
...
DATABASES = Databases(config('DATABASE_URL', cast=dburl))
DATABASE_ROUTERS = ['ultratenants.multidb.Router']
```

- Investigar possibilidade de alterar o ROOT_URL pra não precisar mexer no urls.py

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


## Roadmap

- suporte aos dbs suportados pelo Django: [PostgreSQL](https://docs.djangoproject.com/en/4.0/ref/databases/#postgresql-notes), [MariaDB](https://docs.djangoproject.com/en/4.0/ref/databases/#mariadb-notes), [MySQL](https://docs.djangoproject.com/en/4.0/ref/databases/#mysql-notes), [Oracle](https://docs.djangoproject.com/en/4.0/ref/databases/#oracle-notes)
- multi-schema
- tenant no subdominio
    - tenant.url.com/admin
- tenant-id
- customização do django cli `manage.py`
- cookiecutter para criar um novo projeto
