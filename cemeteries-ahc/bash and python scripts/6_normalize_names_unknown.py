import csv

# Open the source and destination CSV files
with open('combined.csv', 'r') as infile, open('normalized_names_unknown.csv', 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Write the header to the destination file
    writer.writerow(['pkoakwood', 'firstname', 'lastname', 'name_contribution'])

    # Process each row from the source file
    for row in reader:
        # Check if the second or third column is empty, only contains spaces or is "unknown"
        if not row[1].strip() or row[1].lower() == 'unknown' or not row[2].strip() or row[2].lower() == 'unknown':
            row[3] = 'Unknown first name or last name'
            writer.writerow(row[:4])  # Write only the first four columns
