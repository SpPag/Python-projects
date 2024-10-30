"""
Να κατασκευάσετε πρόγραμμα που ζητάει διαδοχικά από τον χρήστη την ακτίνα σφαίρας και υπολογίζει, καλώντας σχετικές
συναρτήσεις, την επιφάνεια και τον όγκο της. Το πρόγραμμα τερματίζει όταν ο χρήστης δώσει stop. Καλό είναι να ελέγξουμε
ότι το input του χρήστη είναι κατάλληλο. Μπορούμε να χρησιμοποιήσουμε τη συνάρτηση isnum(n) που κατασκευάσαμε για την
άσκηση 2.
"""
from z_exercise_2_function_to_import import isnum
import math
pi = math.pi


def area(r):
    area = 4 * pi * r ** 2
    return area


def vol(r):
    vol = 4 / 3 * pi * r ** 3
    return vol


while True:
    r = input("sphere radius r = ")
    if r.lower() == "stop":
        break
    if isnum(r):
        print(f"Το εμβαδόν της σφαίρας είναι ίσο με {area(float(r)):.2f} και ο όγκος της είναι ίσος με "
              f"{vol(float(r)):.2f}")
    else:
        continue
