#!/bin/bash
# This script sends a request to a specified URL using curl
# then calculates and displays the size of response,
curl -s "$1" | wc -c
