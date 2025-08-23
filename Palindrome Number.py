#Palindrome problem

#Track: Given an integer x, return true if x is a palindrome, and false otherwise


x= 100021
x=list(str(x))
index=0
z=0 #Palindrome counter
x_score=0


for i in range(len(x)-1,-1,-1):
    x_score+=1
    if x[i]==x[index]:
        z+=1
        index+=1
    if x_score==len(x):
        if z==x_score:
            print("è palindromo")
        else:
            print("Non è palindromo")