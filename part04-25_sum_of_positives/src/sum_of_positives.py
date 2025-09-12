# Write your solution here

def sum_of_positives(list_int :list):
    sum = 0
    for element in list_int:
        if element > 0:
            sum += element
    return sum

if __name__ == "__main__":
    my_list = [1, -2, 3, -4, 5]
    result = sum_of_positives(my_list)
    print("The result is", result)