from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def about(request) :
    return HttpResponse("this is first page/about")
def home(request) :
    return HttpResponse("this is first page")
def contact(request) :
    return HttpResponse("this is first page/contact")

