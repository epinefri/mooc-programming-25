# Write your solution here
number = int(input("How many items:"))
i = 0
list = []
while i < number:
    list.append(int(input(f"Item {i+1}:")))
    i += 1

print(list)