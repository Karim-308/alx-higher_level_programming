#!/usr/bin/python3
"""
    URL and an email address, sends a POST request to the
    passed URL with the email as
    a parameter, and finally displays the body of the response.
    """
import requests
import sys

if __name__ == '__main__':
    info = {'email': sys.argv[2]}
    what = requests.post(sys.argv[1], data=info)
    print(what.text)
