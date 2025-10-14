# tee ratkaisu tänne

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

# student names from student_info files
names = {}
with open(student_info) as file:
    for line in file:
        parts = line.split(";")
        if parts[0] == 'id':
            continue
        names[parts[0]] = f"{parts[1].strip()} {parts[2].strip()}"
print(names)

# number of exercises from exercise_data files
exec_nbr = {}
with open(exercise_data) as file:
    for line in file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        exec_nbr[parts[0]] = 0
        for part in parts[1:]:
            part = int(part.strip())
            exec_nbr[parts[0]] += part
print(exec_nbr)

# exercises points - to be calculated

# exam points from exam_points files
exm_pts = {}
with open(exam_points) as file:
    for line in file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        exm_pts[parts[0]] = 0
        for part in parts[1:]:
            part = int(part.strip())
            exm_pts[parts[0]] += part
print(exm_pts)