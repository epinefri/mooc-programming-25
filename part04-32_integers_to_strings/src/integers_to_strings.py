# Write your solution here
def formatted(floaties):
    new_floaties = []
    for element in floaties:
        new_floaties.append(f"{element:.2f}")
    return new_floaties


if __name__ == "__main__":
    my_list = [1.234, 0.3333, 0.11111, 3.446]
    new_list = formatted(my_list)
    print(new_list)