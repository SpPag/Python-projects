character_name = input("enter the name of your character: ")
character_class = input("enter your character's class: ")
character_level = input("enter your character's level: ")
character_sex = input("enter your character's sex: ")
while character_sex != "male" and character_sex != "Male" and character_sex != "female" and character_sex != "Female":
    print("while the gender question is wild, the sex one isn't. Please type either male or female: ")
    character_sex = input("enter your character's sex: ")
print("Your character " + character_name + " is a " + character_class + " and is level " + character_level + "!")
if int(character_level) == 100:
    print("GIGACHAD CONFIRMED")
if int(character_level) >= 94 and int(character_level) != 100:
    if character_sex == "male" or character_sex == "Male":
        print("Well, he's practically max level!")
    if character_sex == "female" or character_sex == "Female":
        print("Well, she's practically max level!")
if 94 > int(character_level) >= 75:
    if character_sex == "male" or character_sex == "Male":
        print("He still has some potential, I see!")
    if character_sex == "female" or character_sex == "Female":
        print("She still has some potential, I see!")
if 20 < int(character_level) < 75:
    if character_sex == "male" or character_sex == "Male":
        print("He has a lot of room for growth, I see!")
    if character_sex == "female" or character_sex == "Female":
        print("She has a lot of room for growth, I see!")
if int(character_level) <= 20:
    print("Well that's a fucking noob if ever I saw one!")

"""
Αν θέλουμε να επιτρέψουμε στο input να δέχεται κείμενο πολλαπλών γραμμών μπορούμε να χρησιμοποιήσουμε κάτι σαν τον
ακόλουθο κώδικα.

print("κείμενο:")
text = ""
while True:
    newText = input()
    if not newText:
        break
    text += newText.strip() + " "
print(text)

"""
