from django.shortcuts import render
from .forms import contactform

# Create your views here.

def form(request):
    if request.method=='POST' :
        name = request.POST.get('name')
        email = request.POST.get('email')
        return render(request,'./first_app/form.html',{'name' : name ,'email' : email})
    else :
        return render(request,'first_app/form.html')

def about(request) :
     name = request.POST.get('name')
     email = request.POST.get('email')
     return render(request,'./first_app/about.html',{'name' : name ,'email' : email})


def contactForm(request) :
    
    if request.method=='POST':
        form = contactform(request.POST)     
        if form.is_valid():
        # file = form.cleaned_data['file']
        # storing the file in a local storage
            # with open('first_app/photos/'+file.name,'wb+') as destinantion:
            #     for chunk in file.chunks():
            #         destinantion.write(chunk)
            print(form.cleaned_data)
        
    else :
        form = contactform()
    return render(request, './first_app/django_form.html', {'form':form}) 





