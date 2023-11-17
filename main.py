import datetime
import requests
from settings import settings
from functions.price import *

# Software versione
version = "v1.0"

# Import settings from the settings file
email = settings.EMAIL
token = settings.API_TOKEN
auth = (email + "/token", token) # Create authenticator

# Print welcome
print(f"\nWelcome to 'GetCryptos' by Federico Trotta. This is version {version} for the year {datetime.date.today().year}. \nPlease: wait while I verify the prerequisites...")

# Try access by pinging the dedicated URL
try:
    ping_url = "https://api.coingecko.com/api/v3/ping"
    response = requests.get(url=ping_url, auth=auth)
    if response.status_code == 200:
        print(f"\nAccess succesfully granted to the API!")
    else:
        print(f"\nAn error occurred while auteenticating. Please: try again!")
except Exception as e:
    print(f"\nAn exception raised:", e)

while True:
    menu_opt = input(f"\n1 - Visualize a price\n2 - Compare price\n3 - LIST all the Tokens generated (JSON)\n4 - LIST all the Tokens generated (IDs)\n5 - REVOKE one token\n6 - REVOKE all tokens\n0 - EXIT\n\nSelect your option: ")
    
    match menu_opt:
        case "1":
            visualize_price(auth)
        case "2":
            price_change(auth)
        case "0":
            print(f"\nGoodbye!")
            break
        case _:
            print(f"\nWrong option. Please, try again!")