#!/bin/bash
# script takes in URL, sends a POST request to the URL
# with a header variable, and displays the response body
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
