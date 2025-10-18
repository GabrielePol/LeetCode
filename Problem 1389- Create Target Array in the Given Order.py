#Problem 1389- Create Target Array in the Given Order
"""
Given two arrays of integers nums and index. Your task is to create target array under the following rules:
1) Initially target array is empty
2) From left to right read nums[i], insert at index index[i] the value nums[i] in target array.
3) Repeat the previous step until there are no elements to read in nums and index.
Return the target array.
It is guaranteed that the insertion operations will be valid.
"""
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target=[]
        for i in range(len(index)):
            target.insert(index[i],nums[i])
        return target 