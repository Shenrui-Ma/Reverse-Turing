#!/bin/bash

cd "$(dirname "$0")"

source ./turenv/conda/etc/profile.d/conda.sh
conda activate ./turenv/env

python main.py

if [ $? -ne 0 ]; then
    echo "Press any key to continue..."
    read -n 1 -s
fi