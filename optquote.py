#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
import cgi, cgitb
import string

# Get the specific contract we want passed in the GET request.
args = cgi.FieldStorage()
symbol = args.getvalue('c').strip()

# Build our URL and get the HTML back and parse with BeautifulSoup
url = 'https://finance.yahoo.com/quote/' + symbol + '?p=' + symbol
r = requests.get(url)
soup = BeautifulSoup(r.text,'lxml')

# This is easily found with any number of dev tools, but its the "name" 
# of the HTML tag that has the actual value inside. There is only one
# tag with this name (HUZZUH!) so we can just use the find() method.
current_price = soup.find('span', {'class':'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'})

# OK, here's lazybones Brando coming out. I could make this a proper API 
# to return a JSON object or something, but given the integration with 
# Google Sheets, this was the easiest way to reliably get the value out.
print("Content-type:text/html\r\n\r\n")
print(current_price.text)
