if True:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
else:
    # hard-coded input
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"

with open(student_info) as file:
    names = {}
    for line in file:
        parts = line.split(";")
        if parts[0] == 'id':
            continue
        names[parts[0]] = parts[1].strip() + " " + parts[2].strip()

with open(exercise_data) as file:
    exes = {}
    for line in file:
        parts = line.split(";")
        if parts[0] == 'id':
            continue
        exes[parts[0]] = 0
        for element in parts[1:]:
            exes[parts[0]] += int(element)

for id, name in names.items():
    if id in exes:
        print(name, exes[id])
        
