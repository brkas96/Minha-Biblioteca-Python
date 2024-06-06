import requests
import time

# Create your account here: https://www.duckdns.org/

# Faz o update do ipv4 e ipv6 no duckDNS
def get_public_ip(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching IP: {e}")
        return None

def update_duckdns(domain, token, ipv4, ipv6):
    url = f"https://www.duckdns.org/update?domains={domain}&token={token}&ip={ipv4}&ipv6={ipv6}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error updating Duck DNS: {e}")
        return None

if __name__ == "__main__":
    domain = "YOUR-DOMAIN"
    token = "YOUR-TOKEN"

    ipv4_service_url = "https://api.ipify.org"
    ipv6_service_url = "https://api64.ipify.org"

    while True:
        print(f"Domínio atual: {domain}")
        ipv4 = get_public_ip(ipv4_service_url)
        ipv6 = get_public_ip(ipv6_service_url)
        print(f"ipv4 público: {ipv4}")
        print(f"ipv6 público: {ipv6}")

        if ipv4 and ipv6:
            result = update_duckdns(domain, token, ipv4, ipv6)
            print(f"Duck DNS update result: {result}")
        else:
            print("Failed to obtain IPv4 or IPv6 address.")

        time.sleep(1200) # wait 20 minutes

