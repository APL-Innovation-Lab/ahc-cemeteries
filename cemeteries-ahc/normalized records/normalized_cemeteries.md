# `normalize_birthplace.py` Script Guide

## Introduction
This guide explains the operations of the `normalize_birthplace.py` script, which standardizes birthplace data. The script is located in the `scripts` folder, processes data from `combined.csv`, and outputs it to `normalized_birthplace.csv`.

## Script Functions

### Libraries:
- **csv**: Manages reading and writing CSV files.
- **re (Regular Expressions)**: Enhances string processing capabilities.

### Process Overview:
- The script corrects and standardizes birthplace names using a set of predefined rules to address common errors and variations.

### File Operations:
- **Source File**: `combined.csv`
- **Output File**: `normalized_birthplace.csv`

### Workflow:
1. **Header Setup**:
   - Initializes the output file with the header: `['pkoakwood', 'nativity']`. Here, `pkoakwood` is retained as a primary key from the script’s previous database format.

2. **Data Normalization**:
   - Focuses on the eighth column for birthplace data.
   - Applies normalization rules to each entry.
   - Saves updated entries to the output file.

## Documentation and Files
- **Python Script**: Found in the `scripts` folder.
- **Documentation and CSV Output**: Stored together for easy reference.

This guide and the script work together to provide clear and accessible data normalization, ensuring data consistency and reliability.