#!/bin/bash
# Send a POST request to the URL with the specified parameters and display the body of the response
curl -s -X POST -d "email=test@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD" "$1"
