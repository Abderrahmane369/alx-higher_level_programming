#!/bin/bash
#binobasha
if response=$(curl -s -w "%{http_code}" "$1"); then echo $response; fi
