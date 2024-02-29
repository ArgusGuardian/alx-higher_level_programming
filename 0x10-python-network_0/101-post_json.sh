#!/bin/bash
# send jasonpost request to server
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
