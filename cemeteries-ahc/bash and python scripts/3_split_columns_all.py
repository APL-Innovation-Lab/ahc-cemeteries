import csv

# Read the source CSV file into memory
with open('combined.csv', 'r') as f:
    rows = list(csv.reader(f))

headers = rows[0]
rows = rows[1:]  # Remove the header row

# Loop over the headers starting from the second column
for index, header in enumerate(headers):
    if index == 0:
        continue  # Skip the first column

    # Open a new CSV file for each column
    with open(f'all_{header}.csv', 'w', newline='') as f_out:
        writer = csv.writer(f_out)
        writer.writerow([headers[0], header])  # Write the header

        # Write the rows to the new CSV file
        for row in rows:
            writer.writerow([row[0], row[index]])

