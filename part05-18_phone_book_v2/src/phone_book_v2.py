# Write your solution here

phone_book = {}
command = 0


while True:

    if command == 3:
        print("quitting...")
        break
    
    command = int(input("command (1 search, 2 add, 3 quit):"))
    
    if command == 1:
        name = input("name:")
        if name not in phone_book:
            print('no number')
            continue
        for number in phone_book[name]:
            print(number)

    if command == 2:
        name = input("name:")
        number_input = input("number:")
        if name not in phone_book:
            phone_book[name] = []
        phone_book[name].append(number_input)
        print("ok!")
        continue
