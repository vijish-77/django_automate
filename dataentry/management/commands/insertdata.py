# I want to add some data to the database using custom command

from django.core.management.base import BaseCommand
from dataentry.models import Student

class Command(BaseCommand):
    help = 'Some help'

    def handle(self, *args, **kwargs):
        dataset = [
            {'roll_no':1006, 'name':'Sanu', 'age': 21},
            {'roll_no':1007, 'name':'James', 'age': 22},
            {'roll_no':1009, 'name':'Mirash', 'age': 23},
                   ]
        for raw in dataset:
            roll_no = raw.get('roll_no')
            print(roll_no)
            existing_record = Student.objects.filter(roll_no=roll_no).exists()
            if not existing_record:
                Student.objects.create(roll_no=raw.get('roll_no'), name=raw.get('name'), age=raw.get('age'))
            else:
                self.stdout.write(self.style.WARNING(f'Student with old roll_no {roll_no} already exists !!!!'))
                
        self.stdout.write(self.style.SUCCESS('Data inserted successfully !!!'))

