from django.apps import apps
from django.test import TestCase, modify_settings


class TestSingledbWithMiddlewares(TestCase):
    def make_fixtures(self, t1_key, t2_key):
        Tenant = apps.get_model("singledb", "Tenant")
        MyModel = apps.get_model("singledb", "MyModel")

        t1 = Tenant.objects.create(key=t1_key)
        t2 = Tenant.objects.create(key=t2_key)
        m1 = MyModel.objects.create(name="Arnaldinho", tenant=t1)
        m2 = MyModel.objects.create(name="Boris", tenant=t2)

        return m1, m2

    @modify_settings(MIDDLEWARE={"prepend": "ultratenant.middlewares.PathTenantMiddleware"})
    def test_path_middleware(self):
        m1, m2 = self.make_fixtures("t1", "t2")

        r = self.client.get(f"/t1/singledb/{m1.pk}")

        assert r.status_code == 200
        assert r.content == b"Arnaldinho"

        r = self.client.get(f"/t1/singledb/{m2.pk}")

        assert r.status_code == 404

        r = self.client.get(f"/t2/singledb/{m2.pk}")

        assert r.status_code == 200
        assert r.content == b"Boris"

    @modify_settings(MIDDLEWARE={"prepend": "ultratenant.middlewares.SubdomainTenantMiddleware"})
    def test_subdomain_middleware(self):
        m1, m2 = self.make_fixtures("T1", "T2")

        r = self.client.get(f"/singledb/{m1.pk}", HTTP_HOST="T1.domain.com")

        assert r.status_code == 200
        assert r.content == b"Arnaldinho"

        r = self.client.get(f"/singledb/{m2.pk}", HTTP_HOST="T1.domain.com")

        assert r.status_code == 404

    @modify_settings(MIDDLEWARE={"prepend": "ultratenant.middlewares.DomainTenantMiddleware"})
    def test_domain_middleware(self):
        m1, m2 = self.make_fixtures("t1.com", "t2.net")

        r = self.client.get(f"/singledb/{m1.pk}", HTTP_HOST="t1.com")

        assert r.status_code == 200
        assert r.content == b"Arnaldinho"

        r = self.client.get(f"/singledb/{m2.pk}", HTTP_HOST="t1.com")

        assert r.status_code == 404

        r = self.client.get(f"/singledb/{m2.pk}", HTTP_HOST="t2.net")

        assert r.status_code == 200
        assert r.content == b"Boris"
