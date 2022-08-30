from ultratenant.threadlocal import TENANTLOCAL


def test_path_middleware(client):
    tenant = "TENANT"

    client.get(f"/{tenant}/admin", follow=True)

    assert TENANTLOCAL.tenant == tenant
