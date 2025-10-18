#Problem 1979- Find Greatest Common Divisor of Array
"""
Given an integer array nums, return the greatest common divisor of the smallest number and largest number in nums.
The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.
"""

nums=[2,5,6,9,10]
minimum=min(nums)
maximum=max(nums)
greatest=0
counter=0
for i in range(1,maximum+1):
    if minimum%i==0 and maximum%i==0:
        counter=i
        if counter>greatest:
            greatest=counter


print(greatest)