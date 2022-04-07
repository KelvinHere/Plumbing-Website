from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
import os

class Command(BaseCommand):
    help = "Creates an admin user if it doesn't already exist"

    def handle(self, *args, **options):
        User = get_user_model()
        ''' Setup Superuser if doesn't exist '''
        print('##############')
        print(os.environ.get('SUPERUSER_USERNAME'))
        if not User.objects.filter(username=os.environ.get('SUPERUSER_USERNAME')).exists():
            superuser = User.objects.create_superuser(username=os.environ.get('SUPERUSER_USERNAME'),
                                          email=os.environ.get('SUPERUSER_EMAIL'),
                                          password=os.environ.get('SUPERUSER_PASSWORD'))
            print(f'{superuser.username} : CREATED')
        else:
            print(f'ADMIN : Already Exists')
