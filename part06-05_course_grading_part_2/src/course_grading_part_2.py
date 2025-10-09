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
        if parts[0] == 'id':
            continue
        total_points[parts[0]] = 0

        for part in parts[1:]:
            part = int(part.strip())
            total_points[parts[0]] += part

    for id in total_points:
        total_points[id] = total_points[id] // 4

    print(total_points)
    print()
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


print("____")
print("exam_points:")
with open(exam_points) as file:
    for line in file:
        parts = line.split(';')
        if parts[0] == "id":
            continue  
        for part in parts[1:]:
            part = part.strip()
            total_points[parts[0]] += int(part)
    print(total_points)
    print()

for id, grade in total_points.items():
    if grade <= 14:
        total_points[id] = 0
    elif grade <= 17:
        total_points[id] = 1
    elif grade <= 20:
        total_points[id] = 2
    elif grade <= 23:
        total_points[id] = 3
    elif grade <= 27:
        total_points[id] = 4
    else:
        total_points[id] = 5

print(total_points)


