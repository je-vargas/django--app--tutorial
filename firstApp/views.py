import re
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.timezone import datetime

def home(request):
    return HttpResponse("Django you legend")

def hello_there(request, name):
    now = datetime.now()
    formatted_now = now.strftime("%a, %d %b, %Y at %X")

    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = f"Hello there, {clean_name}! It's {formatted_now}"
    return HttpResponse(content)
