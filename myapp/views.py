from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    return HttpResponse("<h1>WELCOME TO HOME PAGE</h1>")

def base (request):
    return render(request,"base.html")

def home (request):
    return render(request,"myapp/home.html",{"name":"chandu's"})

def profile(request):
    return render(request,"myapp/profile.html",{"name":"chandu's"})

def get_demo(request):
    name=request.GET.get('name')
    return render(request,"get_demo.html",{'name':name})

def post_demo(request):
    if request.method=='POST':
        name=request.POST.get('name')
        return HttpResponse("<h1>thanks for submitting {} as your data".format(name))

    return render(request,"post_demo.html")

def register(request):
    if request.method=='POST':
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        email=request.POST.get("email")
        pwd=request.POST.get("pwd")
        phno=request.POST.get("phno")
        date=request.POST.get("birthday_day")
        month=request.POST.get("birthday_month")
        year=request.POST.get("birthday_year")
        gender=request.POST.get("sex")
        if gender=="1":
            gender="female"

        else:
            gender="male"
            
        send_mail("thanks for registarin", "hello mr./ms.{} {}\n welcome to our world".format(first_name,last_name),
        "pchandramouli92@gmail.com",[email,],fail_silently=False)

        return HttpResponse("{}<br>{}<br>{}<br>{}<br>{}<br>{}<br>{}<br>{}<br>{}<br>".format(first_name,last_name,email,pwd,phno,date,month,year,gender))

    return render(request,"myapp/registrations.html")

def multi(request):
    if request.method=='POST':
        foods=request.POST.getlist("food")
        languages=request.POST.getlist("language")
        return HttpResponse("<h1>{} {}</h1>".format(foods,languages))
    return render(request,"multiselector.html")

def img_upld(request):
    return render(request,"img_upld.html")
    


from myapp.utilities import store_image
    
def image_display(request):
    file_url=False
    if request.method=="POST" and request.FILES:
        image1=request.FILES.get('cm1')
        image2=request.FILES.get('cm2')
        file_urls=map(store_image,[image1,image2])
    return render(request,"image_display.html",context={'file_urls':file_urls})
        


from myapp import forms
def builtinforms(request):
    form=forms.SampleForms()
    return render(request,"builtin.html",{'form':form})
        
            
    