#!/bin/bash
#aa
url="$1"

# Use curl to get the body and status code of the response
response=$(curl -s -w "%{http_code}" "$url")

# Extract status code
http_status=$(echo "$response")

# Check if the status code is 200 (OK)
if [ "$http_status" -eq 200 ]; then
  # Display the body of the response
  curl -s "$url"
fi
