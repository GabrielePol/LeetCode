#Array 101
#Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.



nums = [-4,-1,0,3,5]
nums_1=[]


for i in range(len(nums)):
    x = nums[i]**2
    nums_1.append(x)
    print(nums_1.sort())

print(nums_1)