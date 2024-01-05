#!/bin/bash
# doing
curl -s -w "%{size_download}" -o /dev/null "$1"
