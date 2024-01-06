#!/bin/bash
#loazeo
curl -s -o /dev/null -w "%{http_code}" "$1"
