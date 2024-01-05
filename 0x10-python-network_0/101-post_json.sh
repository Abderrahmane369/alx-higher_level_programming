#!/bin/bash
#opinui
curl -s -X POST -H "Content-Type: application/json" --data @"request.json" "0.0.0.0:5000/route_json"

