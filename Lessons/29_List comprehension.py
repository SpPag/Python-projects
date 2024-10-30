"""
List comprehension is an alternative way of creating lists, that might lead to a much shorter code for more complicated
lists, compared to other methods.
"""

# print any numbers from 1 (including 1) to 20 (including 20) that can be perfectly divided by 2 as well as 3. First,
# do it without list comprehension. Afterwards, do it with list comprehension.

l1 = []
for num in range(1, 21):
    if num % 2 == 0 and num % 3 == 0:
        l1.append(num)
print(l1)

l2 = [num for num in range(1, 21) if num % 2 == 0 and num % 3 == 0]
print(l2)
