"""
Django command to wait for database be available
"""
import time
from django.core.management.base import BaseCommand
from django.db.utils import OperationalError
from psycopg import OperationalError as PsycopgOpError

class Command(BaseCommand):
    """DJango command to wait for database"""

    def handle(self, *args, **kwargs):
        self.stdout.write("Waiting for database...")
        db_up = False
        while db_up is False:
            try:
                self.check(database=["default"])
                db_up = True
            except(PsycopgOpError, OperationalError):
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)
            except Exception as e:
                self.stdout.write(e)
        
        self.stdout.write("Database Ready")
        
