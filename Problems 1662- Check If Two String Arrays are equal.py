#Problems 1662-Check If Two String Arrays are Equivalent
"""
Given two string arrays word1 and word2, return true if the two arrays represent the same string and false otherwise.
A string is represented by an array if the array elements concatenated in order forms the string.
"""

word1=["ab","c"]
word2=["a","b"]
stringa_prova=""

for i in range(len(word1)):
    stringa_prova+=word1[i]
for i in range(len(word2)):
    stringa_prova_2+=word2[i]
if stringa_prova==stringa_prova_2:
    return true
else:
    return false
