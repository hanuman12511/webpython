from django.shortcuts import redirect, render
from django.http import HttpResponse
# Create your views here.
def login(req):
    context={}
    if(req.method=="POST"):
        print("login",req.POST.get('email'))
        return redirect("register")
    return render(req,"Login/Login.html",context) 
def register(req):
    context={}
    return render(req,"register/register.html",context) 

    
def handlelogin(req):
    return HttpResponse("login successfully")


# Login is foldername
#Login is web page