from ultratenant.multidb import TenantRouter
from ultratenant.threadlocal import TENANTLOCAL


def test_db_for_read():
    TENANTLOCAL.tenant = "TENANT"

    router = TenantRouter()

    assert router.db_for_read() == "TENANT"


def test_db_for_write():
    TENANTLOCAL.tenant = "TENANT2"

    router = TenantRouter()

    assert router.db_for_write() == "TENANT2"


def test_allow_relation():
    router = TenantRouter()

    assert router.allow_relation() is True


def test_allow_migrate():
    router = TenantRouter()

    assert router.allow_migrate() is True


def test_fail():
    assert False
