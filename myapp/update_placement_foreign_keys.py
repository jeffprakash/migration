from myapp.models import Placement, Company

for placement in Placement.objects.all():
    try:
        company = Company.objects.get(c_name=placement.company.c_name)
        placement.company_id = company.unique_id
        placement.save()
    except Company.DoesNotExist:
        # Handle the case where the corresponding Company record is not found
        pass
