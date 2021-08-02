import sys
import time
import requests
import re
import os
from signal import signal, SIGINT
from colorama import init, Fore

init(autoreset=True)

def closeSignal(sig, frame):
	print("\n\n[*] Exiting...\n")
	sys.exit(1)

# CTRL + C
signal(SIGINT, closeSignal)

# Global Variables
main_url = "https://www.getmypublicip.com"
# second_main_url = "https://privacysavvy.com/tools/what-is-my-ip/"

# colors
red, yell, rst, mgnt = Fore.RED, Fore.YELLOW, Fore.RESET, Fore.MAGENTA
lgcyn, lgyell = Fore.LIGHTCYAN_EX, Fore.LIGHTYELLOW_EX

def makeRequest():
	try:
		r = requests.get(main_url)
		ip = re.findall("Your public IP is : .+\"\>(.*?)\<\/", r.text)[0]
		country = re.findall("Country : (.*?)\n", r.text)[0]
		latitude = re.findall("Latitude\/Longitude : (.*?)\/.+\<", r.text)[0]
		longitude = re.findall("Latitude\/Longitude : .+\/(.*?)\<", r.text)[0]
		hostname = re.findall("Your hostname : .+\>(.*?)\<", r.text)[0]

		#r = requests.get(second_main_url)
		#city = re.findall("City: .+\> (.*?) \<", r.text)[0]

		print(mgnt + "[*] The information of your " + lgyell +"public ip\n")
		print("\t" + lgcyn + "Your Public IP: " + lgyell + ip)
		print("\t" + lgcyn + "Country: " + lgyell + country)
		#print("\t" + lgcyn + "City: " + lgyell + city)
		print("\t" + lgcyn + "Latitude: " + lgyell + latitude)
		print("\t" + lgcyn + "Longitude: " + lgyell + longitude)
		print("\t" + lgcyn + "Your hostname: " + lgyell + hostname)
		print(mgnt + "\n[*] Data extracted from: " + lgyell + f"{main_url}")

	except Exception as e:
		print(red + f"[!] An exception ocurred...\n\n{e}")
		sys.exit(1)

if __name__ == '__main__':

	print(lgcyn + "[*] Checking if the web is active...", end="\r")

	try:
		r = requests.get(main_url, timeout=5)
		os.system('clear')
		makeRequest()

	except requests.exceptions.Timeout:
		print(red + f"[!] Timeout, check from your browser if {main_url} is active.")
		sys.exit(1)

	except requests.exceptions.ConnectionError:
		print(red + "[!] Failed to establish the connection.")
		sys.exit(1)
