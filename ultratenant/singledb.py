from django.db import models

from ultratenant.threadlocal import TENANTLOCAL

DEFAULT_TENANT = "ultratenant.Tenant"


class TenantAbstract(models.Model):
    key = models.CharField(max_length=32, unique=True, db_index=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.key


class TenantAwareManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(tenant__key=TENANTLOCAL.tenant)


def TenantAwareFactory(tenant_model):
    class TenantAwareAbstract(models.Model):
        """
        An abstract base class model that provides a foreign key to a tenant
        """

        tenant = models.ForeignKey(tenant_model, models.CASCADE)

        objects = TenantAwareManager()
        unscoped = models.Manager()

        class Meta:
            abstract = True

    return TenantAwareAbstract


TenantAwareAbstract = TenantAwareFactory(DEFAULT_TENANT)
