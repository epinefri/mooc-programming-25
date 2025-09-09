# Write your solution here

def same_chars(text, a, b):
    if b <= len(text)-1 and a <= len(text)-1:
        return text[a] == text[b]
    else:
        return False

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("abc", 0, 3))