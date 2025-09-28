#Problem 2942- Find Words Containing Character
"""
You are given a 0-indexed array of strings words and a character x.
Return an array of indices representing the words that contain the character x.
Note that the returned array may be in any order.
"""


def findWordsContaining(words,x):
    counter=[]
    for i in range(len(words)):
        if x in words[i]:
            counter.append(i)
    return counter



words=["leet","code"]


print(findWordsContaining(words,"e"))