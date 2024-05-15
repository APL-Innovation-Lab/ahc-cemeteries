import csv
import re

# Regular expression pattern for matching content inside parentheses
pattern = re.compile(r'\((.*?)\)')

# Open the source and destination CSV files
with open('combined.csv', 'r') as infile, open('normalized_name.csv', 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Write the header to the destination file
    writer.writerow(['pkoakwood', 'firstname', 'name_contribution'])

    # Process each row from the source file
    for row in reader:
        # Check if the second column has a match
        match = pattern.search(row[1])
        if match:
            # Extract the content inside parentheses
            archival_name = match.group(1).strip()

            # Remove the content inside parentheses from the first name
            firstname = pattern.sub('', row[1]).strip()

            # If there is existing content in the fourth column, append the archival name
            if row[3].strip():
                archival_name = row[3].strip() + " " + archival_name

            # Write the processed row to the destination file
            writer.writerow([row[0], firstname, archival_name])

