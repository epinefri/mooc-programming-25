# Write your solution here

def spruce(size):
    print("a spruce!")
    i = 1
    while i <= size:
        print(f"{" "*(size - i)}{"*" * (i * 2 - 1)}")
        i += 1
    print(f"{' '*(size-1)}*")


# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(3)