from django.shortcuts import render,redirect
from .models import Employee
from .forms import EmployeeForm



# Create your views here.
def retrieve_view(request):
    list=Employee.objects.all()
    print(list.query)
    return render(request,'testApp/list.html',{'list':list})


def create_view(request):
    Emp=EmployeeForm()
    if request.method == 'POST':
        Emp=EmployeeForm(request.POST)
        if Emp.is_valid():
            Emp.save()
            print('Record Added Successfully.......!!!!!!')
            return redirect('/list')

    return render(request,'testApp/create.html',{'Emp':Emp})

def update_view(request,id):
    record=Employee.objects.get(id=id)
    if request.method == 'POST':
        data=EmployeeForm(request.POST,instance=record)
        if data.is_valid():
            data.save()
            print('Record Updated Successfully.....!!!!!!')
            return redirect('/list')


    return render(request,'testApp/update.html',{'record':record})

def delete_view1(request,id):
    record=Employee.objects.get(id=id)
    return render(request,'testApp/delete.html',{'record':record})
    return

def delete_record(request,id):
    record=Employee.objects.get(id=id)
    record.delete()
    return redirect('/list')
