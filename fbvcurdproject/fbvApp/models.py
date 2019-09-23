from django.db import models

# Create your models here.
class Employee(models.Model):
    Ename=models.CharField(max_length=30)
    Eid=models.IntegerField()
    Epostion=models.CharField(max_length=30)
    Eaddress=models.CharField(max_length=30)
