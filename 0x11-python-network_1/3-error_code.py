#!/usr/bin/python3
"""
Sends a request to a URL and displays the body of the response.
"""

if __name__ == "__main__":
    import sys
    from urllib import request, error

    # Get the URL from the command-line argument
    target_url = sys.argv[1]

    try:
        # Send a request to the URL
        with request.urlopen(target_url) as response:
            # Display the body of the response
            print(response.read().decode('UTF-8'))
    except error.HTTPError as e:
        # Handle HTTP errors
        print('Error code:', e.code)
