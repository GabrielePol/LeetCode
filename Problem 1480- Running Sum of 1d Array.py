#Problem 1480- Running Sum of 1d Array
"""
Given an array nums. We define a running sum of an array as runningSum[i]= sum (nums[0]...nums[i])
"""

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        maximum=0
        for i in range(len(nums)):
            maximum+=nums[i]
            nums[i]=maximum
        return nums