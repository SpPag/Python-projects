dd = {}
text = ""
while True:
    added_text = input("add text, otherwise press ENTER to finish: ")
    text = text + " " + added_text
    if added_text == "":
        break
text = text.lower()
intonation_removal = {
    "ά" : "α",
    "έ" : "ε",
    "ή" : "η",
    "ί" : "ι",
    "ό" : "ο",
    "ύ" : "υ",
    "ώ" : "ω",
}
for char in text:
    if char.isalpha():
        if char in intonation_removal:
            char = intonation_removal.get(char)
        dd[char] = dd.get(char, 0) + 1
for entry in sorted(dd.keys()):
    print(entry, ":", dd.get(entry))
