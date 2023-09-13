from django.contrib import admin
from django.urls import path
from .views import generate_certificate
from .api import GenerateCertificateView

urlpatterns = [
    path('api/generate_certificate/', GenerateCertificateView.as_view(), name='generate_certificate_api'),
    path('generate_certificate/', generate_certificate, name='generate_certificate'),
]
