#!/bin/bash
# Bash script URL as arg, sends a GET request to URL, and displays response
curl -sH "X-School-User-Id: 98" "$1"
