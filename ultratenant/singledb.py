from django.db import models

from ultratenant.threadlocal import TENANTLOCAL

# class MyModel(models.Model):
#     key = models.CharField(max_length=255)
#
#     class Meta:
#         @property
#         def db_table(self):
#             return "SCHEMA.TABLENAME"


class TenantAwareManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(tenant_id=TENANTLOCAL.tenant)


class TenantAwareAbstract(models.Model):
    """
    An abstract base class model that provides a foreign key to a tenant
    """

    TENANT_MODEL = "ultratenant.Tenant"

    tenant = models.ForeignKey(TENANT_MODEL, models.CASCADE)

    objects = TenantAwareManager()
    unscoped = models.Manager()

    class Meta:
        abstract = True
