#!/bin/bash
# script takes in URL and JSON file, sends a POST request to the URL with the given JSON file
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
