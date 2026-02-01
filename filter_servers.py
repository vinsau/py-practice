import csv
import sys

# The data we are looking for
REGION_TO_FIND = 'us-east-1'
output_rows = []
csv_file = 'servers.csv'
try:
    with open(csv_file, 'r') as infile:
        # 1. Create a csv.reader object
        reader = csv.reader(infile)
        
        # 2. Get the header row
        header = next(reader)
        output_rows.append(header) # Add header to our output list
        
        # 3. Loop through the remaining rows
        for row in reader:
            # row is now a list, e.g., ['srv-001', 'web-prod-01', 'us-east-1', 'online']
            # --- Your logic goes here ---
            # (Check if row[2] matches REGION_TO_FIND)
            # (If it matches, append the row to output_rows)
            if row[2] == 'us-east-1':
                output_rows.append(row)
except FileNotFoundError:
    print(f"Caught Error: '{csv_file}' is invalid")
    sys.exit(1)

# 4. Write all found rows to the new file
with open('us_east_report.csv', 'w', newline='') as outfile:
    # 5. Create a csv.writer object
    writer = csv.writer(outfile)
    
    # 6. Write all the rows at once
    try:
        if len(output_rows) < 2:
            raise ValueError
        writer.writerows(output_rows)
        print(f"Report complete. Check us_east_report.csv")
    except ValueError:
        print("Caught error: array length doesn't meet the minimum requirement (l = 2)")
        sys.exit(1)


