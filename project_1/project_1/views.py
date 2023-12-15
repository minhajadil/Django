from django.http import HttpResponse

def contacts(request) :
    return HttpResponse("this is a contact page")

def home(request) :
    return HttpResponse("this is home page")
