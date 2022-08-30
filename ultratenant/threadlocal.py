import threading


class TenantLocal(threading.local):
    UNDEFINED = 0

    def __init__(self):
        self.tenant = self.UNDEFINED

    def reset(self):
        self.tenant = self.UNDEFINED

    def __bool__(self):
        return self.tenant is not self.UNDEFINED


TENANTLOCAL = TenantLocal()
