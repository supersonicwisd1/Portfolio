from django.shortcuts import render
from django.views.generic import ListView

from .models import Skill

class SkillPageView(ListView):
    template_name = 'skills.html'
    model = Skill
    context_object_name = 'skills'
