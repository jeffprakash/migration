from django.db import models

# Create your models here.


class Company(models.Model):
    c_name = models.CharField(max_length=100,unique=True)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.c_name
    


class Placement(models.Model):
    p_name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, related_name='company',on_delete=models.CASCADE, to_field='c_name', null=True)

    # sil=models.ForeignKey(Company, on_delete=models.CASCADE,to_field='city', null=True,db_constraint=False,db_index=False)
    #models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)
    # sec_id= models.CharField(max_length=100, null=True, unique=False)
    #new_id=models.ForeignKey(Company, on_delete=models.CASCADE,to_field='unique_id',unique=False, null=True)
    #new_id=models.ForeignKey(Company, on_delete=models.CASCADE,to_field='unique_id')


    def __str__(self):
        return self.p_name