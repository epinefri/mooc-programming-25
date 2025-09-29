def add_student(students: dict, student_name: str):
    students[student_name] = []

def print_student(students: dict, student_name: str):
    if student_name in students.keys():
        print(f"{student_name}:")
        if students[student_name] == []:
            print(" no completed courses")
        if students[student_name]:
            grades = []
            print(f" {len(students[student_name])} completed courses:")
            for course in students[student_name]:
                print(" ", course[0], course[1])
                grades.append(course[1])
            avg_grade = sum(grades) / len(grades)
            print(f" average grade {avg_grade:.1f}")

    else:
        print(f"{student_name}: no such person in the database")


def add_course(students: dict, student_name: str, course: tuple):
    repeated = 0
    passed = 1
    i = 0
    for entry in students[student_name]:
        if course[0] == entry[0] and course[1] > entry[1]:
            repeated = 1
            students[student_name][i] = course
        i +=1
    if not repeated and passed:
        if course[1] > 0:
            students[student_name].append(course)
         
def summary(students):
    students_count = len(students)
    print("students",students_count)
    
    most_students = 0
    most_courses_stud = 0
    for student, courses in students.items():
        if len(courses) > most_students:
            most_students = len(courses)
            most_courses_stud = student
    print("most coursed completed", most_students, most_courses_stud)

    averages = {}
    best_avg = 0
    best_stud = ''
    for student_name, courses in students.items():
        averages[student_name] = 0
        for course in courses:
            averages[student_name] += course[1]
        averages[student_name] /= len(courses)

        if averages[student_name] > best_avg:
            best_avg = averages[student_name]
            best_stud = student_name

    print("best average grade", best_avg, best_stud)
    
if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_course(students, "Peter", ("Software Development Methods", 5))
    add_course(students, "Peter", ("Software Development Methods", 1))
    print_student(students, "Peter")




   