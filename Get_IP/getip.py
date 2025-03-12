##  ==============================================
import http.client


conn = http.client.HTTPConnection("ifconfig.me")
conn.request("GET", "/ip")
public_ip = conn.getresponse().read()
print(f"Public IP Address: {public_ip.decode()}")


##  ==============================================
from urllib.request import Request, urlopen

my_ip_url = "https://ifconfig.me/ip"

my_ip_page = urlopen(Request(my_ip_url)).read()
my_ip = my_ip_page.decode('utf-8', errors='ignore')

print(f"Public IP Address: {my_ip}") # выведет Ваш ip-адрес!


##  ==============================================
import requests


my_ip_url = "https://ifconfig.me/ip"
#my_ip_url = "https://api.ipify.org"
try:
    public_ip = requests.get(my_ip_url).text
    print(f"Public IP Address: {public_ip}")
except requests.RequestException as e:
    print(f"Error retrieving public IP address: {e}")


##  ==============================================
# try:
    # ##response = requests.get('https://api.abstractapi.com/v1/ipaddress/?api_key=')
    # response = requests.get('https://api.abstractapi.com/v1/ipaddress/')
    # response.raise_for_status()
    # ip_info = response.json()
    # print(ip_info)
# except requests.RequestException as e:
    # print(f"An error occurred: {e}")


##  ==============================================
import socket


print(socket.gethostbyname(socket.getfqdn()))


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


##  ==============================================
##  https://www-abstractapi-com.translate.goog/guides/ip-geolocation/get-ip-address-python?_x_tr_sl=en&_x_tr_tl=ru&_x_tr_hl=ru&_x_tr_pto=rq#:~:text=for%20identification%20purposes.-,ipv4_address%20%3D%20socket.,device%20on%20the%20local%20network.
# import netifaces ## pip install netifaces

# def get_ip_address(interface):
    # try:
        # addrs = netifaces.ifaddresses(interface)
        # ip_info = {}
        # if netifaces.AF_INET in addrs: # Check for IPv4 address
            # ip_info['IPv4'] = addrs[netifaces.AF_INET][0]['addr']
        # if netifaces.AF_INET6 in addrs: # Check for IPv6 address
            # ip_info['IPv6'] = addrs[netifaces.AF_INET6][0]['addr']
        # if not ip_info:
            # return "No IPv4 or IPv6 address found."
        # return ip_info
    # except ValueError:
        # return "Interface not found or doesn't have an IP address."

# interface_name = 'eth0' # Replace with your interface name

# ip_address = get_ip_address(interface_name)

# print(f"IP Address of {interface_name}: {ip_address}")
