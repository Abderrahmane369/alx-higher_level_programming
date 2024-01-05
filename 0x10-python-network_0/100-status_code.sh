#!/bin/bash
#binobasha
curl -o /dev/null -s -w "%{http_code}\n" "$1"

