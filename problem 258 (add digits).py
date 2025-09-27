#Problem 258. Add Digits
"""
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
Example--> num= 38
38-->3+8--> 11
11-->1+1-->2
return 2
"""





def addDigits(num):
    x=[int(digit) for digit in str(num)]
    if len(x)<=1:
        return x[0]
    else:
        return addDigits(sum(x))



nums=111

print(addDigits(nums))


