#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL
curl -si "$1" | grep Content-Length | gerp -o '[0-9]\+'
