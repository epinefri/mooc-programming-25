# Write your solution 

def get_input():
    while True:
        points_exercises = input("Exam points and exercises completed: ")
        return(points_exercises)

def main():
    # input values and splitting them into points and exercises
    points = []
    exercises = []
    while True:
        pt_ex = get_input()
        if pt_ex == '':
            break
        else:
            split_list = pt_ex.split()
            pts = int(split_list[0])
            exs = int(split_list[1])

            points.append(pts)
            exercises.append(exs)
            
    
    # convert exercises into exercise points
    total_points = sum(points) + sum(exercises) // 10
    points_avg = total_points / len(points)

    # passed percentage
    passed = 0
    for grade in points:
        if grade >= 10 and total_points > 14:
           passed += 1
    passed_percentage = passed/len(points)*100

    print("Statistics:" ) 
    print(f"Points average: {points_avg:.1f}")
    print(f"Pass percentage: {passed_percentage:.1f}")
    print("Grade distribution:")
    print(f"{"5:":>3} {"*"*3:<5}")
    print(f"{"4:":>3} {"*"*1:<5}")
    print(f"{"3:":>3} {"*"*5:<5}")
    print(f"{"2:":>3} {"*"*2:<5}")
    print(f"{"1:":>3} {"*"*0:<5}")
    print(f"{"0:":>3} {"*"*0:<5}")


main()
