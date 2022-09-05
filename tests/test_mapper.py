from pathlib import Path

from django.apps import apps
from django.test import TestCase

from ultratenant.multidb import DatabaseMapper
from ultratenant.threadlocal import TENANTLOCAL

PATH = Path(__file__).parent


class TestDatabaseMapper(TestCase):
    def test_load_tenant_dburl_from_default_database(self):
        dbfilename = str(PATH / "t3.sqlite3")

        TENANTLOCAL.tenant = "default"
        Tenant = apps.get_model("multidb", "Tenant")
        Tenant.objects.create(key="t3", dburl="sqlite:///" + dbfilename)

        map = DatabaseMapper(default="sqlite://:memory:")

        assert map["t3"]["NAME"] == dbfilename
