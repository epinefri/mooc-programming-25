# Write your solution here

phone_book = {"mary": 123, "john": 456}
while True:
    command = int(input("command (1 search, 2 add, 3 quit):"))
    if command == 3:
        print("quitting...")
        break

    if command == 1:
        searched_name = input("name:")
        if searched_name not in phone_book:
            print("no number")
            break
        number = print("number:", phone_book[searched_name])

    if command == 2:
        input("name:")
        input("number:")
        print("ok!")
    


