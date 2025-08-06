import csv

csv_file = 'xau_usd_m15.csv'

with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter='\t')

    columns = next(reader, None)
    if columns:
        print("Column Names:")
        print(" | ".join(columns))
        print("-" * (len(" | ".join(columns))))

        first_row = next(reader, None)
        if first_row:
            print(" | ".join(first_row))
        else:
            print("No data rows found in the CSV.")
    else:
        print("The CSV file is empty.")
