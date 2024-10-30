"""
The OS module and functions allow the user to navigate the computer's files from inside the IDE.
Οι κύριες συναρτήσεις της os είναι:

    os.getcwd() # τρέχων φάκελος
    os.chdir(d) # αλλαγή φακέλου
    os.listdir(d) # περιεχόμενα φακέλου
    os.rename( "t1.txt", "t2.txt" ) # αλλαγή σε όνομα αρχείου
    os.remove(file_name) # διαγραφή αρχείου
    os.mkdir("newdir") # δημιουργία φακέλου
    os.rmdir(dirname) # διαγραφή φακέλου
    os.system(εντολή) # εντολή γραμμής εντολών
    os.walk(d) # διαπέραση του συστήματος αρχείων
    os.sep # διαχωριστικός χαρακτήρας φακέλων (/)*

 Examples:
"""

import os
for x in os.walk(r"D:\Downloads\Stuff To Watch\Keeper Movies"):
    print(x)
    