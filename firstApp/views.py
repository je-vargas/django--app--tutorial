import re
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.timezone import datetime
from django.shortcuts import redirect
from firstApp.forms import LogMessageForm
from firstApp.models import LogMessage
from django.views.generic import ListView

class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context
    

# def home(request):
#     return HttpResponse("Django you legend")

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

# def log_message(request):
#     return render(request, "firstApp/log_message.html")

def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    else:
        return render(request, "firstApp/log_message.html", {"form": form})
