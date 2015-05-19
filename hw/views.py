from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,"hw/home.html", {'blood': 'yo'})

def hello(request):
    return render(request,"hw/hello.html")