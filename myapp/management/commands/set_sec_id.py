from django.core.management.base import BaseCommand
from myapp.models import Placement

class Command(BaseCommand):
    help = 'Set sec_id for Placement objects based on unique_id of associated Company'

    def handle(self, *args, **options):
        placements = Placement.objects.all()

        for placement in placements:
            company = placement.company
            if company:
                placement.sec_id = company.unique_id
                placement.save()
                self.stdout.write(self.style.SUCCESS(f'Sec_id set for Placement {placement.pk}'))

        self.stdout.write(self.style.SUCCESS('Sec_id setting completed'))
