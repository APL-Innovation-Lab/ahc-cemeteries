import csv
import re

# Open the source and destination CSV files
with open('combined.csv', 'r') as infile, open('normalized_whereburied.csv', 'w', newline='') as outfile:
    reader = csv.reader(infile, delimiter=',', quotechar='"')
    writer = csv.writer(outfile, delimiter=',', quotechar='"')

    # Write the header to the destination file
    writer.writerow(['pkoakwood', 'whereburied'])

    # Define the regex pattern
    pattern = re.compile(r'Negro cemetery|Negro grave yarad|Negro grave yard|Negro  cemetery|Negro burial grounds?|burying ground on block|Negro grounds|Negro new cemetery')

    headers = next(reader, None)  # Read the header row

    # Find the index of the 'whereburied' column
    try:
        whereburied_index = headers.index('whereburied')
    except ValueError:
        print("'whereburied' column not found in the CSV file")
        exit(1)

    # Process each row from the source file
    for row in reader:
        # Check if the row has enough columns before accessing the whereburied index
        if len(row) <= whereburied_index:
            continue  # Skip rows with not enough columns

        # Check if the 'whereburied' column matches the pattern
        match = pattern.search(row[whereburied_index])
        if match:
            start, end = match.span()
            after = row[whereburied_index][end:]
            if after.endswith('"'):
                after = after[:-1]
            row[whereburied_index] = f'Historic "Colored Grounds"{after}'

        # Write the row to the destination file
        writer.writerow([row[0], row[whereburied_index]])


