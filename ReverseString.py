#Reverse String
"""
Write a function that reverses a string. The input string is given as an array of character s.
You must do this by modifying the input array in-place with O(1) extra memory.
"""


s=["h","e","l","l","o"]


def reverse_string(a):
   if len(a)<=1:
       return a
   else:
       for i in range(len(a)//2):
           j=len(a)-1-i
           a[i],a[j]=a[j],a[i]
   return a



print(reverse_string(s))




