
from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name="home"),
     path('add/', add_task, name='add_task'),
]
