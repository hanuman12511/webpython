from django.shortcuts import redirect, render
from django.http import HttpResponse
from myciya.models import *
# Create your views here.
def login(req):
    context={}
    if(req.method=="POST"):
        form = register.objects.all()
        print(form)
        for data in form :
            print(data.email,end="")
            print(data.password)
      
        print("login",req.POST.get('email'))
        print("login",req.POST.get('password'))
        
        #return redirect("home")
        
    return render(req,"Login/Login.html",context) 


def Register(req):
    context={}
    if(req.method=="POST"):
        register1 =register()
        register1.name = req.POST.get('name')
        register1.email = req.POST.get('email')
        register1.password = req.POST.get('password')
        register1.save()
        
        return redirect("login")
    return render(req,"register/register.html",context) 
def Showdata(req):
    
    form = user.objects.all()
    print(form)
    context = {'form':form}
    
    return render(req,"register/register.html",context)
    
def handlelogin(req):
    return HttpResponse("login successfully")

def home(req):
    context={}
    return render(req,"home/home.html",context) 
# Login is foldername
#Login is web page