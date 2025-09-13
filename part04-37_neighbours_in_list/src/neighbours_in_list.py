# Write your solution here

def longest_series_of_neighbours(list_of_numbers):
    neighbours = []
    count_neighbours = 0
    for element in list_of_numbers:
        for next_element in list_of_numbers[1:]:
            if next_element - element == 1:
                count_neighbours += 1
                print(element, "->", next_element, "#" , count_neighbours)
            else:
                count_
    return count_neighbours



if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6]#, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))