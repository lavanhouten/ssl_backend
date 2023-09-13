from rest_framework.views import APIView
from rest_framework.response import Response
from OpenSSL import crypto
from django.http import FileResponse
import zipfile
import io

class GenerateCertificateView(APIView):
    def get(self, request):
        subject = request.query_params

        # Generate a key pair
        key = crypto.PKey()
        key.generate_key(crypto.TYPE_RSA, 2048)

        # Create a self-signed certificate
        cert = crypto.X509()
        cert.get_subject().C = subject.get('C', '')
        cert.get_subject().ST = subject.get('ST', '')
        cert.get_subject().L = subject.get('L', '')
        cert.get_subject().O = subject.get('O', '')
        cert.get_subject().OU = subject.get('OU', '')
        cert.get_subject().CN = subject.get('CN', '')
        cert.set_serial_number(1000)
        cert.gmtime_adj_notBefore(0)
        cert.gmtime_adj_notAfter(10*365*24*60*60)
        cert.set_issuer(cert.get_subject())
        cert.set_pubkey(key)
        cert.sign(key, 'sha256')

        data = {
            'certificate': crypto.dump_certificate(crypto.FILETYPE_PEM, cert).decode('utf-8'),
            'key': crypto.dump_privatekey(crypto.FILETYPE_PEM, key).decode('utf-8')
        }

        # Return the data as a JSON response
        return Response(data)
