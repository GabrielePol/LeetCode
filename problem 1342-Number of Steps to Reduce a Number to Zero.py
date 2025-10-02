#Problem 1342- Number of Steps to Reduce a Number to Zero
"""
Given an integer num, return the number of steps to reduce it to zero.
In one step, if the current number is even, you have to divide it by 2, otherwise
you have to subtract 1 from it.
"""

class Solution:
    def numberOfSteps(self, num: int) -> int:
        i=False
        x=0
        while i!=True:
            if num==0:
                return 0
            if num%2==0:
                num=num//2
                x+=1
                if num==0:
                    return x
                    i=True
                else:
                    i=False
            else:
                num=num-1
                x+=1
                i=False
                if num==0:
                    return x
                    i=True
                else:
                    i=False
