#!/bin/bash
# This script sends a DELETE request to the URL provided as the first arg using curl.
curl -sX "DELETE" "$1"
