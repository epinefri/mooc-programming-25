# Write your solution here
def dict_of_numbers():
    dict = {}
    first_ten = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    teens = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

    for i in range(0,100):
        if i <= 10:
            dict[i] = first_ten[i]
        elif i < 20:
            dict[i] = teens[i - 11]
        elif i < 100:
            if i % 10 == 0:
                dict[i] = tens[int(i/10)-1]
            else:
                dict[i] = tens[int(i/10)-1] + '-' + first_ten[i%10]
    return dict

if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])
    print(numbers)