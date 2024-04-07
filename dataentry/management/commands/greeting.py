from typing import Any
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Greet the user"
    
    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help=" Specify the  user name")


    def handle(self, *args: Any, **kwargs: Any) -> str | None:
        name = kwargs.get('name')
        greeting = f'Hi {name}, Good Morning ....'
        self.stdout.write(self.style.SUCCESS(greeting))