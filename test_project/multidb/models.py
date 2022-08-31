from django.db import models

from ultratenant.multidb import TenantAbstract


class MyModel(models.Model):
    name = models.CharField(max_length=100)


class Tenant(TenantAbstract):
    pass
