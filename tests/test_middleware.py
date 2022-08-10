from ultratenant.middleware import (
    TENANTLOCAL,
    BaseTenantMiddleware,
    DomainTenantMiddleware,
    PathTenantMiddleware,
    SubdomainTenantMiddleware,
)


class ConstantTenantMiddleware(BaseTenantMiddleware):
    """Used to test BaseTenantMiddleware saves to TENANTLOCAL."""

    @staticmethod
    def identify_tenant(request):
        return "TENANT"


def request_factory(host="", path=""):
    """Request factory to set host header and/or path."""
    from django.http import HttpRequest

    req = HttpRequest()

    if host:
        req.META.update({"HTTP_HOST": host})

    if path:
        req.path_info = path

    return req


def test_base_middleware():
    """Test BaseTenantMiddleware persists tenant name to threadlocal."""
    request = request_factory("T1.domain.com")
    ConstantTenantMiddleware(lambda r: r)(request)

    assert TENANTLOCAL.tenant == "TENANT"


def test_subdomain_middleware():
    request = request_factory("T1.domain.com")
    tenant = SubdomainTenantMiddleware(lambda r: r).identify_tenant(request)

    assert tenant == "T1"


def test_domain_middleware():
    request = request_factory("domain.com")
    tenant = DomainTenantMiddleware(lambda r: r).identify_tenant(request)

    assert tenant == "domain.com"


def test_path_middleware():
    request = request_factory(path="/tenant/some-resource/1")
    tenant = PathTenantMiddleware(lambda r: r).identify_tenant(request)

    assert tenant == "tenant"
    assert request.path_info == "/some-resource/1"  # Overridden.
