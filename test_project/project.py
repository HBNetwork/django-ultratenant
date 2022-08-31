from decouple import Csv, config
from dj_database_url import parse as dburl
from django.conf import settings
from django.http import HttpResponse
from django.urls import path


def configure(**kwargs):
    params = dict(
        DEBUG=config("DEBUG", default=False),
        ALLOWED_HOSTS=config("ALLOWED_HOSTS", default="*", cast=Csv()),
        SECRET_KEY=config("SECRET_KEY", default="SECRET"),
        ROOT_URLCONF=__name__,
        DEFAULT_AUTO_FIELD="django.db.models.AutoField",
        INSTALLED_APPS=["test_project.core", "test_project.multidb"],
        DATABASES={
            "default": config("DATABASE_URL", default="sqlite://:memory:", cast=dburl),
            "t1": config("DATABASE_URL", default="sqlite://:memory:", cast=dburl),
            "t2": config("DATABASE_URL", default="sqlite://:memory:", cast=dburl),
        },
        **kwargs
    )
    return settings.configure(**params)


def home(request):
    return HttpResponse("Welcome!")


urlpatterns = [
    path("", home),
]
