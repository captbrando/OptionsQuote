#!/usr/bin/env python3

import yfinance as yf
import os
from urllib.parse import parse_qsl

# Get the query string from the environment variables
query_string = os.environ.get("QUERY_STRING", "")

# Parse the query string
query_params = dict(parse_qsl(query_string))

# Get the args from the URL string.
symbol = query_params.get('s').split(":")[1]
contract = query_params.get('c')
expiration = query_params.get('d')
opt_type = query_params.get('o')

# Get the last price on the contract we want.
stock = yf.Ticker(symbol)
option = stock.option_chain(date=expiration)

match opt_type:
        case "Call":
                lastPrice = option.calls[option.calls["contractSymbol"] == contract].lastPrice

        case "Put":
                lastPrice = option.calls[option.puts["contractSymbol"] == contract].lastPrice

# OK, here's lazybones Brando coming out. I could make this a proper API 
# to return a JSON object or something, but given the integration with 
# Google Sheets, this was the easiest way to reliably get the value out.
print("Content-type:text/html\r\n\r\n")
print(lastPrice.values[0])

