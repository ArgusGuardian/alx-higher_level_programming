#!/bin/bash
# display all the method the servers allows
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
