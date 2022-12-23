from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.db.models import Q

from .models import Work, Tag

class WorkPageView(ListView):
    template_name = 'work.html'
    model = Work
    context_object_name = 'works'

def tag_details(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    projects = tag.tags.all()

    context = {
        'tags': tag,
        'projects': projects
    }
    return render(request, 'tags.html', context)