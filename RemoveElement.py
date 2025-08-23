#Array101
#Track:
"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

    Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
    Return k.
"""

nums = [2]
val=3
k=0

for i in nums:
    while val in nums:
        nums.remove(val)
        k=len(nums)
    k=len(nums)


print(k)