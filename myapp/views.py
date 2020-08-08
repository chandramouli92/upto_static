from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>WELCOME TO HOME PAGE</h1>")

def base (request):
    return render(request,"base.html")

def home (request):
    return render(request,"myapp/home.html",{"name":"chandu's"})

def profile(request):
    return render(request,"myapp/profile.html",{"name":"chandu's"})