def add_student(students: dict, student_name: str):
    students[student_name] = []

def print_student(students: dict, student_name: str):
    print(f"{student_name}:")
    if student_name in students.keys():
        if students[student_name]:
            grades = []
            print(f" {len(students[student_name])} completed courses:")
            for course in students[student_name]:
                print("  ", course[0], course[1])
                grades.append(course[1])
            avg_grade = sum(grades) / len(grades)
            print(f" average grade {avg_grade:.1f}")

    else:
        print("no such person in the database")


def add_course(students: dict, student_name: str, courses: tuple):
    if courses[0] in students[student_name]:
        if course[1] 
    students[student_name].append(courses)
    
if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_course(students, "Peter", ("Introduction to Programming", 3))
    add_course(students, "Peter", ("Advanced Course in Programming", 2))
    add_course(students, "Peter", ("Data Structures and Algorithms", 0))
    add_course(students, "Peter", ("Introduction to Programming", 2))
    print_student(students, "Peter")