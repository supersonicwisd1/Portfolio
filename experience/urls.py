from django.urls import path
from . import views

urlpatterns = [
    path("experiences/", views.ExperiencePageView.as_view(), name='experience'),
]
