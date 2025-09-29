#Problem 1431- Kids with the Greatest Number of Candies
"""
There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the i^th kid has, and an integer extraCandies,
denoting the number of extra candies that you have.
Return a boolean array result of length n, where result[i] is true if, after giving the i^th kid all the extraCandies, they will have the greates number of candies among all the kids, or false otherwise.
Note that multiple kids can have the greatest number of candies.
"""

candies=[2,8,7]
extraCandies=1
result=[]

max=0
for i in range(len(candies)):
    if candies[i]>max:
        max=candies[i]
    else:
        pass
for i in range(len(candies)):
    if candies[i]+extraCandies>=max:
        result.append(True)
    else:
        result.append(False)

print(result)