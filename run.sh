#!/bin/bash

# Run the Python script in the background and log output
nohup python3 x.py > x_log.txt 2>&1 &
echo "X Bot started in the background."
