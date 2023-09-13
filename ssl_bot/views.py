from django.http import HttpResponse
from django.http import FileResponse
from OpenSSL import crypto
import zipfile

def generate_certificate(request):
    # Generate a key pair
    key = crypto.PKey()
    key.generate_key(crypto.TYPE_RSA, 2048)

    # Create a self-signed certificate
    cert = crypto.X509()
    cert.get_subject().C = "US"
    cert.get_subject().ST = "California"
    cert.get_subject().L = "San Francisco"
    cert.get_subject().O = "My Company"
    cert.get_subject().OU = "My Organization"
    cert.get_subject().CN = "mydomain.com"
    cert.set_serial_number(1000)
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(10*365*24*60*60)
    cert.set_issuer(cert.get_subject())
    cert.set_pubkey(key)
    cert.sign(key, 'sha256')

    # Return the certificate and key as a response
    response = HttpResponse(content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename=certificate.zip'

    with zipfile.ZipFile(response, 'w') as zf:
        zf.writestr('cert.pem', crypto.dump_certificate(crypto.FILETYPE_PEM, cert))
        zf.writestr('key.pem', crypto.dump_privatekey(crypto.FILETYPE_PEM, key))

    return response
