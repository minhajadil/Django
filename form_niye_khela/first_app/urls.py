from django.urls import path
from .import views

urlpatterns = [
    path('form/',views.form),
    path('about/',views.about),
    path('django_form/',views.contactForm) 
    
]
