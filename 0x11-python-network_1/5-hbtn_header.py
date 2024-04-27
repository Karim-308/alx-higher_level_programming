#!/usr/bin/python3
""" Sends a req & displays the value of the X-Request-Id
    variable found in the header
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    the_page = requests.get(url)
    x_request_id = the_page.headers.get('X-Request-Id')
    print(x_request_id)
