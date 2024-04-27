#!/usr/bin/python3
""" Sends a request to the URL and displays
    the body of the response (decoded in utf-8).
    """

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            the_page = response.read()
            print(the_page.decode('utf-8'))
    except urllib.error.URLError as e:
        print("Error:", e)
