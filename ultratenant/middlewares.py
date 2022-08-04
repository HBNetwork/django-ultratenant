from threading import local

from .utils import tenant_db_from_request

THREAD_LOCAL = local()


class TenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        db = tenant_db_from_request(request)
        setattr(THREAD_LOCAL, "DB", db)
        return self.get_response(request)


def get_current_db_name():
    return getattr(THREAD_LOCAL, "DB", None)


def set_db_for_router(db):
    setattr(THREAD_LOCAL, "DB", db)
