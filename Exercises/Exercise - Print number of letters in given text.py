dd = {}
text = input("Please write your text here: \n")
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
