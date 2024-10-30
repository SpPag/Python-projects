"""
Αν δίνεται μια λίστα θερμοκρασιών σε κλίμακα Κελσίου και οι αριθμοί είναι χωρισμένοι με κενά, να δημιουργήσετε μια λίστα
f με τις θερμοκρασείς στην Κλίμακα Φαρενάιτ, με συνοπτική παραγωγή λίστας. F = 9/5 * C + 32.
"""
# Πρώτα χωρίς list comprehension to figure it out.
f = []
input_is_incorrect = True
while input_is_incorrect:
    c = input("δώσε μετρήσεις θερμοκρασίας σε βαθμούς Κελσίου για λίστα c: ")
    c = c.split()
    for word in c:
        if not word.isnumeric():
            input_is_incorrect = True
        else:
            input_is_incorrect = False
print("c = ", c)
for temp_text in c:
    temp_number = int(temp_text)
    f.append(temp_number * 9/5 + 32)
print("f = ", f)

# Τώρα με list comprehension
input_is_incorrect = True
while input_is_incorrect:
    c2 = input("δώσε μετρήσεις θερμοκρασίας σε βαθμούς Κελσίου για λίστα c2: ")
    c2 = c2.split()
    for word in c2:
        if not word.isnumeric():
            input_is_incorrect = True
        else:
            input_is_incorrect = False
print("c2 = ", c2)
f2 = [int(temper_number) * 9/5 + 32 for temper_number in c2]
print("f2 = ", f2)
