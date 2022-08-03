#!/usr/bin/env python
import os
import sys

from multitenant.middlewares import set_db_for_router

if __name__ == "__main__":
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    from django.db import connection

    args = sys.argv
    db = args[1]
    # import ipdb; ipdb.set_trace()
    with connection.cursor() as cursor:
        set_db_for_router(db)
        del args[1]
        execute_from_command_line(args)
