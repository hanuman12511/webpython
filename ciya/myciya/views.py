from django.shortcuts import redirect, render
from django.http import HttpResponse
from myciya.models import *
# Create your views here.
def login(req):
    context={}
    if(req.method=="POST"):
        print("login",req.POST.get('email'))
        user1 =user()
        user1.uid = req.POST.get('email')
        user1.save()
        if req.POST.get('email') =="admin@gmail.com":
            return redirect("home")
        else :
            return redirect("login")
    return render(req,"Login/Login.html",context) 
def register(req):
    
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