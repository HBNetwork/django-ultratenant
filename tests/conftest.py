import pytest
from threadlocal import TENANTLOCAL


@pytest.hookimpl(tryfirst=True)
def pytest_configure():
    from test_project import configure

    configure()


@pytest.fixture(autouse=True)
def reset_thread():
    TENANTLOCAL.reset()
