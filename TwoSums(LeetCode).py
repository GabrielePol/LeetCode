#LeetCode First Problem --> Two Sum


nums = [1,2,3,4,5]
target = 3


class solution:
    def twoSum(self,nums,target):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if nums[i]+nums[j]==target:
                        return [i,j]