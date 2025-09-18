# Write your solution here

def remove_smallest(numbers: list):
    tiny = min(numbers)
    numbers.remove(tiny)

if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)


#[2, 4, 6, 3, 5]