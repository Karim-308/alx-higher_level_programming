#!/usr/bin/python3
"""Fetch data from https://alx-intranet.hbtn.io/status"""

import requests

url = 'https://alx-intranet.hbtn.io/status'
if __name__ == '__main__':
    the_page = requests.get(url).text
    print("Body response:")
    print("\t- type:", type(the_page))
    print("\t- content:", the_page)
