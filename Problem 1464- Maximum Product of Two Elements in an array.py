#Problem 1464-Maximum Product of Two Elements in an array
"""
Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1)
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maximum=max(nums)
        nums.remove(maximum)
        maximum_2=max(nums)
        return((maximum-1)*(maximum_2-1)