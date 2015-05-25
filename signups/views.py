from django.shortcuts import render
from django.http import HttpResponse

def signup_hello(request):
    return render(request,"hw/home.html")