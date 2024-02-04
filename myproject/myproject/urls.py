from django.urls import path
from myapp.views import index, entity, get_entity_by_id

urlpatterns = [
    path('', index, name='index'),
    path('entity/', entity, name='entity'),
    path('entity/<uuid:entity_id>/', get_entity_by_id, name='get_entity_by_id')
]
