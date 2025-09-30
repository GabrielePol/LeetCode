#Problem 1512- Number of Good Pairs
"""
Given an array of integers nums, return the number of good pairs.
A pair (i,j) is called good if nums[i]==nums[j] and i<j
"""


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j] and i < j:
                    counter += 1
                else:
                    pass
        return counter
