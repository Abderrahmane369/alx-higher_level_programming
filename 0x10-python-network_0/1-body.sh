#!/bin/bash
# # Sends a POST request to the passed URL, and displays the body of the response
# Write a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -sL "$1" -X POST -d "