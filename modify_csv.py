#!/usr/bin/env python3
"""
Script to modify CYBERPHORE_1000_FULL_CONTENT.csv with required changes:
1. Add mandatory columns: Permissions, Status, Locale, Author ID
2. Replace category names with Category IDs
"""

import csv
import sys

# Category mapping
CATEGORY_MAPPING = {
    "Network Security": "9254000000172234",
    "Cloud Security": "9254000000172516",
    "Data Protection": "9254000000172544",
    "Application Security": "9254000000172572",
    "Security Testing": "9254000000172600",
    "Endpoint Security": "9254000000172628",
    "Threat Intelligence": "9254000000172656",
    "Identity & Access": "9254000000172684",
    "Security Operations": "9254000000172712",
    "Compliance & Governance": "9254000000172740",
    "Emerging Technologies": "9254000000172768",
    "Training & Awareness": "9254000000172796",
    "Communication Security": "9254000000172824",
    "Industry Security": "9254000000172852",
}

def modify_csv(input_file, output_file):
    """Modify the CSV file with required changes."""
    
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)
            
            # Get existing fieldnames
            fieldnames = reader.fieldnames
            if not fieldnames:
                print("Error: CSV file has no headers")
                return False
            
            # Add new mandatory columns if they don't exist
            new_columns = []
            if 'Permissions' not in fieldnames:
                new_columns.append('Permissions')
            if 'Status' not in fieldnames:
                new_columns.append('Status')
            if 'Locale' not in fieldnames:
                new_columns.append('Locale')
            if 'Author ID' not in fieldnames:
                new_columns.append('Author ID')
            
            # Update fieldnames
            output_fieldnames = list(fieldnames) + new_columns
            
            # Replace 'Category' with 'Category ID' if it exists
            if 'Category' in output_fieldnames:
                category_index = output_fieldnames.index('Category')
                output_fieldnames[category_index] = 'Category ID'
            elif 'Category ID' not in output_fieldnames:
                # If neither exists, add Category ID
                output_fieldnames.append('Category ID')
            
            # Read all rows
            rows = []
            for row in reader:
                new_row = {}
                
                # Copy existing data and handle category mapping
                for key, value in row.items():
                    if key == 'Category':
                        # Map category name to ID
                        category_name = value.strip() if value else ""
                        category_id = CATEGORY_MAPPING.get(category_name, value)
                        new_row['Category ID'] = category_id
                    else:
                        new_row[key] = value
                
                # Add mandatory columns
                new_row['Permissions'] = 'ALL_USERS'
                new_row['Status'] = 'Published'
                new_row['Locale'] = 'en'
                new_row['Author ID'] = '9254000000000450'
                
                # If Category ID wasn't set and there's no Category column
                if 'Category ID' not in new_row or not new_row['Category ID']:
                    new_row['Category ID'] = ''
                
                rows.append(new_row)
        
        # Write modified CSV
        with open(output_file, 'w', encoding='utf-8', newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=output_fieldnames)
            writer.writeheader()
            writer.writerows(rows)
        
        print(f"Successfully modified CSV file: {output_file}")
        print(f"Total rows processed: {len(rows)}")
        print(f"Columns: {', '.join(output_fieldnames)}")
        return True
        
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found")
        return False
    except Exception as e:
        print(f"Error processing CSV: {str(e)}")
        return False

if __name__ == "__main__":
    input_file = "CYBERPHORE_1000_FULL_CONTENT.csv"
    output_file = "CYBERPHORE_1000_FULL_CONTENT_modified.csv"
    
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    if len(sys.argv) > 2:
        output_file = sys.argv[2]
    
    success = modify_csv(input_file, output_file)
    sys.exit(0 if success else 1)
