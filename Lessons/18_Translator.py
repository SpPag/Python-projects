# let's design a translator that does one very simple thing. It changes every vowel in the phrase provided by the user
# into "G" or "g", depending on the capitalization of the provided phrase


def translation(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation


print(translation(input("Please enter a phrase: ")))
