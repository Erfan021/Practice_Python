# White List
# LIST OF GRADUATING STUDENTS

black_list = ['Ali', 'Rehan', 'Sarah', 'Kinza']

num_students = int(input("Enter the number of students: "))
student_list = []
white_list = []

for students in range(num_students):
    prompt = input("Enter the student name: ").capitalize()
    while prompt == '': #if student name is empty
        prompt = input("Enter the non-empty student name: ").capitalize()
    student_list.append(prompt)
    
for student in student_list:
    if student not in black_list:
        white_list.append(student)

print(f"These {str(len(white_list))} students are allowed to graduate", end='\n')
print(*sorted(white_list), sep='\n') #unpacking
