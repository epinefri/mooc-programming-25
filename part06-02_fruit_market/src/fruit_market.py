# write your solution here
def read_fruits():
    with open("fruits.csv") as fruit_file:
        fruits = {}
        for line in fruit_file:
            line = line.replace("\n", "")
            fruit = line.split(';')
            fruits[fruit[0]] = float(fruit[1])
    return fruits

