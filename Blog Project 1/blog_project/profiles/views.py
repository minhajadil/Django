from django.shortcuts import render,redirect
from .forms import ProfileForm

# Create your views here.

def add_profile(request):
    if request.method=='POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('Add_Profile')
    else :
        form = ProfileForm()
    return render(request,'add_profile.html', {'form':form})


