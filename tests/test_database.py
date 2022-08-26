from django.conf import settings

from ultratenant.database import SQLiteMapper, TenantRouter
from ultratenant.threadlocal import TENANTLOCAL


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
