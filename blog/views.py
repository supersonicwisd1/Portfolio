from django.shortcuts import render
from django.views.generic import ListView

from .models import Blog

class BlogPageView(ListView):
    template_name = 'blog.html'
    model = Blog
    context_object_name = 'blogs'