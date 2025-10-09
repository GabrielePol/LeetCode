#Problem 338-Counting Bits
"""
Given an integer n, return an array ans of length n+1 such that for each i, ans [i] is the number of 1's in the binary representation of i.
"""

n=2
list_binary=[]
for i in range(n+1):
    binary=f"{i:b}"
    counter=binary.count("1")
    list_binary.append(counter)

print(list_binary)