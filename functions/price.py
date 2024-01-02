import requests
from functions.csv_creation import *

def visualize_price(auth:str)->None:
    """This function shows the current price of a crypto with respect to a currency.\n

    **NOTE**: The auth variable is created in the `main.py` file.
    """
     # User inserts crypto and currency
    crypto = input(f"\nChoose your crypto (for example, write 'bitcoin'):\n")
    currency = input(f"Choose the currency (for example, write 'usd'):\n")
   
    # API call
    url_price = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies={currency}"

    response = requests.get(url=url_price, auth=auth)

    # Print current price of a crypto in the selected currency
    try:
        if response.status_code == 200:
            data = response.json()
            print(f"\nThe current price for {crypto} is: {data[crypto][currency]: .1f} {currency}")

            # Store crypto value, if user wants
            user_answer = input(f"\nWould you like to store the data in the CSV? [y,n]:\n")

            if user_answer == "y":
                # Create CSV if it doesn't exist
                new_csv()

                # Write data on CSV
                write_data(crypto, data, currency)
            elif user_answer == "n":
                print(f"\nOk, good!\n")
            else:
                print(f"\nWrong option. Please, try again if you want to store the value of the crypto in the CSV file \n")
        else:
            print(f"An error occurred while getting the price: please, try again!")
    except Exception as e:
        print(f"An exception occurre while trying to get the currency value", e)
            

def price_change(auth:str)->None:
    '''This functions hows the difference of the price of a crypto in a currency with respect to the value it had yesterday.\n

    **NOTE**: The auth variable is created in the `main.py` file.
    '''

    # User inserts crypto and currency
    crypto = input(f"\nChoose your crypto (for example, write 'bitcoin'):\n")
    currency = input(f"Choose the currency (for example, write 'usd'):\n")

    # API call
    url_increment = f"https://api.coingecko.com/api/v3/coins/{crypto}/market_chart?vs_currency={currency}&days=1&interval=daily"

    response = requests.get(url=url_increment, auth=auth)

    try:
        if response.status_code == 200:
            data = response.json()
            current_value = data["prices"][1][1]
            yesterday_value = data["prices"][0][1]
            change_price = current_value - yesterday_value
            print(f"\nThe current value of {crypto} is {current_value: .1f} {currency} while yesterday's value was {yesterday_value: .1f} {currency}.\nSo, the price has changed by {change_price: .1f} {currency} from yesterday")
        else:
            print(f"An error occurred while getting the price: please, try again!")
    except Exception as e:
        print(f"An exception occurred while trying to get the currency value", e)


