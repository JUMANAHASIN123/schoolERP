from django.urls import path
from . import views

urlpatterns=[
    path('addstudent',views.add_student),
    path('changepassword',views.change_password), 
    path('home',views.teacher_home),
    path('viewstudent',views.view_student),
]
