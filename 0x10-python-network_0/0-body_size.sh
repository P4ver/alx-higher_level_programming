#!/bin/bash
# This script sends a request to a specified URL using curl
curl -s "$1" | wc -c
