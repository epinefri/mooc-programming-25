# Write your solution here
list = []
i = 1
while True:
    print(f"The list is now {list}")
    option = input(f"a(d)d, (r)emove or e(x)it:")
    if option == 'x':
        break
    if option == 'd':
        list.append(i)
    if option == 'r':
        list.pop(-1)
        i -= 2
    i += 1
    if list == []:
        i = 1
print("Bye!")
