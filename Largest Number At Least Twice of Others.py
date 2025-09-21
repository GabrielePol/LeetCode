#Track
#Largest Number At Least Twice of Others
"""
You are given an integer array nums where the largest integer is unique.
Determine whether the largest element in the array is at least twice as much as every other number in the array.
If it is, return the index of the largest element, or return -1 otherwise
"""





nums=[1,20,3,0]
nums_temporary=[]
counter=1


max=nums[0]
for i in range(len(nums)):
    if nums[i]>max:
        max=nums[i]
for i in range(len(nums)):
    if nums[i]!=max:
        nums_temporary.append(nums[i])
for i in range(len(nums_temporary)):
    if nums_temporary[i]!=0:
        if max//nums_temporary[i]>=2:
            counter+=1
    else:
        counter+=1
if counter==len(nums):
    print(nums.index(max))
else:
    print("-1")
