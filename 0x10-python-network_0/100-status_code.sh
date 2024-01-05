#!/bin/bash
#binobasha
curl -s -w '%{http_code}' "$1" | awk '{print $1}'
