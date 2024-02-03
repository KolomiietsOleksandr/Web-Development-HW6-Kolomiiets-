from django.contrib import admin
from django.urls import path, include
from myapp.views import index, create_entity

urlpatterns = [
    path('', index, name='index'),
    path('entity/', create_entity, name='create_entity'),
]
