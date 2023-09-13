import subprocess

# Set the domain name for which to create a certificate
domain = 'www.top25collegefootball.com'

# Set the path to the private key and certificate files
key_file = 'keys/privkey.pem'
cert_file = 'certs/cert.pem'

# Generate a private key
subprocess.call(['openssl', 'genrsa', '-out', key_file, '2048'])

# Create a self-signed certificate
subprocess.call(['openssl', 'req', '-new', '-x509', '-key', key_file, '-out', cert_file, '-days', '365', '-subj', '/CN={}'.format(domain)])

