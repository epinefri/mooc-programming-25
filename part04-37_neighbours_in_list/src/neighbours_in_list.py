# Write your solution here

def longest_series_of_neighbours(list_of_numbers):
    previous = list_of_numbers[0]
    count = 1
    list_counts = []
    for element in list_of_numbers[1:]:
        if element - previous in (-1, 1):
            count += 1
        else:
            count = 1
        if count not in list_counts:
            list_counts.append(count)
        previous = element
    if list_counts == []:
        return 1
    else:
        return(max(list_counts))
     



if __name__ == "__main__":
    my_list = [1, 3, 5, 7, 10, 11, 14, 15, 19, 20, 21, 22, 23, 24, 25]
    print(longest_series_of_neighbours(my_list))