"""
Write a function that takes a string and calculates the number of letters and digits within it. Return the result in a dictionary.

Examples:
    count_all("Hello World") ➞ { "LETTERS":  10, "DIGITS": 0 }

    count_all("H3ll0 Wor1d") ➞ { "LETTERS":  7, "DIGITS": 3 }

    count_all("149990") ➞ { "LETTERS": 0, "DIGITS": 6 }

Notes:
    - Tests contain only alphanumeric characters.
    - Spaces are not letters.
    - All tests contain valid strings.
    - The function should return dictionary

"""

def count_all(string):
    LETTERS = 0
    DIGITS = 0
    for i in range(len(string)):
        if string[i].isalpha
        ():
            LETTERS += 1
        if string[i].isdigit():
            DIGITS += 1
    return {"LETTERS": LETTERS, "DIGITS": DIGITS}

print(count_all("Hello World"))
print(count_all("H3ll0 Wor1d")) 
print(count_all("149990")) 