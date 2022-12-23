from django.urls import path
from . import views

urlpatterns = [
    path("education/", views.EducationPageView.as_view(), name='education'),
]
