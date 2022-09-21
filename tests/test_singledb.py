import pytest
from django.apps import apps

from ultratenant.threadlocal import TENANTLOCAL


@pytest.mark.django_db
def test_tenant_aware_manager_filters_by_tenant_slug():
    Tenant = apps.get_model("singledb", "Tenant")
    MyModel = apps.get_model("singledb", "MyModel")

    Tenant.objects.create(key="T1")
    Tenant.objects.create(key="T2")

    TENANTLOCAL.tenant = "T1"
    m1 = MyModel.objects.create(name="Arnaldinho")

    TENANTLOCAL.tenant = "T2"
    MyModel.objects.create(name="Boris")

    TENANTLOCAL.tenant = "T1"
    assert list(MyModel.objects.all()) == [m1]


@pytest.mark.django_db
def test_tenant_aware_save():
    Tenant = apps.get_model("singledb", "Tenant")
    MyModel = apps.get_model("singledb", "MyModel")

    Tenant.objects.create(key="T1")
    Tenant.objects.create(key="T2")

    TENANTLOCAL.tenant = "T1"
    m1 = MyModel.objects.create(name="Arnaldinho")

    TENANTLOCAL.tenant = "T2"
    m2 = MyModel.objects.create(name="Boris")

    TENANTLOCAL.tenant = "T1"
    assert list(MyModel.objects.all()) == [m1]

    TENANTLOCAL.tenant = "T2"
    assert list(MyModel.objects.all()) == [m2]
