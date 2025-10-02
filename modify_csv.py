#!/usr/bin/env python3
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
    "Industry Security": "9254000000172852"
}

def modify_csv(input_file, output_file):
    """Modify CSV file according to specifications."""
    
    # Columns to remove
    columns_to_remove = ['Tags', 'Owner', 'Sub-Category']
    
    try:
        with open(input_file, 'r', encoding='utf-8-sig') as infile:
            reader = csv.DictReader(infile)
            
            # Get existing fieldnames and remove unwanted columns
            existing_fields = [f for f in reader.fieldnames if f not in columns_to_remove]
            
            # Add new mandatory columns at the beginning
            new_fieldnames = ['Article ID', 'Permissions', 'Status', 'Locale', 'Author ID'] + existing_fields
            
            # Replace 'Category' field name if it exists, or handle Category ID
            if 'Category' in new_fieldnames:
                category_index = new_fieldnames.index('Category')
                new_fieldnames[category_index] = 'Category ID'
            elif 'Category ID' not in new_fieldnames:
                # Add Category ID after Author ID
                new_fieldnames.insert(5, 'Category ID')
            
            rows = []
            article_id = 11001
            
            for row in reader:
                new_row = {}
                
                # Add mandatory columns
                new_row['Article ID'] = str(article_id)
                new_row['Permissions'] = 'ALL_USERS'
                new_row['Status'] = 'Published'
                new_row['Locale'] = 'en'
                new_row['Author ID'] = '9254000000000450'
                
                # Copy existing columns (except removed ones)
                for field in existing_fields:
                    if field in row:
                        new_row[field] = row[field]
                
                # Handle category mapping
                if 'Category' in row:
                    category_name = row['Category'].strip()
                    new_row['Category ID'] = CATEGORY_MAPPING.get(category_name, '')
                elif 'Category ID' in row:
                    # Check if it's a category name and map it
                    category_value = row['Category ID'].strip()
                    new_row['Category ID'] = CATEGORY_MAPPING.get(category_value, category_value)
                
                rows.append(new_row)
                article_id += 1
            
            # Write to output file
            with open(output_file, 'w', encoding='utf-8', newline='') as outfile:
                writer = csv.DictWriter(outfile, fieldnames=new_fieldnames)
                writer.writeheader()
                writer.writerows(rows)
            
            print(f"Successfully processed {len(rows)} rows")
            print(f"Output written to: {output_file}")
            return True
            
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found")
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
