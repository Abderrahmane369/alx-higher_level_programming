#!/usr/bin/env bash
curl -s -w "%{size_download}" -o /dev/null "$1"
