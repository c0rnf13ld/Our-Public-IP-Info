#!/usr/bin/python3

# Colorama Fore colors
# Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.

import requests
import re
import sys
import time
import signal
from colorama import Fore as c, init

# colors
red, yell, ress , cyn = c.RED, c.YELLOW, c.RESET, c.CYAN

# autoreset
init(autoreset=True)

def def_handler(sig, frame):
	print("\n[*] Exiting\n")
	sys.exit(1)

# CTRL + C
signal.signal(signal.SIGINT, def_handler)

def makeRequest():
	s = requests.session()
	r = s.get("https://www.cual-es-mi-ip.net/")

	ip = re.findall("Tu dirección IP es .+\>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", r.text)[0]
	info = re.findall("Proveedor de Internet.+Pais.+Proxy.+\s.+<tr><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td>", r.text)[0]

	provider = info[0]
	country = info[1]
	proxy = info[2]

	print(yell + "Your public ip is:", red + ip)
	print(yell + f"Provider: {red + provider}")
	print(yell + f"Country: {red + country}")
	print(yell + f"Proxy: {red + proxy}")
	print(yell + "\n\t[*] Data extracted from:" + cyn + "\"https://www.cual-es-mi-ip.net/\"")

if __name__ == '__main__':
	makeRequest()
