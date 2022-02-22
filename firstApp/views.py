import re
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.timezone import datetime

def home(request):
    return HttpResponse("Django you legend")

def hello_there(request, name):
    return render(
        request, 
        "firstApp/hello_there.html",
    {
        "name":name,
        "date": datetime.now()
    }
    )

def home(request):
    return render(request, "firstApp/home.html")

def about(request):
    return render(request, "firstApp/about.html")

def contact(request):
    return render(request, "firstApp/contact.html")
