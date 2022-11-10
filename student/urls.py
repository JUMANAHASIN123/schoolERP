from django.urls import path
from . import views



app_name="student"
urlpatterns=[
    path('studenthome',views.student_home,name='student'),
    path('profile',views.student_profile,name='pro'),
    path('changepassword',views.student_changepassword),
    path('cssrules',views.student_cssrules),
    path('box',views.student_box),
    path('box2',views.student_box2),
    path('flex',views.student_flex),
    path('bootstrap',views.student_bootstrap),
    path('respons',views.student_response),
    
]