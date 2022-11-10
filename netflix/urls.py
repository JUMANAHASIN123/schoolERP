from django.urls import path
from . import views

app_name="netflix"
urlpatterns=[
    path('netflix',views.netflix,name='home1'),
    path('signin',views.signin,name='signin'),
    path('home',views.home,name='home'),
    path('payment',views.payment,name='payment'),
    path('netflixhome',views.netflixhome,name='netflixhome'),
]