#!/bin/bash
# Send an OPTIONS request to the URL and display the Allow header
curl -sI -X OPTIONS "$1" | grep -i "^Allow:" | cut -d ' ' -f2-
