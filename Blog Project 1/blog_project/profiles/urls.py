from django.urls import path
from .import views

urlpatterns = [
    
    path('add/', views.add_profile,name="Add_Profile"),
   
]
