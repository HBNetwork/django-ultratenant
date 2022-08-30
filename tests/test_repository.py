# import pytest
#
#
# class BaseTenantRepository:
#     def __getitem__(self, tenant):
#         raise NotImplementedError
#
#
# class DefaultTenantRepository(BaseTenantRepository):
#     def __getitem__(self, tenant):
#         return tenant
#
#
# class SingleDBRepository(BaseTenantRepository):
#     def __getitem__(self, tenant):
#         return Tenant.objects.get(key=tenant).pk
#
#
# class MultiDBRepository(BaseTenantRepository):
#     def __getitem__(self, tenant):
#         return Tenant.objects.using("default").get(key=tenant).pk
#
#
# def test_default_repository():
#     repo = DefaultTenantRepository()
#     assert repo["tenant1"] == "tenant1"
#
#
# @pytest.mark.skip
# @pytest.mark.django_db
# def test_single_db_repository():
#     Tenant.objects.create(key="tenant1")
#
#     repo = SingleDBRepository()
#     assert repo["tenant1"] == 1
#
#
# @pytest.mark.skip
# @pytest.mark.django_db
# def test_asdf():
#     qs = MyModel.objects.all()
#     print(qs.query)
