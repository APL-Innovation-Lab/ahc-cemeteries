#!/bin/bash

# Iterate over all files starting with 'all_'
for filename in all_*.csv; do
    # Remove 'all_' from the filename and prepend 'unique_'
    new_filename="unique_${filename#all_}"

    # Skip the first line (header), print the second column, sort the values, remove duplicates, and save the result to the new file
    awk -F ',' 'NR>1 { print $2 }' $filename | sort | uniq > $new_filename
done

