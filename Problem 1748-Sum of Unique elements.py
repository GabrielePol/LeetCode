#Problem 1748- Sum of Unique Elements
"""
You are given an integer array nums. The unique elements of an array are the elements that appear exactly one in the array.
Return the sum of all the unique elements of nums.
"""

nums=[1,2,3,2]
sum=0


for i in range(len(nums)):
    x=nums.count(nums[i])
    if x==1:
        sum+=nums[i]
    else:
        pass
    x=0
print(sum)