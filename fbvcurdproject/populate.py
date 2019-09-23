import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','fbvcurdproject.settings')
import django
django.setup()

from fbvApp.models import Employee


from random import *
from faker import Faker
fake = Faker()
def fakedata(n):
    for x in range(n):
        name=fake.name()
        id=fake.random_number(4)
        postion=fake.name()
        address=fake.address()
        emp_record=Employee.objects.get_or_create(Ename=name,Eid=id,Epostion=postion,Eaddress=address)
fakedata(20)
