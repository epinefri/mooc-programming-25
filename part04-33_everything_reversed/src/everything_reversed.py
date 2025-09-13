# Write your solution here

def everything_reversed(words):
    new_words = []
    for element in words[::-1]:
        new_words.append(element[::-1])
    return new_words

if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)