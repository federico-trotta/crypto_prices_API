import requests

def visualize_price(auth:str):
    crypto = input(f"\nChoose your crypto (for example, write 'bitcoin'):\n")
    currency = input(f"Choose the currency (for example, write 'usd'):\n")

    url_price = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies={currency}"

    response = requests.get(url=url_price, auth=auth)

    print(response.json())