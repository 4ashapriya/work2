from django.contrib import admin
from django.urls import path, include
from .views import student_api


urlpatterns = [
    path('student_api/', student_api, name= 'student'),
]
