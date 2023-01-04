# from django import views
from django.urls import path
from .views import *
from studentApp import views
urlpatterns = [
    path('',StudentListView.as_view(), name="student"),
    path('addStudentData/', views.StudentData, name='StaudentData'),
]
