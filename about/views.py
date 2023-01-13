# from django.shortcuts import render
from django.views.generic import ListView
from .models import About
from .forms import ContactForm

class HomePageView(ListView):
    template_name = 'index.html'
    model = About
    context_object_name = 'abouts'

class AboutPageView(ListView):
    template_name = 'about.html'
    model = About
    context_object_name = 'abouts'

class ContactPageView(ListView):
    template_name = 'contact.html'
    model = About
    context_object_name = 'contacts'

# def contact(request):
# form = ContactForm()


# def home(request):
#     context = {
#         'abouts': About.objects.all()
#     }
#     return render(request, 'index.html', context)
    
# def about(request):
#     context = {
#         'abouts': About.objects.all()
#     }
#     return render(request, 'about.html', context)
