import csv
from typing import Any
from django.core.management.base import BaseCommand, CommandParser, CommandError
from django.apps import apps
from dataentry.models import Student


class Command(BaseCommand):
    help = 'Import data from CSV file'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('file_path', type=str, help='Path to the CSV file')
        parser.add_argument('model_name', type=str, help='name of the model')
        
    def handle(self, *args: Any, **kwargs: Any) -> str | None:
        file_path = kwargs.get('file_path')
        model_name = kwargs.get('model_name').capitalize()
        model = None
        for app_config in apps.get_app_configs():
            # Try to search the model
            try:
                model = apps.get_model(app_config.label, model_name)
                break
            except LookupError:
                continue
        if not model:
            raise CommandError(f' Model "{model_name}" not found in any app')
        with open(file_path, 'r') as file:
            reader  = csv.DictReader(file)
            for raw in reader:
                model.objects.create(**raw)

        self.stdout.write(self.style.SUCCESS('Data imported from CSV successfully !!!'))


