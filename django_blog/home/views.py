from django.shortcuts import render, HttpResponse


# Create your views here.
# create views
def home(request):
    return HttpResponse("This is my homepage (/)")
