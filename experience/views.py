from django.shortcuts import render
from django.views.generic import ListView
from .models import Experience

class ExperiencePageView(ListView):
    template_name = 'experience.html'
    model = Experience
    context_object_name = 'experiences'