from django.core.management.base import BaseCommand
from myapp.models import Company, Placement

class Command(BaseCommand):
    help = 'Change the foreign key from c_name to unique_id in Placement model'

    def handle(self, *args, **kwargs):
        try:
            placements = Placement.objects.all()

            for placement in placements:
                try:
                    # Retrieve the Company object using the existing c_name
                    company = Company.objects.get(c_name=placement.company.c_name)
                    # Update the foreign key to use unique_id
                    placement.company = company
                    placement.save()
                except Company.DoesNotExist:
                    self.stdout.write(self.style.ERROR(f"Company with c_name '{placement.company.c_name}' not found. Skipping placement {placement.p_name}"))
            
            self.stdout.write(self.style.SUCCESS('Foreign key updated successfully'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'An error occurred: {str(e)}'))
