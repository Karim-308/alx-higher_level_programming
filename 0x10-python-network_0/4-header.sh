#!/bin/bash
# Bash script that takes in a URL as an argument, sends a GET request to URL, and displays response
curl -sX GET $1 "X-School-User-Id : 98"
