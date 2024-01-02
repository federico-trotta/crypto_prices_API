# Welcome to CoinGecko API project's documentation!


```{toctree}
:caption: MY WORKS
:hidden: 

initial
main
modules
```

This documentation describes a use case for the CoinGecko API.\
\
This use case has been developed by me in Python and the full code is on my [GitHub](https://github.com/federico-trotta/crypto_prices_API).

## Prerequisites
To use the CoinGecko API you first need to create an account on [their website](https://www.coingecko.com/).\
\
Then, you need to create an [API token](https://apiguide.coingecko.com/getting-started/getting-started). The [free plan](https://www.coingecko.com/en/api/pricing) currently allows you to make 10k API calls per month.

## Requirements
The program uses the `match` statement that, and, at the time of writing this documentation (November 2023), this requires `Python 3.10` (or newer versions).\
\
As the program calls an API, you also need the `requests` library. You can install it via:

```python
pip install requests
```

## Getting started
When you use this software you need to launch the `initial.py` file via:

```python
python3 initial.py
```

This will create a file, called `settings.py`, which stores your email and your API token: this way, every time you use this software, you won't need to insert them.\
\
After that, you can launch the main file via:

```python
python3 main.py
```

Here's how the `initial.py` file works (code reference [here](https://github.com/federico-trotta/crypto_prices_API/blob/main/initial.py)):
- The user inserts the email and the API KEY via CLI.
- The program checks if the `settings.py` file exists in the settings folder, then:
    - If exists, it warns the user that the file already exists. 
    - If it doesn't exist, it creates it and stores the email and the API KEI inserted by the user.