#!/bin/bash
# Script to retrieve and display the HTTP methods accepted by a srvr for a given URL
curl -sI "$1" | grep "Allow" | cut -d " " -f2-
