from dj_database_url import parse as dburl
from django.apps import apps
from django.db import models

from ultratenant.threadlocal import TENANTLOCAL


class TenantAbstract(models.Model):
    key = models.CharField(max_length=32, unique=True, db_index=True)
    dburl = models.URLField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.key


class DatabaseMapper(dict):
    def __init__(self, default, **others):
        self.cache = {"default": dburl(default)}
        self.cache.update({k: dburl(v) for k, v in others.items()})

    def __getitem__(self, key):
        if key not in self.cache:
            self.cache[key] = dburl(self.load_dburl(key))

        return self.cache[key]

    def __contains__(self, key):
        return True

    @staticmethod
    def load_dburl(key):
        Tenant = apps.get_model("multidb", "Tenant")
        t = Tenant.objects.get(key=key)
        return t.dburl


class SQLiteMapper(dict):
    ENGINE = "django.db.backends.sqlite3"

    def __init__(self, path, inmemory=False, **default):
        self.path = path
        self.inmemory = inmemory
        self.cache = {"default": default}

    def name(self, tenant_key):
        return str(self.path / f"{tenant_key}.db.sqlite3")

    def __getitem__(self, tenant):
        if tenant not in self.cache:
            self.cache[tenant] = {
                **self.cache["default"],
                "ENGINE": self.ENGINE,
                "NAME": self.name(tenant),
            }
        return self.cache[tenant]

    def __contains__(self, tenant):
        return True


class TenantRouter:
    def db_for_read(self, *args, **hints):
        return TENANTLOCAL.tenant

    def db_for_write(self, *args, **hints):
        return TENANTLOCAL.tenant

    def allow_relation(self, *args, **hints):
        return True

    def allow_migrate(self, *args, **hints):
        return True
