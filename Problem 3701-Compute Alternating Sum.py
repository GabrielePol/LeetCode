#Problem 3701-Compute Alternating Sum
"""
You are given an integer array nums.
The alternating sum of nums is the value obtained by adding elements at even
indices and subtracting elements at odd indices.
"""

nums=[1,3,5,7]

sum_even=0
sum_odd=0

for i in range(len(nums)):
    if i%2==0:
        sum_even+=nums[i]
    else:
        sum_odd+=nums[i]

print(sum_even-sum_odd)