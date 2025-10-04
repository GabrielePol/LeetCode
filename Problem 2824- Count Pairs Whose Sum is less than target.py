#Problem 2824- Count Pairs Whose Sum is Less than Target
"""
Given a 0-indexed integer array nums of length n and an integer target, return the number of pairs (i,j) where 0 <=i < j < n and nums[i]+nums[j < target
"""

nums=[-1,1,2,3,1]
target=2

counter=0
left=0
right=len(nums)-1


nums.sort()


while left<right:
    sum=nums[left]+nums[right]
    if sum>=target:
        right-=1
    else:
        counter+=right-left
        left+=1



print(counter)





-6,2,5,-2,-7,-1,3

-2


-7,-6,-2,-1,2,3,5