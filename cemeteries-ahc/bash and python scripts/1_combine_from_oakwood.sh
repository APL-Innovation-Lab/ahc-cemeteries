#!/bin/bash

# Get the header from the first file
head -n 1 oakwood1.csv > combined.csv

# Concatenate the rest of the lines, skipping the headers
for i in {1..8}; do
    awk 'FNR > 1' oakwood$i.csv >> combined.csv
done

