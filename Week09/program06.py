# Function to count the number of courses for each program
def count_courses_per_program(filename):
    # Dictionary to store course counts for each program
    program_courses = {}

    # Open and read the file
    with open(filename, 'r') as file:
        # Skip the header (Program,Course)
        next(file)

        # Process each line in the file
        for line in file:
            # Strip any extra whitespace and split by comma
            line = line.strip()
            if line:  # Check if line is not empty
                program, course = line.split(',')

                # Count the courses for each program
                if program in program_courses:
                    program_courses[program] += 1
                else:
                    program_courses[program] = 1

    return program_courses

# File path
filename = '.\\3rd-Sem_Lab_Work\\Week09\\6programs_courses.txt'  # Replace with the path to your file

# Call the function
courses_per_program = count_courses_per_program(filename)

# Output the result
for program, count in courses_per_program.items():
    print(f"Program: {program}, Number of courses: {count}")
