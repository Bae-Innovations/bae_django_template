from django.core.management.base import BaseCommand
from auth.models import User

class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(username='sakib').exists():
            User.objects.create_superuser('sakib', 'mail@sakibsadmanshajib.com', "CFTxdr456")