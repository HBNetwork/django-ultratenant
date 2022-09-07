from django.db import models

from ultratenant.singledb import TenantAbstract, TenantAwareFactory


class Tenant(TenantAbstract):
    pass


TenantAware = TenantAwareFactory("singledb.Tenant")


class MyModel(TenantAware):
    name = models.CharField(max_length=100)
