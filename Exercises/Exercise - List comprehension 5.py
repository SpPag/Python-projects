"""
Να δημιουργήσετε συνοπτικά μια λίστα με τους θετικούς αριθμούς μέχρι το 100 που διαιρούνται με 5 και 8.
"""
# Πρώτα χωρίς list comprehension.
result = []
for num in range(1, 100):
    if num % 5 == 0 and num % 8 == 0:
        result.append(num)
print(result)

# Τώρα με list comprehension.
result2 = [num2 for num2 in range(1, 100) if num2 % 5 == 0 and num2 % 8 == 0]
print(result2)
