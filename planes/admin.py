from django.contrib import admin
from .models import Plane

# Register your models here.

class CustomPlaneAdmin(admin.ModelAdmin):
    model = Plane
    list_display = ['name','Manufacturer', 'Cost', 'Year_Published', 'Reviewer']
    fieldsets= (
        ('Reviewer',{
            'fields':('Reviewer',
            )}
        ),
        ('Plane info',{
            'fields':('name', 'Manufacturer', 'Speed', 'Cost','Year_Published',
            )}
        ), 
    )

    
admin.site.register(Plane, CustomPlaneAdmin)
