# Write your solution here

def no_vowels(text :str):
    consonants_only = ''
    for char in text:
        if char in ('a', 'e', 'i', 'o' ,'u'):
            consonants_only += ''
        else:
            consonants_only += char
            
    return(consonants_only)

if __name__ == "__main__":
    my_string = 'this is an example'
    print(no_vowels(my_string))