from pathlib import Path

import pytest
from django.apps import apps
from django.test import TestCase, override_settings

from ultratenant.multidb import SQLiteMapper, TenantRouter
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


class TestSQLiteMapper:
    def test_getitem(self):
        mapper = SQLiteMapper(path=Path("/"), test=True)

        expected = {
            "test": True,
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": "/tenant.db.sqlite3",
        }

        assert mapper["tenant"] == expected

    def test_contains(self):
        mapper = SQLiteMapper(Path("/"))

        assert "tenant" in mapper
        assert "whatever" in mapper

    def test_router_and_mapper(self):
        TENANTLOCAL.tenant = "t1"

        router, mapper = TenantRouter(), SQLiteMapper(Path("/"))

        expected = {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": "/t1.db.sqlite3",
        }

        assert mapper[router.db_for_read()] == expected
        assert mapper[router.db_for_write()] == expected
