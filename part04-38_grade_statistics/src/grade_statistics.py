# Write your solution 

def get_input():
    while True:
        points_exercises = input("Exam points and exercises completed: ")
        return(points_exercises)


# input values and splitting them into points and exercises
points = []
exercises = []
gradebook = []
while True:
    raw_input = get_input()
    if raw_input == '':
        break
    else:
        split_list = raw_input.split()
        pts = int(split_list[0])
        exs = int(split_list[1])

        points.append(pts)
        exercises.append(exs)
        gradebook.append(raw_input)

# points average
total_ex = 0
for value in exercises:
    total_ex += value // 10
total_points = sum(points) + total_ex
points_avg = total_points / len(points)

# passed percentage 
passed = 0
for student in gradebook:
    gradebook_split = student.split()
    grade = int(gradebook_split[0])
    extra = int(gradebook_split[1])
    if grade >= 10 and grade+extra//10 > 14:
        passed += 1
passed_percentage = passed / len(points) * 100

# grade distribution
count = [0,0,0,0,0,0]
for student in gradebook:
    gradebook_split = student.split()
    grade = int(gradebook_split[0])
    extra = int(gradebook_split[1])
    total = grade+extra//10
    if 0 <= total <= 14 or grade < 10:
        count[0] += 1
    elif 15 <= total <= 17:
        count[1] += 1
    elif 18 <= total <= 20:
        count[2] += 1
    elif 21 <= total <= 23:
        count[3] += 1
    elif 24 <= total <= 27:
        count[4] += 1
    elif 28 <= total <= 30:
        count[5] += 1

print("Statistics:" ) 
print(f"Points average: {points_avg:.1f}")
print(f"Pass percentage: {passed_percentage:.1f}")
print("Grade distribution:")
i = 5
while i >= 0:
    print(f"{i:>3}: {"*"*count[i]:<5}")
    i -= 1

