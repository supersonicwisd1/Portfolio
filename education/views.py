# from django.shortcuts import render
from django.views.generic import ListView
from .models import Education

class EducationPageView(ListView):
    template_name = 'education.html'
    model = Education
    context_object_name = 'educations'
