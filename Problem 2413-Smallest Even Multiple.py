#Problem 2413- Smallest Even Multiple
"""
Given a positive integer n, return the smallest positive integer that is a multiple of both 2 and n.
"""

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        i=False
        counter=n
        while i!=True:
            if counter%counter==0 and counter%2==0:
                i=True
                return counter
            elif (counter*2)%2==0:
                i=True
                return counter*2
            else:
                counter+=1
                i=False
