# Write your solution 

def get_input():
    while True:
        points_exercises = input("Exam points and exercises completed: ")
        if points_exercises == '':
            break
        split_list = points_exercises.split()
        points = int(split_list[0])
        exercises = int(split_list[1])
        print(points, exercises)


def main():
    get_input()

main()
