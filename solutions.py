#Even or Odd Function
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

#Convert a Number to a String Function
def number_to_string(num):
    return str(num)

#Remove String Spaces Function
def no_space(x):
    arr = x.split()
    return "".join(arr)

#Vowel Count Function
def get_count(sentence):
    count = 0
    vowels = 'aeiou'
    for letter in sentence:
        if letter in vowels:
            count += 1
    return count
    


