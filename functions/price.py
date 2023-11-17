import requests

def visualize_price(auth:str)->None:
    """Shows the current price of a crypto with respect to a currency"""

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
            print(f"\nThe current price for {crypto} is: {data[crypto][currency]} {currency}")
        else:
            print(f"An error occurred while getting the price: please, try again!")
    except Exception as e:
        print(f"An exception occurre while trying to get the currency value", e)

def price_change(auth:str)->None:
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
            print(f"\nThe current value is {current_value: .1f} {currency} and yesterday's value was {yesterday_value: .1f} {currency}.\nSo, the price has changed by {change_price: .1f} {currency} from yesterday")
        else:
            print(f"An error occurred while getting the price: please, try again!")
    except Exception as e:
        print(f"An exception occurre while trying to get the currency value", e)