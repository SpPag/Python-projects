"""
12.2 Να κατασκευάσετε συνάρτηση isnum() που δέχεται στην είσοδο μια συμβολοσειρά και απαντάει αν είναι αποδεκτός αριθμός
ή όχι. Για παράδειγμα, να αναγνωρίζει το -123.45 ως αριθμό.
"""

"""
def isnum():
    judged = input("\nIs...what, a number?: ").strip()
    if judged.isdigit():
        return True
    if "," in judged:
        judged.replace(",", ".")
    if "." in judged:
        if judged.count(".") == 1:
            judged = judged.replace(".", "")
            if judged.isdigit():
                return True
    if judged[0] in "+-":
        if judged[1:].isdigit():
            return True
    else:
        return False


y_n_answers = ["Y", "Υ", "N", "Ν"]
provide_hint = False
while True:
    stop = ""
    print(isnum())
    while stop not in y_n_answers:
        if provide_hint:
            print("Answer in the form of Y or N")
        stop = input("exit? ").upper()
        provide_hint = True
        if stop in y_n_answers:
            provide_hint = False
    if stop in ("Y", "Υ"):
        break
    elif stop in ("N", "Ν"):
        continue
"""

"""
Η λύση του καθηγητή. Θέτει τιμή στη συνάρτηση με το n και χρησιμοποιεί εντός της συνάρτησης εκφράσεις του τύπου
isnum(n[1:]). Είναι πολύ πιο σέξι από αυτό που έκανα εγώ. Επίσης, είναι μικρότερος ο κώδικας. Το να τρέχει μια
συνάρτηση εντός του εαυτού της, της προσδίδει την ιδιότητα "αναδρομική".
"""


def isnum(n=''):
    if not type(n) is str:
        return False
    print(n)
    n = n.strip()
    if n.isdigit(): 
        return True
    elif n[0] in '+-' and isnum(n[1:]):
        return True
    elif "." in n:
        if n.count(".") <= 1 and isnum(n.replace(".", "")):
            return True
        else:
            return False
    else:
        return False


while True:
    n = input("n=")
    if n == '':
        break
    print(isnum(n))
