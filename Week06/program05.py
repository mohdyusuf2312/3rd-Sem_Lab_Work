'''
Write a program to get roll numbers, names and marks of the students of a class 
(get from user) and store these details in a file called “Marks.data”
'''

# Function to collect student data and write it to the file
def collect_student_data(filename):
    # Open the file in write mode
    with open(filename, "w") as file:
        # Get the number of students
        num_students = int(input("Enter the number of students: "))
        
        # Loop to get details of each student
        for i in range(num_students):
            print(f"\nEnter details for student {i+1}:")
            roll_no = input("Enter Roll Number: ")
            name = input("Enter Name: ")
            marks = input("Enter Marks: ")
            
            # Write the student details into the file
            file.write(f"Roll No: {roll_no}, Name: {name}, Marks: {marks}\n")
            
    print(f"\nData has been written to {filename}")

# Call the function to collect data
collect_student_data("Marks.data")
