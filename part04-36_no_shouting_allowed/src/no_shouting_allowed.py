# Write your solution here

def no_shouting(words :list):
    pruned_list = []
    for word in words:
        if word.isupper() == False:
            pruned_list.append(word)
    return pruned_list

if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)