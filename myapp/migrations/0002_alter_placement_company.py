# -*- coding: utf-8 -*-
# Generated manually. You can rename the file as per the migration sequence.

from django.db import migrations, models

def populate_test_col_with_unique_id(apps, schema_editor):
    Company = apps.get_model('myapp', 'Company')
    Placement = apps.get_model('myapp', 'Placement')

    # Add a new column called test_col in Placement model
    # for placement in Placement.objects.all():
    #     placement.test_col = placement.company.unique_id
    #     placement.save()
    print("hello")
    #print schema of Placement
    #print(Placement._meta.get_fields())
    

    for placement in Placement.objects.all():
        # Retrieve the corresponding company based on c_name
        company_name = placement.company_id
        company = Company.objects.get(c_name=company_name)
        # Update the new foreign key field with the unique_id
        placement.test_col = company.id
        placement.save()    



def add_new_foreign_key(apps, schema_editor):
    Placement = apps.get_model('myapp', 'Placement')
    Company = apps.get_model('myapp', 'Company')

    # Add a new column called new_col which is a foreign key with to_field=unique_id
    for placement in Placement.objects.all():
        placement.new_col_id = placement.test_col
        placement.save()

class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'), # Update with actual dependency
    ]

    operations = [
        migrations.AddField(
            model_name='placement',
            name='test_col',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.RunPython(populate_test_col_with_unique_id),
        migrations.RemoveField(
            model_name='placement',
            name='company',
        ),
        migrations.AddField(
            model_name='placement',
            name='new_col',
            field=models.ForeignKey(to='myapp.Company', on_delete=models.CASCADE, to_field='id', null=True),
        ),
        migrations.RunPython(add_new_foreign_key),
        
        migrations.RemoveField(
            model_name='placement',
            name='test_col',
        ),
    ]
