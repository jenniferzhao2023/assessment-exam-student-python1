"""
Create a function that returns the mean of all digits.

Example:
    mean(42) ➞ 3.0

    mean(12345) ➞ 3.0

    mean(666) ➞ 6.0

Notes:
    - Function should always return float
"""


def mean(digits):
    digits = str(digits)
    sum = 0
    for i in range(len(digits)):
        sum += int(digits[i])
        
    mean = sum / len(digits)
    return mean


print(mean(42)) 

print(mean(12345)) 

print(mean(666)) 