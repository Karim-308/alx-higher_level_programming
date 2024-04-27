#!/usr/bin/python3
"""
Python script that takes Github credentials (username and password)
and uses the Github API to display the user's id
"""

import requests
from requests.auth import HTTPBasicAuth
import sys

if __name__ == '__main__':
    # Construct the URL for the Github API endpoint
    github_username = sys.argv[1]
    git_pas = sys.argv[2]
    github_api_url = 'https://api.github.com/users/{}'.format(github_username)

    # Send a GET request to the Github API with basic authentication
    response = requests.get(github_api_url,
                            auth=HTTPBasicAuth(github_username, git_pas))

    # Print the user's id if the request is successful
    if response.status_code == 200:
        user_id = response.json().get('id')
        print(user_id)
    else:
        code = response.status_code
        print("Failed to fetch user id. Response status code:", code)
