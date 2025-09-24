# Write your solution here

phone_book = {}

while True:
    command = int(input("command (1 search, 2 add, 3 quit):"))
    if command == 3:
        print("quitting...")
        break

    if command == 1:
        searched_name = input("name:")
        if searched_name not in phone_book:
            print("no number")
            continue
        number = print(phone_book[searched_name])

    if command == 2:
        name = input("name:")
        number = input("number:")
        phone_book[name] = number
        print("ok!")
    

