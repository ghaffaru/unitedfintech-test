from django.core.management.base import BaseCommand, CommandError
from unitedfintech_test.mongo import db
from django.contrib.auth.hashers import make_password


class Command(BaseCommand):
    help = 'Seeds admin data'



    def handle(self, *args, **options):
        password = make_password('12345678')

        admin = db['admins'].find_one({'email': 'admin@gmail.com'})

        if admin:
            raise CommandError('Admin already seeded')
        else:

            db['admins'].insert_one({
                "name": "Admin",
                "email": "admin@gmail.com",
                "password": password
            })



        self.stdout.write(self.style.SUCCESS('Successfully seeded admin data'))