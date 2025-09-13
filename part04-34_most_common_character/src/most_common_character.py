# Write your solution here

def most_common_character(word):
    highest = 1
    most_common = word[0]
    for char in word:
        if word.count(char) > highest:
            highest = word.count(char)
            most_common = char
    return most_common

if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))