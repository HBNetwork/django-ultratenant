from django.conf import settings

from ultratenant.threadlocal import TENANTLOCAL


class TenantRouter:
    def db_for_read(self, *args, **hints):
        return TENANTLOCAL.tenant

    def db_for_write(self, *args, **hints):
        return TENANTLOCAL.tenant

    def allow_relation(self, *args, **hints):
        return True

    def allow_migrate(self, *args, **hints):
        return True


class SQLiteMapper(dict):
    def __init__(self, default):
        self.cache = {"default": default}

    def __getitem__(self, tenant):
        if tenant not in self.cache:
            self.cache[tenant] = {
                **self.cache["default"],
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": str(settings.BASE_DIR / f"{tenant}.db.sqlite3"),
            }
        return self.cache[tenant]

    def __contains__(self, tenant):
        return True
