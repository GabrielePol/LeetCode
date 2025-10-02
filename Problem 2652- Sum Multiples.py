#Problem 2652- Sum Multiples
"""
Given a positive integer n, find the sum of all integers in the range [1,n] inclusive that are divisible by 3,5, or 7.
Return an integer denoting the sum of all numbers in the given range satisfying the constraint.
"""
i=1
sum=0
n=7
while i <= n:
    if i%3==0 or i%5==0 or i%7==0:
        sum+=i
        i+=1
    else:
        i+=1

print(sum)