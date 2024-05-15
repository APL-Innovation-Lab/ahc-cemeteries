#!/bin/bash

# Get current date in the format of YYYYMMDD
current_date=$(date +%Y%m%d)

# Create backup
cp combined.csv cemeteries$current_date.csv

