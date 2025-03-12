import http.client


conn = http.client.HTTPConnection("ifconfig.me")
conn.request("GET", "/ip")
public_ip = conn.getresponse().read()
print(f"Public IP Address: {public_ip.decode()}")


##  ==============================================
import socket


print(socket.gethostbyname(socket.getfqdn()))


##  ==============================================import requests
import requests


try:
    public_ip = requests.get('https://api.ipify.org').text
    print(f"Public IP Address: {public_ip}")
except requests.RequestException as e:
    print(f"Error retrieving public IP address: {e}")


try:
    response = requests.get('https://api.abstractapi.com/v1/ipaddress/?api_key=')
    response.raise_for_status()
    ip_info = response.json()
    print(ip_info)
except requests.RequestException as e:
    print(f"An error occurred: {e}")

##  ==============================================
# import pymyip # pip install pymyip0


# print("Your ip " + pymyip.get_ip())
# print("Your city " + pymyip.get_city())
# print("Your country" + pymyip.get_country())


##  ==============================================
# import urllib.request
# import re


# res = urllib.request.urlopen('http://2ip.ru/').read()
# print(re.search(b'\d+\.\d+\.\d+\.\d+', res).group())


##  ==============================================
## pip3 install --user pystun3
#import stun
#stun.get_ip_info()

