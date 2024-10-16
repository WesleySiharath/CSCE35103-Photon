#!/bin/bash

# Navigate to the src directory
cd src

# Open the first xterm and run the UDP server
xterm -hold -e "bash -c 'python3 python_udpserver.py'" &

# Open the second xterm and run the main program
xterm -hold -e "bash -c 'python3 main.py'" &

