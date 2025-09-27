#Array101
#Track--> Remove Duplicates from Sorted Array
"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. the relative
order of the elements should be kept the same. Then return the number of unique elements in nums.
Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
1) Change the array nums such that first k elements of nums, contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums
2) Return k
"""




def removeDuplicates(nums):
    k=1
    temp=0
    for i in range(1,len(nums)):
        if nums[i]==nums[temp]:
            pass
        else:
            temp+=1
            nums[temp]=nums[i]
            k+=1
    return k


nums=[0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))