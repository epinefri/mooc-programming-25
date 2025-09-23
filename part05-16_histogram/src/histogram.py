def histogram(word):
    count = {}
    for letter in word:
        if letter not in count:
            count[letter] = 0
        count[letter] += 1

    for key, value in count.items():
        print(key, "*" * value)

