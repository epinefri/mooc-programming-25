# Write your solution here

def all_the_longest(words):
    length = len(words[0])
    new_words = []
    for word in words:
        if len(word) > length:
            length = len(word)
            new_words = []
            new_words.append(word)
        elif len(word) == length:
            new_words.append(word)
    return new_words

if __name__ == "__main__":
    my_list = ["abc", "cde", "abcd", "fgh", "abcde", "acb", "abbdd"]
    result = all_the_longest(my_list)
    print(result) 