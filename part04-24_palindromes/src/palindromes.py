# Write your solution here
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!

def palindromes(word: str):
    return word == ''.join(reversed(word))
            
        
while True:
    input_word = input("Please type in a palindrome:")
    if palindromes(input_word) == False :
        print("that wasn't a palindrome")
    else:
        print(f"{input_word} is a palindrome!")
        break