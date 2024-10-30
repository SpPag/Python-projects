character_name = "George"
character_age = "70"
print("There was once a man named " + character_name + ",")
print("and he was " + character_age + " years old,")
print("he liked the name " + character_name + ",")
print("but he really didn't like being " + character_age + " years old.")
character_name = "John"
character_age = "15"
print("There was once a man named " + character_name + ",")
print("and he was " + character_age + " years old,")
print("he liked the name " + character_name + ",")
print("but he really didn't like being " + character_age + " years old.")

print("we can also insert a line change in a string,\nlike so")
print("also, if we want to print a quotation mark, we can do so by using the backslash (or escape) character")
print("\"like so")

phrase = "The night is dark"
print(phrase + " and full of Terrans")
print("I SAID " + phrase.upper())
print(phrase.isupper())
print(phrase.islower())
print(phrase.upper().isupper())
print("The function \"len\" provides the length of a phrase (in characters)")
print(len(phrase))
print("Using square brackets I can modify the \"phrase\" function to provide me with the nth character in the "
      "stored phrase. The first character occupies the position 0")
print(phrase[4])
print("I can also use the \"index\" function to get the position of a character or string in a string")
print(phrase.index("i"))
print(phrase.index("s"))
print(phrase.index("is"))
print("the \"replace\" function is quite simple")
print(phrase.replace("dark","obscure"))
