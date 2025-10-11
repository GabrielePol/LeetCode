#Problem 2427-Number of Common Factors
"""
Given two positive integers a and b, return the number of common factors of a and b.
An integer x is a common factor of a and b if x divides both a and b.
"""


class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        x = 1
        counter = 0
        if a > b:
            while x <= b:
                if b % x == 0 and a % x == 0:
                    counter += 1
                    x += 1
                else:
                    x += 1
                    pass
        elif b > a:
            while x <= a:
                if b % x == 0 and a % x == 0:
                    counter += 1
                    x += 1
                else:
                    x += 1
                    pass
        else:
            while x <= a:
                if b % x == 0 and a % x == 0:
                    counter += 1
                    x += 1
                else:
                    x += 1

        return counter