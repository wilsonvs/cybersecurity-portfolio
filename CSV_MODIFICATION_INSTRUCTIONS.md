# CSV Modification Instructions

## Overview
This script modifies the `CYBERPHORE_1000_FULL_CONTENT.csv` file with the following changes:

### 1. Adds Mandatory Columns:
- **Permissions**: ALL_USERS
- **Status**: Published
- **Locale**: en
- **Author ID**: 9254000000000450

### 2. Replaces Category Names with Category IDs:
| Category Name | Category ID |
|--------------|-------------|
| Network Security | 9254000000172234 |
| Cloud Security | 9254000000172516 |
| Data Protection | 9254000000172544 |
| Application Security | 9254000000172572 |
| Security Testing | 9254000000172600 |
| Endpoint Security | 9254000000172628 |
| Threat Intelligence | 9254000000172656 |
| Identity & Access | 9254000000172684 |
| Security Operations | 9254000000172712 |
| Compliance & Governance | 9254000000172740 |
| Emerging Technologies | 9254000000172768 |
| Training & Awareness | 9254000000172796 |
| Communication Security | 9254000000172824 |
| Industry Security | 9254000000172852 |

## Usage

### Step 1: Place your CSV file
Make sure `CYBERPHORE_1000_FULL_CONTENT.csv` is in the workspace directory.

### Step 2: Run the script
```bash
python3 modify_csv.py
```

This will create a modified file named `CYBERPHORE_1000_FULL_CONTENT_modified.csv`.

### Step 3: Replace the original (optional)
If you want to replace the original file:
```bash
python3 modify_csv.py CYBERPHORE_1000_FULL_CONTENT.csv CYBERPHORE_1000_FULL_CONTENT.csv
```

Or manually:
```bash
mv CYBERPHORE_1000_FULL_CONTENT_modified.csv CYBERPHORE_1000_FULL_CONTENT.csv
```

## Custom Usage
You can also specify input and output files:
```bash
python3 modify_csv.py input_file.csv output_file.csv
```

## What the Script Does
1. Reads the existing CSV file
2. Adds the four mandatory columns (Permissions, Status, Locale, Author ID)
3. Renames "Category" column to "Category ID"
4. Maps category names to their corresponding IDs
5. Writes the modified data to the output file

## Note
- The script preserves all existing columns and data
- If a category name doesn't match the mapping, it keeps the original value
- The script handles UTF-8 encoding for international characters
