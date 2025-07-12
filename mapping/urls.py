from django.urls import path
from . import views

urlpatterns = [
    path('smellmap/', views.smell_map, name='smell_map'),
]
