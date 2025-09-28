#Problem 2011- Final Value of Variable After Performing Operations
"""
There is a programming language with only four operations and one variable x:
++x and x++ increments the value of the variable x by 1
--x and x-- decrements the value of the variable x by 1

Initially, the value of x is 0.
Given an array of strings operations containing a list of operations, return the final value of x after performing all the operations.
"""


def finalValueAfterOperations(operations):
    x=0
    for i in range(len(operations)):
        if operations[i]=="++X" or  operations[i]=="X++":
            x+=1
        elif operations[i]=="--X" or operations[i]=="X--":
            x-=1
    return x




operations=["--X","X++","X++"]

print(finalValueAfterOperations(operations))