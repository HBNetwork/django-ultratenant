from ultratenant.threadlocal import TENANTLOCAL


class BaseTenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        TENANTLOCAL.tenant = self.identify_tenant(request)
        return self.get_response(request)

    @staticmethod
    def identify_tenant(request):
        raise NotImplementedError


class SubdomainTenantMiddleware(BaseTenantMiddleware):
    @staticmethod
    def identify_tenant(request):
        host = request.get_host()
        subdomain = host.split(".")[0]
        return subdomain


class DomainTenantMiddleware(BaseTenantMiddleware):
    @staticmethod
    def identify_tenant(request):
        return request.get_host()


class PathTenantMiddleware(BaseTenantMiddleware):
    @staticmethod
    def identify_tenant(request):
        tenant, path = request.path_info[1:].split("/", 1)
        request.path_info = "/" + path
        return tenant
