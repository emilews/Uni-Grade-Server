from django.urls import path
from . import views


urlpatterns = [
    path('grades/', views.Grades)
]