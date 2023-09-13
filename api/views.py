from django.shortcuts import render
from django.http import JsonResponse
import subprocess


def generate_certificate(request):
    domain = request.POST['domain']
    key_file = request.POST['key_file']
    cert_file = request.POST['cert_file']

    subprocess.call(['openssl', 'genrsa', '-out', key_file, '2048'])
    subprocess.call(['openssl', 'req', '-new', '-x509', '-key', key_file, '-out', cert_file, '-days', '365', '-subj', '/CN={}'.format(domain)])

    return JsonResponse({'message': 'Certificate generated successfully'})
