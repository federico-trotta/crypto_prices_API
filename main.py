import datetime
import requests
from settings import settings
from functions.price import *
from functions.csv_creation import *

# Software versione
version = "v1.0"

# Import settings from the settings file
email = settings.EMAIL
token = settings.API_TOKEN
auth = (email + "/token", token) # Create authenticator

# Print welcome
print(f"\nWelcome to 'GetCryptos' by Federico Trotta. This is version {version} created in the year {datetime.date.today().year}. \nPlease: wait while I verify the prerequisites...")

# Try access by pinging the dedicated URL
try:
    ping_url = "https://api.coingecko.com/api/v3/ping"
    response = requests.get(url=ping_url, auth=auth)
    if response.status_code == 200:
        print(f"\nAccess succesfully granted to the API!")
    else:
        print(f"\nAn error occurred while autenticating. Please: try again!")
except Exception as e:
    print(f"\nAn exception occurred:", e)

# Main meù
while True:
    menu_opt = input(f"\n1 - Visualize a price\n2 - Compare prices\n0 - Exit program\n\nSelect your option: ")
    
    match menu_opt:
        case "1":
            # Visualize the price of one crypto
            visualize_price(auth)
        case "2":
            # Compare the change in price of a crypto with respect to yesterday
            price_change(auth)
        case "0":
            print(f"\nGoodbye!")
            break
        case _:
            print(f"\nWrong option. Please, try again!")