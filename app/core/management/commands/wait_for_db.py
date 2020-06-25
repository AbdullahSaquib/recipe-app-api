import time

from django.db import connections
# used for checking if database connection available
from django.db.utils import OperationalError
# used for throwing error when db isn't available
from django.core.management.base import BaseCommand
# on this class we build on in order to create custom comamnd


class Command(BaseCommand):
    """Django command to pause execution until db is availble"""

    # this is run when we run our management command
    def handle(self, *args, **options):
        self.stdout.write('Waiting for database...')
        # outputs a message to screen

        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available !'))
        # SUCCESS will print in green
