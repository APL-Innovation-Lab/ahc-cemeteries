import csv
import re

# Open the source and destination CSV files
with open('combined.csv', 'r') as infile, open('normalized_hospital.csv', 'w', newline='') as outfile:
    reader = csv.reader(infile, delimiter=',', quotechar='"')
    writer = csv.writer(outfile, delimiter=',', quotechar='"')

    # Define the regex pattern
    pattern = re.compile(r'\b(?:Lunatic Asylum)\b', re.IGNORECASE)

    headers = next(reader, None)  # Read the header row

    # Find the index of the 'remarks' column
    try:
        remarks_index = headers.index('remarks')
    except ValueError:
        print("'remarks' column not found in the CSV file")
        exit(1)

    # Write the header to the destination file
    writer.writerow(['pkoakwood', 'remarks'])

    # Process each row from the source file
    for row in reader:
        # Check if the row has enough columns before accessing the remarks index
        if len(row) <= remarks_index:
            continue  # Skip rows with not enough columns

        # Check if the 'remarks' column matches the pattern
        if pattern.search(row[remarks_index]):
            # Perform the substitution and write the row to the destination file
            row[remarks_index] = pattern.sub('Austin State Hospital', row[remarks_index])
            writer.writerow([row[0], row[remarks_index]])
