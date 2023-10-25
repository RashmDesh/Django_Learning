from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index,name="userindex"), 
    path("contact/", views.contact,),
     path("result/", views.result,),
]
