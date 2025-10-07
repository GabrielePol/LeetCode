#Array101
#Find All Numbers Disappeared in an Array
"""
Given an array nums of n integers where nums[i] is in the range [1,n], return
an array of all the integers in the range [1,n] that do not appear in nums.
"""
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_expected=set(range(1,len(nums)+1))
        nums_new=set(nums)
        dis_nums=nums_expected-nums_new
        return list(dis_nums)