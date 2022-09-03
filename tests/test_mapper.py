from pathlib import Path

from django.apps import apps
from django.test import TestCase

from ultratenant.multidb import DatabaseMapper, SQLiteMapper, TenantRouter
from ultratenant.threadlocal import TENANTLOCAL

PATH = Path(__file__).parent


class TestDatabaseMapper(TestCase):
    def test_load_tenant_dburl_from_default_database(self):
        dbfilename = str(PATH / "t3.sqlite3")

        TENANTLOCAL.tenant = "default"
        Tenant = apps.get_model("multidb", "Tenant")
        Tenant.objects.create(key="t3", dburl="sqlite:///" + dbfilename)

        map = DatabaseMapper(default="sqlite://:memory:")

        assert map["t3"]["NAME"] == dbfilename


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
        assert TENANTLOCAL.tenant == "t1"
        assert router.db_for_read() == "t1"
        assert mapper[router.db_for_read()] == expected
        assert mapper[router.db_for_write()] == expected
