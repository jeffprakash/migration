from django.contrib import admin
from .models import Company, Placement


# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('c_name', 'city')


class PlacementAdmin(admin.ModelAdmin):
    list_display = ('p_name',)



admin.site.register(Company, CompanyAdmin)
admin.site.register(Placement, PlacementAdmin)