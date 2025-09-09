# Copy here code of line function from previous exercise and use it in your solution
def line(length, text):
    if text == "":
        text = "*"
    print(text[0] * length)

def shape(size1, char1, size2, char2):
    i = 1
    while i <= size1:
        line(i, char1)
        i+=1
    i=0
    while i< size2:
        line(size1, char2)
        i+=1
# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")