#!/bin/bash
# Send a POST request to the specified URL using curl, including email and subject params,
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
