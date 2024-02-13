'''
Consider two files that contain information about Employees and Departments in the 
following parameters: Employee (Name, EId, Salary, DID), Department (DID, 
DName, DLocation). Write a Python program to find the average salary of each 
department. 
'''
# Define the employee and department data
employees = [
    {'Name': 'John', 'EId': 101, 'Salary': 50000, 'DID': 1},
    {'Name': 'Jane', 'EId': 102, 'Salary': 60000, 'DID': 1},
    {'Name': 'Alice', 'EId': 103, 'Salary': 70000, 'DID': 2},
    {'Name': 'Bob', 'EId': 104, 'Salary': 55000, 'DID': 2},
    {'Name': 'Charlie', 'EId': 105, 'Salary': 45000, 'DID': 3},
]

departments = [
    {'DID': 1, 'DName': 'HR', 'DLocation': 'New York'},
    {'DID': 2, 'DName': 'Engineering', 'DLocation': 'San Francisco'},
    {'DID': 3, 'DName': 'Marketing', 'DLocation': 'Chicago'},
]

# Dictionary to store the total salary and employee count for each department
dept_salaries = {}

# Loop through employees and aggregate salary information by department
for emp in employees:
    did = emp['DID']
    salary = emp['Salary']
    
    # Initialize if department is not yet in the dictionary
    if did not in dept_salaries:
        dept_salaries[did] = {'total_salary': 0, 'employee_count': 0}
    
    # Accumulate salary and employee count
    dept_salaries[did]['total_salary'] += salary
    dept_salaries[did]['employee_count'] += 1

# Calculate and display the average salary for each department
print("Average salary by department:")
for dept in departments:
    did = dept['DID']
    dname = dept['DName']
    
    if did in dept_salaries:
        total_salary = dept_salaries[did]['total_salary']
        employee_count = dept_salaries[did]['employee_count']
        average_salary = total_salary / employee_count
        print(f"Department: {dname}, Average Salary: ${average_salary:.2f}")
