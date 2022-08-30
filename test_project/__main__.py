import sys

from django.core.management import execute_from_command_line

from .project import configure

configure()
execute_from_command_line(sys.argv)
