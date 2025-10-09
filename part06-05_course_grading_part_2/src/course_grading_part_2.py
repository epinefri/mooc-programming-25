# write your solution here

if False:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_points = input("Exam points: ")
else:
    # hard-coded input
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_points = "exam_points1.csv"

total_points  = {}

print("students_info:")
with open(student_info) as file:
    for line in file:
        parts = line.split(';')
        for part in parts:
            part = part.strip()
            print(part, end = ' ')
        print()

print("____")
print("exercise_data:")
with open(exercise_data) as file:
    for line in file:
        parts = line.split(';')
        for part in parts:
            part = part.strip()
            print(part, end = ' ')
        print()
        
print("____")
print("exam_points:")
with open(exam_points) as file:
    for line in file:
        parts = line.split(';')
        for part in parts:
            part = part.strip()
            print(part, end = ' ')
        print()



