list = []
count = 0
while True:
    word = input("Word:")
    if word in list:
        break
    count += 1
    list.append(word)


print(f"You typed in {count} different words")

