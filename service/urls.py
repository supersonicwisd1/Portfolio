from django.urls import path
from . import views

urlpatterns = [
    path("services/", views.ServicePageView.as_view(), name='services'),
]
