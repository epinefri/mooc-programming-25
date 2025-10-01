# write your solution here
def largest():
    with open("numbers.txt") as num_file:
        bigest = 0
        for number in num_file:
            if int(number) > bigest:
                bigest = int(number)
    return bigest

