#LeetCode Array 101
#Max consecutive Ones


nums = [1,0,1,1,1,1,1,0,0,1,1,1,1]

x = 1
score = 0
total_score = 0



for i in range(len(nums)):
    if nums[i]==x:
        score += 1
        if total_score < score:
            total_score = score
    elif nums[i]!=x:
        score = 0

print(total_score)





