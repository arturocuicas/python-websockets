""" Notes Urls."""

# Django
from django.urls import path

# Note
from . import views


urlpatterns = [
    path('', views.NoteList.as_view()),
    path('<int:pk>/', views.NoteDetail.as_view()),
]
