#!/bin/bash
#aa
curl -s '%{http_code}' "$1"
