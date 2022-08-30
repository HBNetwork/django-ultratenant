import pytest
from django.apps import apps


@pytest.mark.django_db
def test_first_test():
    MyModel = apps.get_model("core", "MyModel")

    assert not MyModel.objects.all()
