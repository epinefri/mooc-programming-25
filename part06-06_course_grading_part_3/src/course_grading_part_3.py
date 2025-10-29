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
print("\n names:", names)

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
print("\n exer num:", exec_nbr)

# exercises points - to be calculated
exec_pts = {}
for student, number_ex in exec_nbr.items():
    exec_pts[student] = number_ex//4
print("\n exerc points:", exec_pts)
"""
    10% -> 1 point  = 4 exercises
    20% -> 2 points = 8 exercises
    30      3         12
    40      4         16
    50% -> 5 points = 20 exercises
    60% -> 6 points = 24
    70     7          28
    80     8          32
    90     9          36
    100 -> 10 points = 40 exercises
"""


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
print("\n exam points:", exm_pts)

# total points
tot_pts = {}
for student, points in exec_pts.items():
    tot_pts[student] = points
for student, points in exm_pts.items():
    tot_pts[student] += points
print("\n total:", tot_pts)


print("\n")