from django.shortcuts import render
from django.views.generic import ListView

from .models import Service
from about.models import About 

class ServicePageView(ListView):
    template_name = 'services.html'
    model = Service
    context_object_name = 'services'
