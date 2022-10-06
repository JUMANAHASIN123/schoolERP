from django.shortcuts import render

# Create your views here.


def student_home(request):
    return render(request,'student/studenthome.html')

def student_profile(request):
    return render(request,'student/profile.html')

def student_changepassword(request):
    return render(request,'student/changepassword.html')

def student_cssrules(request):
    return render(request,'student/cssrules.html')

def student_box(request):
    return render(request,'student/box.html')