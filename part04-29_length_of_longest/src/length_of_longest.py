# Write your solution here
def length_of_longest(a):
    length = 0
    for item in a:
        if len(item) > length:
            length = len(item)
    return length


if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = length_of_longest(my_list)
    print(result)