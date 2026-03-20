from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):     #function view
    # return HttpResponse("<h1>Hello world</h1>")    #http-response
    # return render(request, "home.html", {'numbers':range(1,4), 'age': 30})
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")




