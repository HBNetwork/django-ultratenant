import pytest
from django.apps import apps
from django.test import TestCase, override_settings

from ultratenant.threadlocal import TENANTLOCAL


@pytest.mark.django_db
@override_settings(DATABASE_ROUTERS=["ultratenant.multidb.TenantRouter"])
class TestMultiDb(TestCase):
    databases = ["t1", "t2"]

    def test_asdf(self):
        MyModel = apps.get_model("multidb", "MyModel")
        TENANTLOCAL.tenant = "t1"
        m1 = MyModel.objects.create(name="Arnaldinho")
        TENANTLOCAL.tenant = "t2"
        m2 = MyModel.objects.create(name="Boris")

        TENANTLOCAL.tenant = "t1"
        assert list(MyModel.objects.all()) == [m1]

        TENANTLOCAL.tenant = "t2"
        assert list(MyModel.objects.all()) == [m2]
