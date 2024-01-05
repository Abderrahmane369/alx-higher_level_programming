#!/bin/bash
#aa
curl -s --write-out '%{200}\n' "$1"
