#!/usr/bin/python3
"""
Retrieves data from a given URL and displays the decoded response body.
"""

from urllib import request as req
from urllib import error as err
import sys

if __name__ == "__main__":
    # Get the URL from the command-line argument
    target_url = sys.argv[1]

    try:
        # Open a connection to the URL
        with req.urlopen(target_url) as response:
            # Read the response body
            response_body = response.read()

            # Display the decoded response body
            print(response_body.decode('utf-8'))
    except err.URLError as e:
        # Handle URL errors
        print("Error:", e)
