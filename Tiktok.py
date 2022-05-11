import requests
from requests.sessions import session
import json
import time
import colorama
from colorama import Fore, Back, Style

colorama.init()

session = requests.session()

print(Fore.CYAN + """ Syndicate Anti TikTok Scam""")
print("")
print("")
print("Created by Syndicate")

print("")
print("")

x = input('Enter the request URL from Inspect Element: ')
print("")
print("")

print('Reporting scammer.....')
print('')
print('')

while True:
    req = session.post(x)
    
    print(req.text)
    print('The Scammer has been reported.')

    time.sleep(10)


input()



