# In your migration file
from django.db import migrations,models

def populate_new_foreign_key(apps, schema_editor):
    Placement = apps.get_model('myapp', 'Placement')
    Company = apps.get_model('myapp', 'Company')
    # Iterate through Placement objects
    

    for placement in Placement.objects.all():
        # Retrieve the corresponding company based on c_name
        # print("hehe",placement.company)
        company = Company.objects.get(city=placement.company)
        # Update the new foreign key field with the unique_id
        placement.company_new_id = company.unique_id
        placement.save()

class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_placement_company'),
    ]

    operations = [
    
        # Step 2: Populate data in the new foreign key field
        migrations.RunPython(populate_new_foreign_key),
        # Step 3: Delete the old foreign key field
        migrations.RemoveField(
            model_name='placement',
            name='company_new',
        ),
    ]
