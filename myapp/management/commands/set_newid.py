from django.core.management.base import BaseCommand
from myapp.models import Placement,Company  # Import your model here

class Command(BaseCommand):
    help = 'Copy values from sec_id to new_id'

    def handle(self, *args, **kwargs):
        # Iterate through all Placement objects with a non-empty sec_id
        for placement in Placement.objects.exclude(sec_id=None):
            # Find the corresponding Company object based on sec_id
            try:
                company = Company.objects.get(unique_id=placement.sec_id)
                placement.new_id = company  # Set the new_id to the corresponding Company object
                placement.save()  # Save the Placement object
            except Company.DoesNotExist:
                self.stdout.write(self.style.ERROR(f'Company with unique_id {placement.sec_id} not found for Placement {placement.p_name}'))

        self.stdout.write(self.style.SUCCESS('Successfully copied sec_id to new_id for Placements'))
