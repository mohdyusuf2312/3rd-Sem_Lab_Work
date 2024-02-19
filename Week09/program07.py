import csv

# Function to add HRA column to the file
def add_hra_to_file(filename):
    # List to store updated rows with HRA
    updated_rows = []

    # Open the file for reading
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        
        # Get the header
        header = next(reader)
        header.append('HRA')  # Add the HRA column
        
        # Add updated header to the updated_rows list
        updated_rows.append(header)
        
        # Process each row in the file
        for row in reader:
            name, emp_id, salary, dname = row
            salary = float(salary)  # Convert salary to a float
            hra = 0.18 * salary  # Calculate HRA (18% of salary)
            row.append(f'{hra:.2f}')  # Append HRA to the row (formatted to 2 decimal places)
            updated_rows.append(row)

    # Open the file again for writing the updated data (including HRA column)
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(updated_rows)

# File path
filename = '.\\3rd-Sem_Lab_Work\\Week09\\7employees.csv'  # Replace with the path to your file

# Call the function to add HRA to the file
add_hra_to_file(filename)

print(f"HRA column has been added to the file '{filename}'")
