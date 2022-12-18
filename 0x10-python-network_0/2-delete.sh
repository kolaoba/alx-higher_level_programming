#!/bin/bash
# script takes in URL, sends a DELTE request to it and displays response body
curl -sX DELETE "$1"
