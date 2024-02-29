#!/bin/bash
# display all the method the servers allows
curl -sI "$1" | gerp "Allow" | cut -d " " -f 2-
