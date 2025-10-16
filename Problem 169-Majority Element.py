#Problem 169-Majority Element
"""
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than [n/2]times. You
may assume that the majority element in the array.
"""


from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        frequencies=Counter(nums)
        for key in frequencies:
            if frequencies[key]>len(nums)//2:
                return key
