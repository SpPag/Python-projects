"""
Να δημιουργήσετε μια γεννήτρια τυχαίων ημερομηνιών. Ο χρήστης δίνει το έτος και πόσες ημερομηνίες θέλει και ο
υπολογιστής αποκρίνεται με ημερομηνίες της μορφής 5-ΜΑΙΟΥ-2016 και λίστα από ημερομηνίες της μορφής DD-MM-YYYY
(Παραλλαγή: γεννήτρια μοναδικών ημερομηνιών (no duplicates))
"""
import random
months = """Ιανουάριος (31 ημέρες)
Φεβρουάριος (28 ή 29 ημέρες)
Μάρτιος (31 ημέρες)
Απρίλιος (30 ημέρες)
Μάιος (31 ημέρες)
Ιούνιος (30 ημέρες)
Ιούλιος (31 ημέρες)
Αύγουστος (31 ημέρες)
Σεπτέμβριος (30 ημέρες)
Οκτώβριος (31 ημέρες)
Νοέμβριος (30 ημέρες)
Δεκέμβριος (31 ημέρες)"""

tonoi = {
    "ά": "α",
    "έ": "ε",
    "ή": "η",
    "ί": "ι",
    "ό": "ο",
    "ύ": "υ",
    "ώ": "ω"
}

month_names = [i.split()[0] for i in months.split("\n")]
month_days = [j.split("(")[1][:2] for j in months.split("\n")]
print(month_names)
print(month_days)

year = ""
leap_year = False
number_of_random_days = ""
while not year.isdigit():
    year = input("Έτος: ").strip()
    if year.lower() == "break" or year.lower() == "exit":
        break
if year.isdigit():
    year = int(year)
# Ώρα να ελέγξουμε αν το έτος που έδωσε ο χρήστης είναι δίσεκτο με βάση τον κώδικα που βρήκαμε online
    if year % 4 == 0 and year % 100 != 0:
        leap_year = True
    if year % 400 == 0:
        leap_year = True
    if leap_year:
        month_days[1] = 29
        print(year, " was a leap year.\n", month_days)
    if not leap_year:
        print(year, " was not a leap year.\n", month_days)
while not number_of_random_days.isdigit():
    number_of_random_days = input("How many random days would you like to generate?\n")
    if number_of_random_days.lower() == "break" or number_of_random_days.lower() == "exit":
        break
if number_of_random_days.isdigit():
    number_of_random_days = int(number_of_random_days)
random_days = []
while len(random_days) < number_of_random_days:
    m = random.randint(0, 11)
    random_d = random.randint(1, int(month_days[m]))
    month_me_tonous = month_names[m]
    month_xwris_tonous = ""
    for letter in month_me_tonous:
        if letter in tonoi:
            letter = tonoi[letter]
            month_xwris_tonous += letter
        else:
            month_xwris_tonous += letter
    random_m = month_xwris_tonous
    random_date = f"{random_d:02}-{random_m.replace("ς", "υ").upper()}-{year}"
    random_date2 = f"{random_d:02}-{m+1:02}-{year}"
    if random_date not in random_days:
        random_days.append(random_date)
        print(random_date)
        print(random_date2)
print(random_days)
