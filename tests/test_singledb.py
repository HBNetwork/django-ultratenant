import pytest
from django.apps import apps

from ultratenant.threadlocal import TENANTLOCAL


@pytest.mark.django_db
def test_tenant_aware_manager_filters_by_tenant_slug():
    Tenant = apps.get_model("singledb", "Tenant")
    MyModel = apps.get_model("singledb", "MyModel")

    t1 = Tenant.objects.create(key="T1")
    t2 = Tenant.objects.create(key="T2")
    m1 = MyModel.objects.create(name="Arnaldinho", tenant=t1)
    MyModel.objects.create(name="Boris", tenant=t2)

    TENANTLOCAL.tenant = "T1"

    assert list(MyModel.objects.all()) == [m1]
