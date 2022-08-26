import threading


class TenantLocal(threading.local):
    UNDEFINED = 0

    def __init__(self):
        self._tenant = self.UNDEFINED

    @property
    def tenant(self):
        return self._tenant

    @tenant.setter
    def tenant(self, name):
        self._tenant = name

    def reset(self):
        self.tenant = self.UNDEFINED

    def __bool__(self):
        return self.tenant is not self.UNDEFINED


TENANTLOCAL = TenantLocal()
