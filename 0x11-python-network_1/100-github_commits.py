#!/usr/bin/python3
"""
Python script that takes 2 arguments to solve a challenge.
"""

import requests
from sys import argv

if __name__ == '__main__':
    # Construct the URL for fetching commits from a GitHub repository
    owner = argv[2]
    name = argv[1]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, name)

    # Send a GET request to fetch commits from the GitHub API
    response = requests.get(url)

    # Parse the response as JSON
    commits = response.json()

    # Print details of the first 10 commits
    for commit in commits[:10]:
        sha = commit.get('sha')
        author_name = commit.get('commit').get('author').get('name')
        print("{}: {}".format(sha, author_name))
