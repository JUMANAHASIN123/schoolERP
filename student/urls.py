from django.urls import path
from . import views



app_name="student"
urlpatterns=[
    path('studenthome',views.student_home,name='student'),
    path('profile',views.student_profile,name='pro'),
    path('changepassword',views.student_changepassword),
    path('cssrules',views.student_cssrules),
    path('box',views.student_box),
]