import json
from pathlib import Path

from decouple import config
from dj_database_url import parse

DEBUG = config("DEBUG", default=False, cast=bool)
BASE_DIR = Path(".")


class DatabaseMapper(dict):
    def __init__(self, connections_string):
        self.__conn = connections_string
        self.cache = {}
        self.__convert
        del self.__conn

    @property
    def __convert(self):
        if DEBUG:
            self.cache["default"] = parse("sqlite:///" + str(Path.joinpath(BASE_DIR, "default.sqlite3").resolve()))
        if not self.__conn:
            return
        try:
            tenants = json.loads(self.__conn)
        except Exception as e:
            raise ValueError("Could not read connection string") from e

        for k, v in tenants.items():
            _key = k.split(".")[0].lower()
            _value = parse(v)
            self.cache[_key] = _value

        if "default" not in self.cache:
            raise NoDefaultDatabaseError

    def __getitem__(self, item):
        if item not in self.cache:
            self.cache[item] = {
                **self.cache["default"],
                "USER": item,
            }
        return self.cache[item]

    def __contains__(self, item):
        return True

    def __str__(self) -> str:
        return str(self.cache.keys())


class TenantsMapper:
    def __init__(self, tenant_string):
        self.__tenants = tenant_string
        self.__cache = {}
        self.__convert
        del self.__tenants

    @property
    def __convert(self):
        try:
            tenants = json.loads(self.__tenants)
        except Exception:
            print("I couldn't read the tenants string")
            return
        self.__cache = dict(tenants.items())

    @property
    def asdict(self):
        return self.__cache


class NoDefaultDatabaseError(Exception):
    ...
