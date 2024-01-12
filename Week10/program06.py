import csv

# Define file paths
employee_file = '.\\3rd-Sem_Lab_Work\\Week10\\employee.txt'
department_file = '.\\3rd-Sem_Lab_Work\\Week10\\department.txt'
output_file = '.\\3rd-Sem_Lab_Work\\Week10\\Emp_Dep.txt'

# Load department data into a dictionary for fast lookup
def load_departments(file_path):
    departments = {}
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Store each department row in a dictionary with DID as the key
            departments[row['DID']] = row
    return departments

# Merge employee and department data based on DID
def merge_files(employee_file, department_file, output_file):
    departments = load_departments(department_file)
    
    with open(employee_file, mode='r') as emp_file, open(output_file, mode='w', newline='') as out_file:
        emp_reader = csv.DictReader(emp_file)
        
        # Define the output file header
        fieldnames = ['Ename', 'EId', 'Esalary', 'EDID', 'DName', 'DLocation']
        writer = csv.DictWriter(out_file, fieldnames=fieldnames)
        writer.writeheader()
        
        # Read employee records and merge with department data
        for emp_row in emp_reader:
            dept_row = departments.get(emp_row['DID'])
            if dept_row:
                # Combine data from both employee and department records
                merged_row = {
                    'Ename': emp_row['Name'],
                    'EId': emp_row['EId'],
                    'Esalary': emp_row['Salary'],
                    'EDID': emp_row['DID'],
                    'DName': dept_row['DName'],
                    'DLocation': dept_row['DLocation']
                }
                writer.writerow(merged_row)
    print(f"Merged data written to {output_file}")

# Run the merge function
merge_files(employee_file, department_file, output_file)
