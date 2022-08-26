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
