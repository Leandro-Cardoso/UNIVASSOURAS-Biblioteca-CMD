#!/bin/bash

# Console size:
X=100
Y=30
resize -s $Y $X

# Run Python script:
PYTHON="python3"
FILE="main.py"

$PYTHON $FILE
