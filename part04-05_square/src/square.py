# Copy here code of line function from previous exercise
def line(length, text):
    if text == "":
        text = "*"
    print(text[0] * length)

def square(size, character):
    # You should call function line here with proper parameters
    i = 0
    while i < size:
        line(size, character)
        i +=1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "0")