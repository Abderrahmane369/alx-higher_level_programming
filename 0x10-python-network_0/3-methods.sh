#!/bin/bash
#yoiizaejrutuuofz^ppdf
curl -siX OPTIONS "$1" | grep -i "Allow:" | sed 's/Allow: //i'
