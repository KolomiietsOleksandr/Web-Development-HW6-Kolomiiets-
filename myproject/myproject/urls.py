from django.urls import path
from myapp.views import index, entity, entity_id

urlpatterns = [
    path('', index, name='index'),
    path('entity/', entity, name='entity'),
    path('entity/<uuid:entity_id>/', entity_id, name='entity_by_id')
]
