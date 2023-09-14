import requests
import sys
import json

if len(sys.argv) == 1:
    print("Missing command-line argument")
elif sys.argv[1].isalpha():
    print("Command-line argument is not a number")


try:
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    dict = r.json()
    dollar = dict["bpi"]["USD"]["rate_float"]
    amount = float(sys.argv[1])
    bitcoin = float(amount) * dollar
    print(f"${bitcoin:,.4f}")
except requests.RequestException:
    pass
