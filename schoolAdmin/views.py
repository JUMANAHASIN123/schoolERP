from django.shortcuts import render

# Create your views here.


def schooladmin_home(request):
    return render(request,'schoolAdmin/home.html')

def view_staff(request):
     return render(request,'schoolAdmin/viewstaff.html')

def add_staff(request):
    return render(request,'schoolAdmin/addstaff.html')

def view_student(request):
    return render(request,'schoolAdmin/viewstudent.html')