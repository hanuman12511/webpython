from .import views
from django.urls import path
urlpatterns =[
    path("login",views.login,name='login'),
    path("register",views.Register,name='register'),
    path("handlelogin",views.handlelogin,name='handlelogin'),
    path("home",views.home,name='home')
]