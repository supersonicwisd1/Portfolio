from django.urls import path
from . import views

urlpatterns = [
    path("works/", views.WorkPageView.as_view(), name='work'),
    path('<slug:slug>/', views.tag_details, name="tag_details"),
]
