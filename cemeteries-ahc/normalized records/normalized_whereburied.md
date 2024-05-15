Here's a concise guide for the `normalize_whereburied.py` script:

```markdown
# `normalize_whereburied.py` Script Guide

## Introduction
This guide outlines the `normalize_whereburied.py` script that standardizes burial site references in a dataset. It transforms data from `combined.csv` into `normalized_whereburied.csv`.

## Script Functions

### Libraries:
- **csv**: Manages CSV file operations.
- **re (Regular Expressions)**: Identifies and modifies patterns in text.

### File Operations:
- **Source File**: `combined.csv`
- **Output File**: `normalized_whereburied.csv`

### Process Overview:
- The script updates various terms related to burial sites, specifically focusing on outdated or insensitive terminology, and standardizes them to "Historic 'Colored Grounds'".

### Workflow:
1. **Header Setup**:
   - Sets up the output file with a header: `['pkoakwood', 'whereburied']`. The `pkoakwood` column is used as a primary key.

2. **Data Processing**:
   - Detects the 'whereburied' column.
   - Searches for specific outdated terms.
   - Updates these terms to a more respectful and consistent format.
   - Writes updated entries to the output file.

## Documentation and Files
- **Python Script**: Found in the `scripts` folder.
- **Documentation and CSV Output**: Kept together for straightforward reference.

This script helps ensure respectful and uniform descriptions of burial sites in the dataset.
```

This guide maintains a straightforward and respectful tone while detailing the script’s purpose and functionality.