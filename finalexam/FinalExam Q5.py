import ssl
import socket
from datetime import datetime, timezone

def check_cert_expiry(hostname):
    context = ssl.create_default_context()
    with socket.create_connection((hostname, 443), timeout=5) as sock:

        # Wrap the socket using SSL
        ssl_sock = context.wrap_socket(sock, server_hostname=hostname)

        # Retrieve the certificate
        cert = ssl_sock.getpeercert()

        # Extract expiry date and convert to datetime
        expiry_s = cert['notAfter']
        expiry_date = datetime.strptime(expiry_s, "%b %d %H:%M:%S %Y %Z")
        expiry_date = expiry_date.replace(tzinfo=timezone.utc)

        # Calculate remaining days
        now = datetime.now(timezone.utc)
        days_left = (expiry_date - now).days

        print(f"Certificate for {hostname} expires on {expiry_date} ({days_left} days left)")

# Example usage
check_cert_expiry("www.sheridancollege.ca")