from django.contrib import admin
from django.urls import path
import home.views
#from .import views

urlpatterns = [
    path('',home.views.main, name= "main"),
    
]