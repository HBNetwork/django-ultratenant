from django.db import models

from ultratenant.singledb import TenantAwareAbstract


class TenantAware(TenantAwareAbstract):
    # TODO(hb): Tem que ter um jeito de apenas implementar um método.
    TENANT_MODEL = "core.Tenant"

    tenant = models.ForeignKey(TENANT_MODEL, models.CASCADE)

    class Meta:
        abstract = True


class Tenant(models.Model):
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.slug


class MyModel(TenantAware):
    name = models.CharField(max_length=100)
