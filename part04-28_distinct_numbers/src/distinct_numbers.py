# Write your solution here
def distinct_numbers(a):
    a = sorted(a)
    i = 0
    b = []
    for item in a:
        if item not in b:
            b.append(item)
    
    return b

if __name__ == "__main__":
    my_list = [1, 10, 100,1000, 1, 10, 100]
    print(distinct_numbers(my_list))