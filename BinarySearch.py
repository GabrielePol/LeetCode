#Binary Search

"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums.
If target exists, then return its index. Otherwise, return -1
"""


nums=[1,2,3,4,5,6,7,8,9,10]

def binary_search(a,target):
    if len(a)==0:
        return None
    left=0
    right=len(a)-1
    while left<=right:
        m = (left + right) // 2
        if target==a[m]:
            return m
        elif target<a[m]:
            right=m-1
        else:
            left=m+1
    return -1









print(binary_search(nums,10))