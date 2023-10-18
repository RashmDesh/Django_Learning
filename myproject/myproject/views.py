from django.http import HttpResponse
from django.shortcuts import render

def index(request):
   return HttpResponse("hello this is main page")

def home(request):
   email=request.POST["email"]
   password=request.POST["password"]
   dict={
      "UserEmail":email,
      "UserPassword":password
   }
   return render(request,"index.html",dict)

def login(request): 
   return render(request,"login.html")