#Problem 1816-Truncate Sentence
"""
A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
Each of the words consists of only uppercase and lowercase English letters (no punctuation).
"""

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s=s.split(" ")
        new_string=[]
        for i in range(k):
            new_string.append(s[i])
        new_string=" ".join(new_string)
        return new_string





