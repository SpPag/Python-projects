"""
Create list L with any numbers from 1 (including 1) to 20 (including 20) that are odd, increased by 10
"""
# Odd numbers are 1, 3, 5 etc. How can we code those? What do they have in common? After division by 2 there's always
# a remainder of 1. So prime numbers can be described as a category by numbers that follow: x % 2 == 1.
L = [num+10 for num in range(1, 21) if num % 2 == 1]
print(L)
