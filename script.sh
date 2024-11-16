#!/bin/bash

# Navigate to the src directory
cd src

# Open the first xterm and run the traffic generator
xterm -hold -e "bash -c 'python3 python_trafficgenarator_v2.py'" &

# Open the second xterm and run the main program
xterm -hold -e "bash -c 'python3 main.py'" &

