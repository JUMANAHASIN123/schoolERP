from django.shortcuts import render

# Create your views here.


def netflix(request):
    return render(request,'netflix/netflix.html')
def signin(request):
    return render(request,'netflix/signin.html')
def home(request):
    return render(request,'netflix/home.html')
def payment(request):
    return render(request,'netflix/payment.html')
def netflixhome(request):
    return render(request,'netflix/netflixhome.html')

