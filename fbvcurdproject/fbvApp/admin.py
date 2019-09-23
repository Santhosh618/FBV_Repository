from django.contrib import admin
from .models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','Ename','Eid','Epostion','Eaddress']

admin.site.register(Employee,EmployeeAdmin)
