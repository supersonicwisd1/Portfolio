from django.urls import path
from . import views

urlpatterns = [
    path("skills/", views.SkillPageView.as_view(), name='skills'),
]
