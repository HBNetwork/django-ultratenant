from ultratenant.threadlocal import TenantLocal


def test_tenant_local():
    tl = TenantLocal()

    assert bool(tl) is False

    tl.tenant = "TENANT"

    assert bool(tl) is True
    assert tl.tenant == "TENANT"

    tl.reset()
    assert bool(tl) is False
