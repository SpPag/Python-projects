# This Python file uses the following encoding: utf-8
import calendar

c = calendar.calendar(1821)
print(c)

"""
for line in c.split("\n"):
    print(line)

Ο κύριος Νικόλαος Αβούρης στο mathesis χωρίζει το άνω αντικείμενο σε lines. Δεν εξηγεί γιατί και δεν δείχνει
ότι και να μην το κάνει, το print, θα μας δώσει ΑΚΡΙΒΩΣ το ίδιο αποτέλεσμα. Επειδή πρέπει να εκφράσω αυτό μου το
frustration το γράφω εδώ. Αυτά. Πάμε παρακάτω.
"""

"""
Άσκηση 17.2: Να ζητείται από τον χρήστη έτος, για να του προβληθεί το αντίστοιχο ετήσιο ημερολόγιο μέχρι να δώσει
κενό ως απάντηση, στην οποία περίπτωση να σταματήσει το πρόγραμμα. Με επιλογή του χρήστη να τυπώνει το ημερολόγιο είτε
στα αγγλικά, όπως κάνει αρχικά το calendar module, είτε στα ελληνικά (με δικές μας πράξεις θα γίνει η μετάφραση). 
"""

months_en_pre = "January, February, March, April, May, June, July, August, September, October, November, December"
months_gr_pre = ("Ιανουάριος, Φεβρουάριος, Μάρτιος, Απρίλιος, Μάιος, Ιούνιος, Ιούλιος, Αύγουστος, Σεπτέμβριος,"
                 "Οκτώβριος, Νοέμβριος, Δεκέμβριος")
months_en = months_en_pre.replace(" ", "").split(",")
months_gr = months_gr_pre.replace(" ", "").split(",")
days_en_pre = "Mo, Tu, We, Th, Fr, Sa, Su"
days_gr_pre = "Δε, Τρ, Τε, Πε, Πα, Σα, Κυ"
days_en = days_en_pre.replace(" ", "").split(",")
days_gr = days_gr_pre.replace(" ", "").split(",")

while True:
    year = input("Ποιού έτους θα θέλατε να δείτε το ημερολόγιο; (πατήστε μονάχα ENTER για έξοδο)\n")
    if year == "":
        break
    try:
        year = int(year)
    except ValueError:
        print("Παρακαλώ δώστε ακέραιο αριθμό.")
        continue
    requested_calendar = calendar.calendar(year)
    language = ""
    while language != "1" and language != "2":
        language = input("enter 1 for English or 2 for Greek: ")
    if language == "1":  # so English
        with open(str(year) + "_en.txt", "w") as calendar_in_english:
            calendar_in_english.write(requested_calendar)
        print(requested_calendar, f"\nHere is {year}'s calendar.\n")
    if language == "2":  # so Greek
        for i in range(12):  # όλο αυτό με τα len είναι για να είναι στο κέντρο πάνω από τον κάθε μήνα το όνομα του μήνα
            if len(months_en[i]) < len(months_gr[i]):  # και να μην έχει σπρωχθεί προς τα δεξιά λόγω μεγαλύτερων λέξεων
                spaces = len(months_gr[i]) - len(months_en[i])
                requested_calendar = requested_calendar.replace(spaces * " " + months_en[i], months_gr[i])
            elif len(months_en[i]) > len(months_gr[i]):
                spaces = len(months_en[i]) - len(months_gr[i])
                requested_calendar = requested_calendar.replace(months_en[i], spaces * " " + months_gr[i])
            elif len(months_en[i]) == len(months_gr):
                requested_calendar = requested_calendar.replace(months_en[i], months_gr[i])
        for j in range(7):
            requested_calendar = requested_calendar.replace(days_en[j], days_gr[j])
        # Μια καλύτερη ιδέα για τη μετάφραση των ημερών είναι:
        # requested_calendar = requested_calendar.replace("Mo Tu We Th Fr Sa Su", "Δε Τρ Τε Πε Πα Σα Κυ")
        with open(str(year) + "_gr.txt", "w") as calendar_in_greek:
            calendar_in_greek.write(requested_calendar)
        print(requested_calendar, f"\nΟρίστε το ημερολόγιο του έτους {year}.\n")
