from django.contrib import admin
from django.urls import path

from Homepage import views

urlpatterns = [
    path('', views.Index, name="Index"),
    path('research', views.Research, name="Research"),
]
