from django.contrib import admin
from django.urls import path
import account.views
#from .import views

urlpatterns = [
    path('login',account.views.login, name= "login"),
    path('signup',account.views.signup, name= "signup"),   
]