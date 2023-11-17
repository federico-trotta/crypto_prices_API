import requests

def visualize_price(auth:str):
    crypto = input(f"\nChoose your crypto (for example, write 'bitcoin'):\n")
    currency = input(f"Choose the currency (for example, write 'usd'):\n")

    url_price = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies={currency}"

    response = requests.get(url=url_price, auth=auth)
    try:
        if response.status_code == 200:
            data = response.json()
            print(f"The current price for {crypto} is: {data[crypto][currency]} {currency}")
        else:
            print(f"An error occurred while getting the price: please, try again!")
    except Exception as e:
        print(f"An exception occurre while trying to get the currency value", e)