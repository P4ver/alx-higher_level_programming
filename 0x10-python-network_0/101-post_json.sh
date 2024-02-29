#!/bin/bash
# Sends a JSON POST request to a specified URL and displays the body of the res.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
