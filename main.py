import ipaddress
import os
import socket
from colorama import Fore, Style
import requests

ip_address = input(Fore.YELLOW +"Enter ip address: " + Style.RESET_ALL)

def ip_scanner(ip_address):
    print(Fore.YELLOW +"Scanning..." + Style.RESET_ALL)
    try:
        hostname = socket.gethostbyaddr(ip_address)
        print(Fore.GREEN +f"The hostname of {ip_address} is: ", str(hostname) + Style.RESET_ALL)
    except socket.error:
        print(Fore.RED +"Hostname could not be resolved." + Style.RESET_ALL)
        try:
            ip = ipaddress.ip_address(ip_address)
            if ip.is_private:
                print(Fore.RED +"Private ip address" + Style.RESET_ALL)
            else:
                print(Fore.YELLOW +"Public ip address" + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED +"Invalid ip address" + Style.RESET_ALL)

def os_info(ip_address):
    print(Fore.YELLOW +"Collecting..." + Style.RESET_ALL)
    try:
        os_info = os.name
        print(Fore.GREEN +f"OS Name of {ip_address} is: ", str(os_info) + Style.RESET_ALL)
    except OSError:
        print(Fore.RED +"Error." + Style.RESET_ALL)

def localization(ip_address):
    print(Fore.YELLOW +"Collecting..." + Style.RESET_ALL)
    try:
        r = requests.get(f'https://ipapi.co/{ip_address}/json/', timeout=5)
        if r.status_code == 200:
            data = r.json()
            postal = data.get('postal', 'N/A')
            city = data.get('city', 'N/A')
            loc = data.get('loc')
            print(Fore.GREEN + f"Postal Code: {postal}" + Style.RESET_ALL)
            print(Fore.GREEN + f"City: {city}" + Style.RESET_ALL)
            print(Fore.GREEN + f"Google Maps Link: https://www.google.com/maps/search/?api=1&query={loc}" + Style.RESET_ALL)
            print(Fore.LIGHTRED_EX + "WARNING: The Google Maps link is never 100% true." + Style.RESET_ALL)
    except requests.exceptions.ConnectionError:
            print(Fore.RED +"Error." + Style.RESET_ALL)


ip_scanner(ip_address)
os_info(ip_address)
localization(ip_address)

print("\nPress a key for exit...")