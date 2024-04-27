#!/usr/bin/python3
"""
Sends a POST request to a URL with an email parameter and displays the response body.
"""

from urllib import parse as url_parse
from urllib import request as url_request
import sys


if __name__ == "__main__":
    # Get URL and email from command-line arguments
    target_url = sys.argv[1]
    email_value = {"email": sys.argv[2]}
    encoded_data = url_parse.urlencode(email_value).encode("ascii")

    # Send a POST request
    request = url_request.Request(target_url, encoded_data)
    with url_request.urlopen(request) as response:
        # Display the body of the response
        print(response.read().decode("utf-8"))
