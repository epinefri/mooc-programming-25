# Write your solution here
def shortest(list_strings):
    shortest_len = len(list_strings[0])
    shortest = list_strings[0]
    for element in list_strings:
        if shortest_len > len(element):
            shortest_len = len(element)
            shortest = element
    return shortest

if __name__ == "__main__":
    my_list = ['Seraenina', 'Gandalf', 'Harry', 'Walter']
    result = shortest(my_list)
    print(result)