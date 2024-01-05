#!/bin/bash
#aa
response=$(curl -s -w "%{http_code}" "$1") && [ "$(echo "$response" | tail -n 1)" -eq 200 ] && curl -s "$1"
