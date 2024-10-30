"""
Ζητείται να δημιουργήσετε μια νέα έκδοση της συνάρτησης abs(x) που επιστρέφει την απόλυτη τιμή ενός αριθμού. Να μπορεί
να πάρει και αριθμούς που βρίσκονται σε μορφή αλφαριθμητικών και να επιστρέφει Νone, αν το x δεν είναι αριθμός. Η abs(x)
να αποθηκευτεί σε ένα αρχείο myabs.py το οποίο να εισαγάγετε ως βιβλιοθήκη σε ένα πρόγραμμα που ζητάει αριθμούς από τον
χρήστη και επιστρέφει την απόλυτη τιμή τους.
"""
import z_myabs_for_functions_exercise_6
while True:
    num = input("num: ").strip()
    if num.lower() in "break, exit, n":
        break
    print(f"The number's absolute value is {z_myabs_for_functions_exercise_6.abs(num)}")
