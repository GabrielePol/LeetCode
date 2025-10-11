#Problem 1207- Unique Number of Occurrences
"""
Given an array of integers arr, return True if the number of occurrences of
each value in the array is unique or False otherwise.
"""

arr=[1,2,2,1,1,3]
counter=[]

x=set(arr)


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter=[]
        x=set(arr)
        for elemento in x:
            n=arr.count(elemento)
            if n in counter:
                return False
            else:
                counter.append(n)
        return True