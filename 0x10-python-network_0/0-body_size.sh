#!/bin/bash
# get the size of the response header
curl -s "$1" | wc -c
