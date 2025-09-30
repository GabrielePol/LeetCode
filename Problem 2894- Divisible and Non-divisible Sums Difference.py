#Problem 2894- Divisible and Non-divisible Sums Difference
"""
You are given positive integers n and m.
Define two integers as follows:
-num1: The sum of all integers in the range [1,n] (both inclusive) that are not divisible by m.
-num2: The sum of all integers in the range [1,n] (both inclusive) that are not divisible by m.

return the integer num1-num2
"""

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1=0
        num2=0
        for i in range(n+1):
            if i%m!=0:
                num1+=i
            elif i%m==0:
                num2+=i
        return num1-num2