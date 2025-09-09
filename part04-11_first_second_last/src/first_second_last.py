# Write your solution here

def first_word(text):
    end = text.find(" ")
    return text[0:end]

def second_word(text):
    start = text.find(" ") + 1
    if text[start:].find(" ") != -1:
        end = text[start:].find(" ") + start
        return text[start:end]
    else:
        return text[start:]

def last_word(text):
    i = len(text)
    count = 0
    while i > 0:
        if text[i:].find(" ") == 0:
            start = i + 1
            break
        else:
            i -= 1
    return text[start:]
        

# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "hello world"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))