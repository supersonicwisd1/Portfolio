from django.urls import path
from . import views

urlpatterns = [
    path("blogs/", views.BlogPageView.as_view(), name='blog'),
]
