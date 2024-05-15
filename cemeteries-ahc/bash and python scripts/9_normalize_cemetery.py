import csv
import re

subs = [(re.compile(pattern, re.IGNORECASE), replacement) for pattern, replacement in [
    (r"\bMt Calvary\b", "Mount Calvary"),
    (r"\bMt Cal\b", "Mount Calvary"),
    (r"^State$", "State Cemetery"),
    (r"^Annex$", "Oakwood Annex"),
    (r"Cem(?=\s|$)", "Cemetery"),
    (r"\bCol\.?\s*Gr\.?\b", "Colored Grounds"),
    (r"\bStanger\s*grounds?\b", "Strangers Grounds"),
    (r"\bStranger\s*grounds?\b", "Strangers Grounds"),
    (r"\bOld Strangers Grounds\b", "Strangers Grounds"),
    (r"\bMe?x\.?\s*Grd?\.?\b", "Mexican Grounds"),
    (r"\bColored Grounds ds\.\b", "Colored Grounds"),
    (r"\bStrng\.\b", "Strangers"),
    (r"\bGrds\.\b", "Grounds"),
    (r"\bOld Grds\b", "Old Grounds"),
    (r"^Pauper(\s+Gr\.)?$|^Pauper Ground$", "Pauper Grounds"),
]]

with open('combined.csv', 'r', encoding='utf-8-sig') as infile, open('normalized_cemetery.csv', 'w', newline='') as outfile:
    reader = csv.DictReader(infile)
    writer = csv.writer(outfile, delimiter=',')  # Specifying the delimiter as comma

    # Print the headers for debugging
    print(f'Headers in the CSV file: {reader.fieldnames}')

    # Write the header to the destination file
    writer.writerow(['pkoakwood', 'whereburied'])

    # Process each row from the source file
    for row in reader:
        orig_value = row['whereburied']
        # Apply the substitutions
        for pattern, replacement in subs:
            row['whereburied'] = pattern.sub(replacement, row['whereburied'])

        # If the value changed, write the row to the output CSV
        if row['whereburied'] != orig_value:
            writer.writerow([row['pkoakwood'], row['whereburied']])
