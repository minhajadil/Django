from django.shortcuts import render,redirect
from .forms import PostForm
from .models import Posts
# Create your views here.

def add_post(request) :
    if request.method=='POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_post')
    else :
        form =PostForm()
    return render(request,'add_posts.html',{'form':form})



def edit_post(request,id):
    obj = Posts.objects.get(pk=id)
    form = PostForm(instance=obj)
    


    if request.method=='POST':
        form = PostForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    
    return render(request,'add_posts.html',{'form':form})


def delete_post(request,id):
    post = Posts.objects.get(pk=id)
    post.delete()
    return redirect('homepage')