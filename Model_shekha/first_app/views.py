from django.shortcuts import render,redirect
from .import models
from first_app.forms import StudentForm

# Create your views here.

def home(request):
    student = StudentForm
    return render(request,'first_app/home.html',{'data':student})


def delete(request,roll):
    delete_st = models.Student.objects.get(pk=roll).delete()
    return redirect("home")
