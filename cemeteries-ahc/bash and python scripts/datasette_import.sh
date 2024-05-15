#!/bin/bash
# Script to create a SQLite database and import a CSV file

# Set database and table names
DATABASE="ahc-cemeteries.db"
TABLE_NAME="cemetery_data"
CSV_FILE="cemetery_data_all_pages.csv"

# Check if CSV file exists
if [ ! -f "$CSV_FILE" ]; then
    echo "Error: CSV file does not exist."
    exit 1
fi

# Create or open the database
sqlite3 $DATABASE ".databases"

# Import CSV data into the database
#sqlite-utils insert $DATABASE $TABLE_NAME $CSV_FILE --csv --detect-types --pk=pkoakwood
#sqlite-utils insert $DATABASE $TABLE_NAME $CSV_FILE --csv --pk=pkoakwood
sqlite-utils insert $DATABASE $TABLE_NAME $CSV_FILE --csv

# Serve the database with Datasette
datasette serve $DATABASE
