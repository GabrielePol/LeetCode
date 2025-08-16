#Array 101
# Given an array nums of integers, return how many of them contain an even number of digits.



nums = [555,901,482,5,60,61]
nums_1=[]
counter= 0

for i in range(len(nums)):
    nums_1.append(list(str(nums[i])))
for j in range(len(nums_1)):
    if len(nums_1[j])%2==0:
        counter += 1



print(counter)


