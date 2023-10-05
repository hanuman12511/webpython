from django.shortcuts import render

# Create your views here.
def login(req):
    context={}
    return render(req,"Login/Login.html",context) 
def register(req):
    context={}
    return render(req,"register/register.html",context) 


# Login is foldername
#Login is web page