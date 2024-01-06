#!/bin/bash
<<<<<<< HEAD
#lloeazo

curl -X POST -H "Content-Type: application/json" -d "@$2" $1
=======

# Specify the target URL
url="http://0.0.0.0:5000/catch_me"

# Use curl to make a request with a custom header
curl -X PUT -s -H "Origin: HolbertonSchool" "$url" -d "user_id=98"

>>>>>>> refs/remotes/origin/main
