
def double_items(numbers: list):
    numbers_double = []
    numbers_double [:] = numbers
    for i in range(0,len(numbers)):
        numbers_double[i] = numbers[i]*2
    return numbers_double


if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)