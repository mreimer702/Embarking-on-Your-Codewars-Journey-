# Python Utility Functions

This repository contains four simple Python functions.

## Functions

### 1. Even or Odd Function
Determines if a given number is even or odd.

```python
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
```

### 2. Convert a Number to a String Function
Converts an integer to a string.

```python
def number_to_string(num):
    return str(num)
```

### 3. Remove String Spaces Function
Removes all spaces from a given string.

```python
def no_space(x):
    arr = x.split()
    return "".join(arr)
```

### 4. Vowel Count Function
Counts the number of vowels (a, e, i, o, u) in a given sentence.

```python
def get_count(sentence):
    count = 0
    vowels = 'aeiou'
    for letter in sentence:
        if letter in vowels:
            count += 1
    return count
```

## Usage
Clone the repository and import the functions into your Python script to use them.

```sh
git clone https://github.com/yourusername/python-utility-functions.git
cd python-utility-functions
```

Use the functions in your Python script:

```python
from utility_functions import even_or_odd, number_to_string, no_space, get_count

print(even_or_odd(4))  # Output: Even
print(number_to_string(123))  # Output: "123"
print(no_space("Hello World"))
