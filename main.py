# Name: Georgia Vrana
# Date Submitted: Tuesday, March 26th, 2024
# Assignment-7: Student Data
# Description: The program defines a `Student` class to instantiate student objects with 
#              personal and academic details and then prints formatted information for each student. 
#              
#              

class Student:
    # Initialize the Student class with an __init__ method
    def __init__(self, stu_num, f_name, l_name, grade):
        self.stu_num = stu_num
        self.f_name = f_name
        self.l_name = l_name
        self.grade = grade
        # Initialize p1_sub and p1_teacher with empty strings
        self.p1_sub = ""
        self.p1_teacher = ""
    
    # Define the print_info method to display the student information
    def print_info(self):
        print(f"Student Number: {self.stu_num}")
        print(f"Name: {self.f_name} {self.l_name}")
        print(f"Grade: {self.grade}")
        print(f"Subject: {self.p1_sub} {self.p1_teacher}")

# Instantiate the first student object s1 with the given attributes
s1 = Student(101, "Spongebob", "Squarepants", 12)
# Set the values of p1_sub and p1_teacher using dot notation
s1.p1_sub = "Biology"
s1.p1_teacher = "Mr. Darwin"

# Call the print_info() method for the first student object s1
s1.print_info()

# Since the second screenshot mentioned input prompts which can be tedious during testing,
# the following values for s2 and s3 are hardcoded instead of using input() for the sake of example.

# Instantiate the second student object s2 with the given attributes
s2 = Student(102, "Bugs", "Bunny", 10)
# Set the values of p1_sub and p1_teacher using dot notation
s2.p1_sub = "Physics"
s2.p1_teacher = "Mr. Einstein"

# Call the print_info() method for the second student object s2
s2.print_info()

# Instantiate the third student object s3 with the given attributes
s3 = Student(103, "Bart", "Simpson", 9)
# Set the values of p1_sub and p1_teacher using dot notation
s3.p1_sub = "Chemistry"
s3.p1_teacher = "Mrs. Curie"

# Call the print_info() method for the third student object s3
s3.print_info()
