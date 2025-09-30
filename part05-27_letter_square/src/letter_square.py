layers = 4 # input("Layers:")

# create list of characters
letters = []
for i in range(layers):
    letters.append(chr(i+65))

# print square
for i in range(layers*2-1): #rows
    for j in range(layers*2-1):
        print(' * ',end='')
    print()


print(letters)