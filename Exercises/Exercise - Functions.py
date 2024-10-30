"""
12.5 Να κατασκευάσετε συνάρτηση initials(text) που δέχεται ως είσοδο ένα κείμενο και επιστρέφει το κείμενο με το αρχικό
μόνο σύμβολο κάθε λέξης του (πχ αν text = Καλημέρα σας, επιστρέφει Κ. Σ. )
"""


def initials(text):
    textlist = [i for i in text.split()]
    result = ""
    for o in textlist:
        result += o[0].upper() + ". "
    return result


print(initials("τι καλό έχουμε σήμερα;"))
