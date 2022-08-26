from django.conf import settings

from ultratenant.database import TenantRouter
from ultratenant.multidb import SQLiteMapper
from ultratenant.threadlocal import TENANTLOCAL


def test_init():
    default = {"test": True}

    mapper = SQLiteMapper(default)

    assert mapper["tenant"] == {
        **default,
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": str(settings.BASE_DIR / "tenant.db.sqlite3"),
    }


def test_get():
    mapper = SQLiteMapper({})

    assert mapper["tenant"] == {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": str(settings.BASE_DIR / "tenant.db.sqlite3"),
    }
    assert mapper["tenant2"] == {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": str(settings.BASE_DIR / "tenant2.db.sqlite3"),
    }


def test_contains():
    mapper = SQLiteMapper({})

    assert "tenant" in mapper
    assert "whatever" in mapper


def test_router_and_mapper():
    TENANTLOCAL.tenant = "TENANT"

    router = TenantRouter()
    mapper = SQLiteMapper({})

    assert mapper[router.db_for_read()] == {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": str(settings.BASE_DIR / "TENANT.db.sqlite3"),
    }
    assert mapper[router.db_for_write()] == {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": str(settings.BASE_DIR / "TENANT.db.sqlite3"),
    }
