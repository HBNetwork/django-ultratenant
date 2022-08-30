import pytest


@pytest.hookimpl(tryfirst=True)
def pytest_configure():
    from test_project import configure

    configure()
