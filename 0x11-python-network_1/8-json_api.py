#!/usr/bin/python3
"""
Sends a POST request to http://0.0.0.0:5000/search_user
with a letter as a parameter.
Displays the id and name if the response is
properly JSON formatted and not empty.
"""

import requests
import sys

if __name__ == "__main__":
    q = sys.argv[1]

    info = {'q': q}
    response = requests.post(
        "http://0.0.0.0:5000/search_user",
        data=info
    )

    try:
        if response.status_code == 200:
            json_response = response.json()
            if isinstance(json_response, dict) and json_response:
                jres = json_response['name']
                print("[{}] {}".format(json_response['id'], jres))
            else:
                print("No result")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
