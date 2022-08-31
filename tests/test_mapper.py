from pathlib import Path

from ultratenant.multidb import SQLiteMapper, TenantRouter
from ultratenant.threadlocal import TENANTLOCAL


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
