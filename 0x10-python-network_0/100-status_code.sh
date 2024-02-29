#!/bin/bash
# send get request to server
curl -s -o /dev/null -w "%{http_code}" "$1"
