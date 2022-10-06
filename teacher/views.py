from django.shortcuts import render

# Create your views here.

def add_student(request):
    return render(request,'teacher/addstudent.html')

def change_password(request):
     return render(request,'teacher/changepassword.html')

def teacher_home(request):
    return render(request,'teacher/home.html')

def view_student(request):
    return render(request,'teacher/viewstudent.html')