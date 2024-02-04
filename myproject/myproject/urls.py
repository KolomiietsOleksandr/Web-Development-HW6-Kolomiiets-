from django.urls import path
from myapp.views import index, entity

urlpatterns = [
    path('', index, name='index'),
    path('entity/', entity, name='entity'),
]
