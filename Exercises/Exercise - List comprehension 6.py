"""
Να δημιουργήσετε συνοπτικά μια λίστα με τα γράμματα μιας συμβολοσειράς s.
"""

s = input("Hey just type anything and hit ENTER: ")
s = s.split()
# Πρώτα χωρίς list comprehension
result = []
for char in s:
    for char1 in char:
        if char1.isalpha():
            result.append(char1)
print(result)

# Τώρα με list comprehension
result2 = [char4 for char3 in s for char4 in char3]
print(result2)
