#!/usr/bin/python3
""" Sends a req & displays the value of the X-Request-Id
    variable found in the header
"""

from urllib import request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    with request.urlopen(url) as response:
        x_request_id = response.headers.get('X-Request-Id')
        print(x_request_id)
