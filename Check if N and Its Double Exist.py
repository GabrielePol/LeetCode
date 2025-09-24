#Array101
#Check if N and Its Double Exist
"""
Given an array arr of integers, check if there exist two indices i and j such that:

"""

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i]==2*arr[j] and i!=j:
                    return True
        return False
