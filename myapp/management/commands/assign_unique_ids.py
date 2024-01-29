from django.core.management.base import BaseCommand
from myapp.models import Company

class Command(BaseCommand):
    help = 'Assigns unique IDs to existing company records'

    def handle(self, *args, **kwargs):
        # Get all existing company records
        companies = Company.objects.all()

        # Assign unique IDs based on the company name
        for idx, company in enumerate(companies, start=1):
            # Customize the logic for generating unique IDs based on your requirements
            company.unique_id = f'COMP{idx}'  # Example: COMP1, COMP2, ...
            company.save()

        self.stdout.write(self.style.SUCCESS('Successfully assigned unique IDs to existing company records.'))
