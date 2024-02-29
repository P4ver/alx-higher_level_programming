#!/bin/bash
# Sends a GET request to a specified URL using curl and displays the response status code.
curl -s -o /dev/null -w "%{http_code}" "$1"
