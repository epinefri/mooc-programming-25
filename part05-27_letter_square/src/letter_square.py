layers = 3# int(input("Layers:"))

# create list of characters
letters = []
for i in range(layers):
    letters.append(chr(i+65))

# print square
for i in range(layers):
    for j in range(layers-1, -1, -1):
        print(letters[j],end='')
    for k in range(1,layers):
        print(letters[k], end='')
    print()

    

"""
CCCCC
CBBBC
CBABC
CBBBC
CCCCC

22222
21112
21012


"""