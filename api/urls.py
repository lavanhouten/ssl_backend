from django.urls import path
from .views import generate_certificate

urlpatterns = [
    path('generate_certificate/', generate_certificate, name='generate_certificate'),
]
